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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://jinny_render_db_user:LWmku3hpecib7ktldE2aG4F7tF8SEUGa@dpg-d46pkh6r433s738c7bhg-a/jinny_render_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Sucessfully Created"
