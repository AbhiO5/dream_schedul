# scheduler.py
import joblib
from datetime import datetime, timedelta

# Load the trained model
model = joblib.load("model/schedule_model.pkl")

def generate_schedule(wake_time, sleep_time, tasks):
    schedule = []
    total_hours = int((sleep_time - wake_time).seconds / 3600)
    time_slots = [wake_time + timedelta(hours=i) for i in range(total_hours)]

    for slot in time_slots:
        hour = slot.hour
        day = datetime.today().weekday()
        predictions = []
        for task in tasks:
            task_name = task["name"]
            encoded_task = 0 if task_name == "Study" else 1 if task_name == "Exercise" else 2
            pred = model.predict([[hour, day, encoded_task]])[0]
            predictions.append((task_name, pred))
        best_task = max(predictions, key=lambda x: x[1])[0]
        schedule.append((slot.strftime('%I:%M %p'), best_task))
    return schedule
