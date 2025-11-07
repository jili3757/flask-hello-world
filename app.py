from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://jinny_render_db_user:LWmku3hpecib7ktldE2aG4F7tF8SEUGa@dpg-d46pkh6r433s738c7bhg-a/jinny_render_db")
    conn.close()
    return "Database Connection Sucessful"
