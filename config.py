class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://<username>:'
        '<database password>'
        '@<username>.mysql.pythonanywhere-services.com/'
        '<username>$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False