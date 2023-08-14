# config.py

# Import the necessary libraries
from urllib.parse import quote_plus

# Define the configuration variables
SECRET_KEY = 'qwertyuiopasdfghjklzxcvbnm'
password = quote_plus('Mysql@123')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{password}@localhost/mydb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
