import os

dir_path = os.path.dirname(__file__)
base_dir = os.path.abspath(dir_path)


class BaseConfig:
    # General flask app configure

    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_SECURE = True
    # Celery Configure
    # This broker is for localhost
    # CELERY_BROKER_URL =  'amqp://guest@localhost//'
    db = 'mongodb://'
    param_con = 'user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'
    res_bkend = db + param_con
    # string connection for Yo host
    CELERY_BROKER_URL = 'amqp://devcrack:mientras123@192.168.56.101:5672//'
    # string connection for yeyo host
    # CELERY_BROKER_URL = 'amqp://devcrack:mientras123@192.168.100.28:5672//'
    CELERY_RESULT_BACKEND = res_bkend
    # Reference to celery task files.
    # CELERY_INCLUDE = ['main.task_s.task1']


class Development_Config(BaseConfig):
    DEBUG = True
