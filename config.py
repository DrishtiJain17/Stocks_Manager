class Config:
    #Replace "yourusername" with your PostgreSQL username and "yourpassword" with your PostgreSQL password
    SQLALCHEMY_DATABASE_URI = 'postgresql://yourusername:yourpassword@localhost/stocks_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dh83ew9k'
