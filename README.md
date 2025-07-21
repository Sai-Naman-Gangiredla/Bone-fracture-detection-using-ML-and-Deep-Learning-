
---

## 🛠️ Technology Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, TensorFlow, Keras
- **Image Processing:** Pillow (PIL)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Development:** Jupyter Notebook

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Sai-Naman-Gangiredla/Bone-fracture-detection-using-ML-and-Deep-Learning-.git
cd Bone-fracture-detection-using-ML-and-Deep-Learning-
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
py -3.10 -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Download the Dataset

- Download from [Kaggle](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)
- Place it in a `data/` folder (ignored by Git)

### 5. Run the App

```bash
python app.py
```
- Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

- ![screenshot_upload](https://github.com/user-attachments/assets/2d325ea5-c1f9-48a4-9c1a-e447254518db)
![screenshot_result](https://github.com/user-attachments/assets/c1f63231-c071-4713-ac86-b9c4cb752a0f)

---

## 🧠 Implementation Details

- **X-ray Validation:**  
  Uses a pre-trained MobileNetV2 model and image statistics to ensure only real X-ray images are analyzed.

- **Fracture Detection:**  
  The main ML model (`model/model.pkl`) predicts if the uploaded X-ray is fractured or not.

- **Fracture Type Classification:**  
  If a fracture is detected, the app displays a likely fracture type (e.g., Avulsion, Comminuted, Spiral, etc.), severity, and common locations, using a mapping in the backend.

- **Confidence Score:**  
  The app shows the model’s confidence in its prediction.

- **Frontend:**  
  Built with Bootstrap for a modern, responsive look.  
  The UI includes a navbar, logo, upload form, result card, and error handling.

- **No Dataset in Repo:**  
  The dataset is not included due to size. Download it from Kaggle if you want to retrain the model.

---

## 📂 Dataset

- **Not included in this repo!**
- Download from Kaggle:  
  [Bone Fracture Multi-Region X-ray Data](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)

---

## 👨‍💻 Author

- G. Sai Naman

---

## 📜 License

This project is for educational and research purposes.

---

## 🙏 Acknowledgements

- [Kaggle Dataset](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)
- [Bootstrap](https://getbootstrap.com/)

---

## 💡 Tips

- To retrain the model, use the Jupyter notebook in the `notebooks/` folder.
- For best results, use clear, high-resolution X-ray images.
- If you encounter issues, check your Python version and ensure all dependencies are installed.

---

##  Imp note 

- In this current implementation, the fracture type and details are being assigned randomly whenever the model predicts "fractured."

- It is because this model is a binary classifier (it only predicts "fractured" or "not fractured"), and the code then randomly selects a fracture type from a list for demonstration purposes.

- This means every time a fracture is detected, the app picks a random fracture type and shows its details.

- The details (description, severity, locations) are correct for each type, but the type itself is not based on the actual image.

- How to Make It Real:

- If you want the app to actually classify the type of fracture (e.g., Avulsion, Spiral, etc.),
You need to:
Train a multi-class classification model (not just binary) using labeled data for each fracture type.
Update your model training code in the Jupyter notebook to predict the specific fracture type.
Update your Flask app to use the model’s predicted class directly, instead of picking randomly.

---

