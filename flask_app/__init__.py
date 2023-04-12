from flask import Flask

app = Flask(__name__)
app.secret_key = 'Harry Potter was mid'

DATABASE = 'users_schema'
