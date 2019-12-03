import os


class Config:
    SECRET_KEY ='924aa84d9830e3138f9caeb669c646dd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    QUOTE_API ='http://quotes.stormconsultancy.co.uk/random.json'
    QUOTE_API_KEY = os.environ.get('QUOTE_API_KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}