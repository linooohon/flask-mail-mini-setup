from flask import Flask
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient, Content
import config

app = Flask(__name__)

def send_email():
    subject = 'hello'
    to_emails = 'linooohon@gmail.com'
    from_email = 'lifeplaylistforfun@gmail.com'
    mail_html = Content('text/html', '<h1>Test Mail</h1><p>From Sendgrid Web API</p>')
    msg = Mail(from_email, to_emails, subject, mail_html)
    try:
        sg = SendGridAPIClient(config.config['sendgrid']().MAIL_PASSWORD)
        response = sg.send(msg)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

@app.route('/')
def index():
    send_email()
    return 'Flask app 已啟動，沒報錯的話信已寄出'


if __name__ == '__main__':
    app.run()