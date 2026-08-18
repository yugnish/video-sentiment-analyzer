# 🎥 Video Sentiment Analysis System

A Flask-based web application that analyzes the emotions expressed in a video using **DeepFace** and **OpenCV**. The system processes uploaded videos, detects facial emotions, generates a sentiment breakdown report, and sends the analysis result directly to the user's email.

---

## 🚀 Features

- Upload video files through a web interface.
- Extract and analyze video frames using OpenCV.
- Detect facial emotions using DeepFace.
- Supports emotions:
  - Angry
  - Disgust
  - Fear
  - Happy
  - Sad
  - Surprise
  - Neutral
- Generates emotion percentage analysis.
- Sends the final sentiment report through email.
- Automatically removes uploaded videos after processing.

---

## 🛠️ Technologies Used

- Python
- Flask
- OpenCV
- DeepFace
- TensorFlow
- Flask-Mail
- SMTP
- HTML/CSS

---

## 📂 Project Structure
Video-Sentiment-Analysis/
 app.py # Main Flask application,
 sentiment_analyzer.py # Video emotion analysis logic,
 mailer.py # Email sending functionality,
 config.py # Configuration settings,

 uploads/ # Temporary uploaded videos,
 output/ # Generated output files,

 templates/
 index.html # Upload webpage,
 README.md.
