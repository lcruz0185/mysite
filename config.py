class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://lcruz0185:'
        'ineedamiracle'
        '@lcruz0185.mysql.pythonanywhere-services.com/'
        'lcruz0185$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'eifheifjgifjeihfsdnvbncxkahefeigjiehf'