import os



class Config:

    
    SECRET_KEY = '12345'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URL=os.environ.get("DATABASE_URL")



class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URL=os.environ.get("DATABASE_URL")

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}