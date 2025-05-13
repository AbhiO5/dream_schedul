# 🧠 AI Dream Schedule Creator

**AI Dream Schedule Creator** is an intelligent daily planner that generates a personalized, optimized schedule based on your wake/sleep cycle, task preferences, and feedback. It learns over time using a machine learning model to adapt to your productivity patterns.

---

## 📌 Features

- ⏰ Personalized schedule generation based on user input
- 🤖 Machine learning–based task time prediction using Decision Trees
- 🎯 Task prioritization system
- 📈 Real-time feedback loop for learning user behavior
- 👤 Save and load user preferences
- 📊 Model accuracy tracking
- 🧠 Built with Python and Streamlit

---

## 🖼️ Sample Output

🕒 07:00 AM - Study
🕒 08:00 AM - Study
🕒 09:00 AM - Exercise
🕒 10:00 AM - Breaks


---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit (UI)
- Scikit-learn (ML model)
- Pandas, NumPy (data handling)
- Joblib (model saving)
- DecisionTreeClassifier (task time prediction)

---

## 🧪 How It Works

1. User inputs wake-up and sleep times, task preferences, and priorities.
2. The ML model (trained on synthetic + feedback data) predicts the best task for each hour.
3. The schedule is generated and shown in an interactive UI.
4. User submits task completion feedback.
5. The model is retrained using new feedback to improve predictions.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-dream-schedule-creator.git
cd ai-dream-schedule-creator
