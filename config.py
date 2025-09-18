class Config:
    #Replace "yourusername" with your PostgreSQL username and "yourpassword" with your PostgreSQL password
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pass1234@localhost/stocks_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dh83ew9k'
