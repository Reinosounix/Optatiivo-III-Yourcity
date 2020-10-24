class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}:{}/{}'.format(
        'postgres',
        'postgres1',
        'db_users',
        '5432',
        'users'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):

    SQLALCHEMY_ECHO = False
