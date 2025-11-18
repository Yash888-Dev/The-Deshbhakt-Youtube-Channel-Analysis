#**📊 YouTube Video Popularity Predictor**

A Machine-Learning powered Streamlit web application that predicts whether a YouTube video will be Popular or Not Popular based on engagement metrics such as likes, comments, views, and more. Designed for content creators, analysts, and ML beginners looking for a practical end-to-end project.


#**🚀 Features**

---🧠 Pre-trained ML Model stored as The Deshbhakt.pkl
---🎛️ Clean & Interactive Streamlit UI
---🔢 Input fields for:
	Likes
	Comments
	Views
	Likes-per-View
	Comments-per-View
	Is Short Video (<60 sec)
	Publish Day
	Publish Month
---⚡ Instant Popularity Prediction
---📂 Organized and lightweight project structure
---📈 Helps creators estimate video performance


**🚀 Demo**
Run locally using Streamlit:

'''bash
streamlit run The Deshbhakt.py
'''


**🧩 Project Structure**
├── The Deshbhakt.py        # Streamlit app (UI + Prediction logic)
├── The Deshbhakt.pkl       # Trained ML model
├── videos_data.csv         # Training dataset
└── README.md               # Project documentation


**🛠️ Tech Stack**
---Python 3.8+
---Streamlit
---Pandas
---NumPy
---scikit-learn
---Pickle

**⚙️ How It Works**

The Streamlit UI collects input features and prepares a DataFrame:

---likes
---comments
---views
---likes_per_view
---comments_per_view
---is_short
---publish_day
---publish_month

The model (loaded from The Deshbhakt.pkl) predicts:
---1 → Popular 🎉
---0 → Not Popular 😐

This logic is handled in The Deshbhakt.py using:

'''bash
prediction = model.predict(input_data)[0]
'''


**🧠 Model Training Overview**

Although the training script is not included in this repo, the model was trained using:
---Data from videos_data.csv
---Supervised binary classification
---Feature engineering (ratio features, short-video flag)
---Standard ML pipeline (cleaning → training → evaluation → export as .pkl)

Model stored using Python’s pickle module.

**▶️ Running the Project**

1️⃣ Install dependencies

'''bash
pip install streamlit pandas numpy scikit-learn
'''

2️⃣ Run the app

'''bash
streamlit run The Deshbhakt.py
'''

3️⃣ Use the UI
Enter video metrics → Get prediction instantly.


**🧑‍💻 Author**
**YASH SARWATE**
