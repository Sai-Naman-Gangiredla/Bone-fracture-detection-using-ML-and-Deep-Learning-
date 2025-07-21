from flask import Flask, render_template, request
import joblib
import os
from PIL import Image
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as keras_image

app = Flask(__name__)

# Load models
model = joblib.load('model/model.pkl')
xray_detector = MobileNetV2(weights='imagenet')

def get_fracture_description(fracture_type):
    """
    Returns detailed information about each fracture type.
    NOTE: In a real app, this would come from the multi-class model's output.
    Here, we simulate it based on the binary 'fractured' prediction.
    """
    # Simulate a detailed fracture type for demonstration
    fracture_types = [
        "Avulsion fracture", "Comminuted fracture", "Fracture Dislocation",
        "Greenstick fracture", "Hairline Fracture", "Impacted fracture",
        "Longitudinal fracture", "Oblique fracture", "Spiral fracture",
        "Transverse fracture", "Segmental fracture"
    ]
    # Randomly pick a detailed fracture type if the prediction is "fractured"
    if 'fractured' in fracture_type.lower():
        fracture_type = np.random.choice(fracture_types)

    descriptions = {
        'Avulsion fracture': {
            'name': 'Avulsion Fracture',
            'description': 'An injury where a small piece of bone attached to a tendon or ligament gets pulled away from the main part of the bone.',
            'severity': 'Moderate',
            'common_locations': 'Ankle, Hip, Elbow, Knee'
        },
        'Comminuted fracture': {
            'name': 'Comminuted Fracture',
            'description': 'A severe break where the bone shatters into three or more pieces.',
            'severity': 'Severe',
            'common_locations': 'Often results from high-impact trauma like car accidents.'
        },
        'Fracture Dislocation': {
            'name': 'Fracture Dislocation',
            'description': 'A complex injury where a joint becomes dislocated and one of the bones of the joint also has a fracture.',
            'severity': 'Severe',
            'common_locations': 'Ankle, Wrist, Elbow, Shoulder'
        },
        'Greenstick fracture': {
            'name': 'Greenstick Fracture',
            'description': 'An incomplete fracture where the bone is bent. This type occurs most often in children.',
            'severity': 'Mild to Moderate',
            'common_locations': 'Common in children - Forearm bones'
        },
        'Hairline Fracture': {
            'name': 'Hairline Fracture (Stress Fracture)',
            'description': 'A tiny crack in a bone that is often caused by repetitive force or overuse.',
            'severity': 'Mild',
            'common_locations': 'Foot, Ankle, Tibia (shin bone)'
        },
        'Impacted fracture': {
            'name': 'Impacted Fracture',
            'description': 'A break where the broken ends of the bone are jammed together by the force of the injury.',
            'severity': 'Moderate to Severe',
            'common_locations': 'Often seen in falls from a height; affects long bones.'
        },
        'Longitudinal fracture': {
            'name': 'Longitudinal Fracture',
            'description': 'A fracture that follows the length of the bone.',
            'severity': 'Moderate',
            'common_locations': 'Long bones like the tibia or femur.'
        },
        'Oblique fracture': {
            'name': 'Oblique Fracture',
            'description': 'A fracture where the break has a curved or sloped pattern.',
            'severity': 'Moderate to Severe',
            'common_locations': 'Long bones'
        },
        'Spiral fracture': {
            'name': 'Spiral Fracture',
            'description': 'A type of fracture caused by a twisting force, creating a spiral-like break line.',
            'severity': 'Moderate to Severe',
            'common_locations': 'Long bones, commonly in sports injuries.'
        },
        'Transverse fracture': {
            'name': 'Transverse Fracture',
            'description': 'A fracture where the break is a straight line across the bone.',
            'severity': 'Moderate',
            'common_locations': 'Long bones'
        },
        'Segmental fracture': {
            'name': 'Segmental Fracture',
            'description': 'A severe injury where a bone is fractured in two separate places, leaving a "floating" segment of bone.',
            'severity': 'Severe',
            'common_locations': 'Long bones, particularly the tibia.'
        }
    }
    return descriptions.get(fracture_type)


def is_valid_xray(img_path):
    """
    Multi-factor validation for X-ray images with more lenient thresholds
    """
    try:
        # Open and convert image to grayscale
        img = Image.open(img_path).convert('L')
        
        # 1. Basic image property checks
        width, height = img.size
        aspect_ratio = width / height
        if not (0.2 <= aspect_ratio <= 5.0):  # More lenient aspect ratio
            return False
            
        # 2. Check pixel intensity distribution
        img_array = np.array(img)
        mean_intensity = np.mean(img_array)
        std_intensity = np.std(img_array)
        
        if mean_intensity < 20 or mean_intensity > 235:  # Wider range
            return False
        if std_intensity < 10:  # Lower threshold for variation
            return False
            
        # 3. MobileNetV2 backup check with more lenient thresholds
        img_color = Image.open(img_path).convert('RGB')
        img_color = img_color.resize((224, 224))
        x = keras_image.img_to_array(img_color)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        preds = xray_detector.predict(x, verbose=0)
        decoded = decode_predictions(preds, top=10)[0]
        
        medical_terms = [
            'x-ray', 'radiograph', 'medical', 'bone', 'scan', 'microscope',
            'diagnostic', 'skeletal', 'fracture', 'joint', 'limb', 'tissue'
        ]
        
        for _, term, confidence in decoded:
            if any(med_term in term.lower() for med_term in medical_terms) and confidence > 0.001:
                return True
                
        if decoded[0][2] > 0.95 and not any(med_term in decoded[0][1].lower() for med_term in medical_terms):
            return False
            
        return True
        
    except Exception as e:
        print(f"Error in X-ray validation: {str(e)}")
        return False

def preprocess_image(image_path):
    img_size = (128, 128)
    img = Image.open(image_path).convert('L').resize(img_size)
    img_array = np.array(img).flatten().reshape(1, -1)
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'xray' not in request.files or request.files['xray'].filename == '':
            return render_template('index.html', error="No file selected. Please upload an image.")
            
        file = request.files['xray']
        
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        
        if not is_valid_xray(filepath):
            # os.remove(filepath) # Keep the file for debugging if needed
            return render_template('result.html', 
                                 error="The uploaded image does not appear to be an X-ray. Please upload a valid X-ray image.",
                                 image=file.filename)
        
        try:
            img_data = preprocess_image(filepath)
            prediction = model.predict(img_data)[0]
            confidence = None
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(img_data)[0]
                confidence = round(max(proba) * 100, 2)
            
            fracture_info = None
            if 'fractured' in prediction.lower():
                fracture_info = get_fracture_description(prediction)

            return render_template('result.html',
                                 prediction=prediction,
                                 confidence=confidence,
                                 image=file.filename,
                                 fracture_info=fracture_info)
        except Exception as e:
            # os.remove(filepath)
            return render_template('result.html', 
                                 error=f"Error processing image: {str(e)}",
                                 image=file.filename)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)