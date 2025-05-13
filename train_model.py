import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Create synthetic dataset
np.random.seed(42)
data = []
task_types = {"Study": 0, "Exercise": 1, "Breaks": 2}
for _ in range(300):
    hour = np.random.randint(6, 22)
    day = np.random.randint(0, 7)
    task = np.random.choice(list(task_types.keys()))
    task_encoded = task_types[task]
    if task == "Study":
        completed = int(6 <= hour <= 11)
    elif task == "Exercise":
        completed = int(17 <= hour <= 20)
    else:
        completed = int(12 <= hour <= 15)
    data.append([hour, day, task_encoded, completed])

df = pd.DataFrame(data, columns=["Hour", "Day", "TaskType", "Completed"])

# 🔁 Append feedback if available BEFORE training
feedback_path = "model/feedback.csv"
if os.path.exists(feedback_path):
    feedback_df = pd.read_csv(feedback_path, names=["Hour", "Day", "TaskType", "Completed"])
    df = pd.concat([df, feedback_df], ignore_index=True)

# Train model
X = df[["Hour", "Day", "TaskType"]]
y = df["Completed"]
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/schedule_model.pkl")

# Accuracy
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

with open("model/accuracy.txt", "w") as f:
    f.write(f"{accuracy:.2f}")
