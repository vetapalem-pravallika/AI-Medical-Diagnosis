AI-Powered Medical Diagnosis System
An AI-driven system for predicting diseases using machine learning.

📖 Table of Contents
Overview
Features
Installation
Usage
Technologies Used
Dataset
Results
Contributing
License
📌 Overview
This project aims to develop an AI-powered medical diagnosis system that enhances disease prediction accuracy. It uses machine learning models trained on medical datasets to predict conditions such as Diabetes, Heart Disease, Parkinson's Disease, Lung Cancer, and Hypo-Thyroidism.

🔥 Features
✅ Predicts multiple diseases using trained ML models
✅ Streamlit web interface for user-friendly interaction
✅ Uses SVM and other ML models for prediction
✅ Supports real-time input for diagnosis

⚙️ Installation
Step 1: Install Python
Ensure Python (3.x) is installed on your system.
👉 Download from Python Official Site

After installation, verify it by running the following command in Command Prompt:
python --version
🔹 Step 2: Install Required Libraries
Open Command Prompt and install the necessary dependencies using:
pip install numpy pandas scikit-learn streamlit pickle5
🔹 Step 3: Running the Code in Jupyter Notebook
1️⃣ Install Jupyter Notebook if not installed:
  pip install notebook
2️⃣ Start Jupyter Notebook:
jupyter notebook
3️⃣ Open the notebook (model.ipynb) and run the cells step by step.
🔹 Step 4: Running the Code in Command Prompt (Streamlit Web App)
If your project file is model.py, execute it using:
streamlit run model.py
This will open a browser window with the AI-powered medical diagnosis interface.

🚀 Usage
Open the Streamlit web app.
Select a disease to diagnose.
Enter the required medical parameters.
Click the Predict button to get results.
🛠 Technologies Used
Python
Streamlit (Frontend)
Scikit-learn (Machine Learning)
Pandas & NumPy (Data Processing)
📊 Dataset
The project uses medical datasets like:

Parkinson's Disease Dataset
Heart Disease UCI Dataset
Diabetes Prediction Dataset
🔗 Dataset Source

📈 Results
✅ Achieved 90%+ accuracy in Parkinson’s Disease prediction.
✅ Optimized ML models for fast processing.

🤝 Contributing
Fork the repository
Create a new branch (feature-branch)
Commit changes and push (git push origin feature-branch)
Open a pull request
📜 License
This project is open-source under the MIT License.

