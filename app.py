import streamlit as st
from datetime import datetime, time
from scheduler import generate_schedule
import os
import json

# Page config
st.set_page_config(page_title="AI Dream Schedule Creator", layout="centered")
st.title("🧠 AI Dream Schedule Creator")

# User identity
username = st.text_input("Enter your name", "Guest")
profile_path = f"model/{username}_prefs.json"

# Default values
wake = st.time_input("Wake-Up Time", time(7, 0))
sleep = st.time_input("Sleep Time", time(22, 0))

st.markdown("### Select Task Durations")
study_duration = st.slider("Study (hrs)", 1, 8, 4)
exercise_duration = st.slider("Exercise (hrs)", 1, 4, 2)
breaks_duration = st.slider("Breaks/Leisure (hrs)", 1, 4, 2)

# Try loading saved preferences
if os.path.exists(profile_path):
    st.markdown(f"🔁 Loaded saved preferences for **{username}**")
    with open(profile_path, "r") as f:
        prefs = json.load(f)
        wake = time.fromisoformat(prefs["wake"])
        sleep = time.fromisoformat(prefs["sleep"])
        study_duration = prefs["tasks"]["Study"]
        exercise_duration = prefs["tasks"]["Exercise"]
        breaks_duration = prefs["tasks"]["Breaks"]

# Save preferences button
if st.button("💾 Save Preferences"):
    prefs = {
        "wake": wake.strftime("%H:%M"),
        "sleep": sleep.strftime("%H:%M"),
        "tasks": {
            "Study": study_duration,
            "Exercise": exercise_duration,
            "Breaks": breaks_duration
        }
    }
    with open(profile_path, "w") as f:
        json.dump(prefs, f)
    st.success("✅ Preferences saved!")

# Show model accuracy if available
try:
    with open("model/accuracy.txt", "r") as f:
        accuracy = f.read().strip()
        st.info(f"📊 Model Accuracy: {accuracy}")
except:
    st.warning("⚠️ Model not yet trained. Run train_model.py.")

# Generate schedule
schedule = []

if st.button("🗓️ Generate Schedule"):
    tasks = [
        {"name": "Study", "duration": study_duration},
        {"name": "Exercise", "duration": exercise_duration},
        {"name": "Breaks", "duration": breaks_duration}
    ]
    wake_dt = datetime.combine(datetime.today(), wake)
    sleep_dt = datetime.combine(datetime.today(), sleep)
    schedule = generate_schedule(wake_dt, sleep_dt, tasks)

    st.success("✅ Here’s your personalized schedule:")
    for time_slot, task in schedule:
        st.write(f"🕒 {time_slot} - {task}")

# Feedback section
if schedule:
    st.markdown("### 📝 Task Completion Feedback")
    feedback = []
    for i, (time_slot, task) in enumerate(schedule):
        done = st.selectbox(f"{time_slot} - {task}", ["Yes", "No"], key=i)
        feedback.append((time_slot, task, 1 if done == "Yes" else 0))

    if st.button("📤 Submit Feedback"):
        import csv
        with open("model/feedback.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for row in feedback:
                hour = int(datetime.strptime(row[0], '%I:%M %p').hour)
                task_type = {"Study": 0, "Exercise": 1, "Breaks": 2}[row[1]]
                writer.writerow([hour, datetime.today().weekday(), task_type, row[2]])
        st.success("✅ Feedback saved and will improve future schedules!")
