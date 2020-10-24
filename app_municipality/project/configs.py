class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}:{}/{}'.format(
        'postgres',
        'postgres2',
        'db_municipality',
        '5432',
        'municipality'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):

    SQLALCHEMY_ECHO = False
