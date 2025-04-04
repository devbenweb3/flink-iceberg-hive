# superset_config.py
from superset.config import *  # Kế thừa toàn bộ cấu hình mặc định

# Cấu hình cơ bản
SUPERSET_WEBSERVER_PORT = 8088
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@superset_db:5432/superset"
SECRET_KEY = 'thisISaSECRET_1234'