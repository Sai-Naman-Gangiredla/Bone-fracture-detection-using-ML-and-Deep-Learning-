    # Bone Fracture Detection using Deep Learning

    This web application uses a machine learning model to analyze X-ray images and detect bone fractures. Users can upload an image, and the system will classify whether the bone is fractured or not, providing a confidence score and details about the fracture type.

    ![App Screenshot](https://i.imgur.com/8IVm98d.png) <!-- You can replace this with a real screenshot of your app -->

    ---

    ## Features

    -   **Image Upload**: Simple and intuitive interface to upload X-ray images.
    -   **Advanced X-ray Validation**: A multi-step validation process checks if the uploaded image is a valid X-ray before analysis.
    -   **Binary Fracture Classification**: The model predicts whether the bone is `fractured` or `not fractured`.
    -   **Detailed Fracture Information**: For a "fractured" prediction, the app provides details on a possible fracture type, its severity, and common locations.
    -   **Confidence Score**: Displays the model's confidence in its prediction.
    -   **Responsive UI**: The user interface is built with Bootstrap and is usable on both desktop and mobile devices.

    ---

    ## Technology Stack

    -   **Backend**: Python, Flask
    -   **Machine Learning**: Scikit-learn, TensorFlow, Keras
    -   **Image Processing**: Pillow (PIL)
    -   **Frontend**: HTML, CSS, Bootstrap 5
    -   **Development Environment**: Jupyter Notebook (for model development)

    ---

    ## Setup and Installation

    Follow these steps to set up and run the project locally.

    ### 1. Prerequisites

    -   Python 3.10 or 3.11
    -   `pip` (Python package installer)

    ### 2. Clone the Repository

    ```bash
    git clone https://github.com/Sai-Naman-Gangiredla/Bone-fracture-detection-using-ML-and-Deep-Learning-.git
    cd Bone-fracture-detection-using-ML-and-Deep-Learning-
    ```

    ### 3. Create a Virtual Environment

    It is highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    # Create the virtual environment
    py -3.10 -m venv venv

    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    ```

    ### 4. Install Dependencies

    Install all required packages from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

    ### 5. Download the Dataset (Optional)

    The model included in this repository is pre-trained. If you wish to retrain it, download the dataset from Kaggle and place it in a `data/` folder in the project root.

    -   **Dataset Link**: [Bone Fracture Multi-Region X-ray Data](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)

    ---

    ## How to Run the Application

    With your virtual environment activated and dependencies installed, run the Flask application:

    ```bash
    python app.py
    ```

    Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.