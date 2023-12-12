import os
from dotenv import load_dotenv
load_dotenv()

#Config.py is used to set some configurations for the py.file
#Development environment is when the application is still in development by the developers.
#They may use less security checks so that they can access stuff easily and make changes to the code.

#Stage environment is for testing the application
#Production environment is when the application is live for the users to use

class BaseConfig:
  """Base configuration"""
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  DEBUG_TB_ENABLED = False
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  BCRYPT_LOG_ROUNDS = 13
  SECRET_KEY = os.environ.get('SECRET_KEY')
  TOKEN_EXPIRATION_DAYS = 30
  TOKEN_EXPIRATION_SECONDS = 0
  UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "static/uploaded_images/"))
  POSTS_PER_PAGE = 50
  MONGO_URI = os.environ.get('MONGO_URI')

class DevelopmentConfig(BaseConfig):
  """Development configuration"""
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  DEBUG_TB_ENABLED = True
  BCRYPT_LOG_ROUNDS = 4

class TestConfig(BaseConfig):
  """Testing configuration"""
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  BCRYPT_LOG_ROUNDS = 4
  TOKEN_EXPIRATION_DAYS = 0
  TOKEN_EXPIRATION_SECONDS = 3

class ProductionConfig(BaseConfig):
  """Production configuration"""
  uri = os.getenv("DATABASE_URL")

  if uri and uri.startswith('postgres://'):
    uri = uri.replace("postgres://", "postgresql://")

  SQLALCHEMY_DATABASE_URI = uri

class StageConfig(BaseConfig):
  """Development configuration"""
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  DEBUG_TB_ENABLED = True
  BCRYPT_LOG_ROUNDS = 4
