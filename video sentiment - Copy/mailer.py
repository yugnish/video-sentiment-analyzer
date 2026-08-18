from flask_mail import Mail,Message
mail=Mail()
def send_video(app,user_email,report):
    mail.init_app(app)
    msg=Message("your result",
                sender="yugnishg@gmail.com",
                recipients=[user_email],
                body="here is your video")
    msg.body=report
    mail.send(msg)

