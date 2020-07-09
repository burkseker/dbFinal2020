from flask import Flask
from flask import render_template 
import sqlite3

app = Flask(__name__)



@app.route("/")
def food_group():
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM food_group')
    
    try:
        return render_template('food_groups.html',title='Food Groups', rows = c.fetchall())
    finally:
        conn.close()


@app.route("/food/<int:food_group_id>/", methods=['GET', 'POST'])
def foods(food_group_id):
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM food WHERE food_group_id=?',[food_group_id])
    x = conn.cursor()
    x.execute('SELECT * FROM food_group WHERE id=?',[food_group_id])

    try:
        return render_template('food.html',title='Food', rows = c.fetchall(),food_group_name =x.fetchall())
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080, debug=True)
