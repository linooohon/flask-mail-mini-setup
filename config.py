import os
import dotenv
dotenv.load_dotenv()


class BaseConfig(object):
    DEBUG = False # 為 True 的話，code 有改動，Flask 會自動重啟(app.run)
    TESTING = False

class GmailConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    
    # MAIL Config
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME='lifeplaylistforfun@gmail.com' # MAIL_USERNAME 一定要放上 email 帳號
    MAIL_DEFAULT_SENDER='lifeplaylistforfun@gmail.com'
    MAIL_PASSWORD=os.getenv('LIFEPLAYLISTFORFUN_PASSWORD')

class SendgridConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    
    # MAIL Config
    MAIL_SERVER='smtp.sendgrid.net'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='apikey' # MAIL_USERNAME 一定要放上 apikey
    MAIL_DEFAULT_SENDER='lifeplaylistforfun@gmail.com'
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    SENDGRID_WEB_API_KEY=os.getenv('SENDGRID_WEB_API_KEY') # 這個也可以，跟 MAIL_PASSWORD 是一樣可以用的，可以去 https://app.sendgrid.com/guide/integrate/langs/python 拿到


config = {
    'gmail': GmailConfig,
    'sendgrid': SendgridConfig,
}
