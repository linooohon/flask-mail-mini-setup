from flask import Flask
from flask_mailman import Mail
from flask_mailman import EmailMessage
import config

app = Flask(__name__)
app.config.from_object(config.config['gmail'])

mail = Mail()
mail.init_app(app)

def send_email():
    subject = 'hello'
    from_email = 'lifeplaylistforfun@gmail.com'
    to = 'linooohon@gmail.com'
    html_content = '<h1>Test Mail</h1><p>From flask_mailman module, using gmail config</p>'
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = 'html'
    response = msg.send()
    print(response)

@app.route('/')
def index():
    send_email()
    return 'Flask app 已啟動，沒報錯的話信已寄出'


if __name__ == '__main__':
    app.run()