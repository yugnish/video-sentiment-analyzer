import os
from flask import Flask, render_template, request
from mailer import mail, send_video
from sentiment_analyzer import analyze_video





app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ygarg1_be25@thapar.edu' # <-- Replace with your email
app.config['MAIL_PASSWORD'] = 'hdwj lsvw fkfj pybn' 



input='uploads'
os.makedirs(input,exist_ok=True)

os.makedirs('output',exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    user_email=request.form['email']
    video_file=request.files['video']

    video_path=os.path.join(input,video_file.filename)
    video_file.save(video_path)

    try:
        report=analyze_video(video_path)

        send_video(app,user_email,report)

        return "your video has been send properlyy"
    finally:
        if os.path.exists(video_path):
            os.remove(video_path)


if __name__=='__main__':
    app.run(debug=True)