from flask import Flask
from flask import redirect, url_for, render_template, request 
import sqlite3
from forms import Update

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

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

@app.route("/viewfood/<int:food_id>/", methods=['GET', 'POST'])
def viewfood(food_id):

    conn = sqlite3.connect('database.db')
    d = conn.cursor()
    d.execute('SELECT * FROM food WHERE id=?',[food_id])
    row = d.fetchall()
    m = conn.cursor()
    m.execute('SELECT * FROM food_group WHERE id=?',[row[0][1]])

    

    try:
        return render_template('view_food.html',title='ViewFood',rows =row,food_group_name=m.fetchall())
    finally:
        conn.close()

@app.route("/update/<int:food_id>/", methods=['GET', 'POST'])
def updatefood(food_id):
    
    conn = sqlite3.connect('database.db')
    d = conn.cursor()
    d.execute('SELECT * FROM food WHERE id=?',[food_id])
    row = d.fetchall()
    m = conn.cursor()
    m.execute('SELECT * FROM food_group')
    food_group_name=m.fetchall()
    form=Update()
    
    form.group.choices=food_group_name
    
    if (form.validate_on_submit()):
        x = conn.cursor()
        x.execute('''UPDATE food SET
            food_group_id=?, long_desc=?, short_desc=?, manufac_name=?, sci_name=?  
            WHERE id=?''',(form.group.data,form.longdes.data,form.shortdes.data,
            form.manu.data,form.sci.data,food_id))
        conn.commit()
                
        return redirect(url_for('food_group'))
    print(row[0][0])

    try:
        return render_template('update_food.html',title='UpdateFood',
        rows =row,form=form)
    finally:
        conn.close()



if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080, debug=True)
