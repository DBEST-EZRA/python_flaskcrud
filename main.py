from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crudphp"
)


@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM crud_table"
    cursor.execute(query)
    result = cursor.fetchall()
    return render_template('index.html', data=result)


@app.route('/add', methods=['POST'])
def add():
    cursor = db.cursor()
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    i_d = request.form['i_d']
    query = "INSERT INTO crud_table (crud_name, crud_email, crud_phone, crud_id) VALUES(%s, %s, %s, %s)"
    values = (name, email, phone, i_d)
    cursor.execute(query, values)
    db.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST',])
def update(id):
    if request.method == 'POST':
        cursor = db.cursor()
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        i_d = request.form['i_d']
        query = "UPDATE crud_table SET crud_name=%s, crud_email=%s, crud_phone=%s, crud_id=%s WHERE id=%s"
        values = (name, email, phone, i_d, id)
        cursor.execute(query, values)
        db.commit()
        return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    cursor = db.cursor()
    query = "DELETE FROM crud_table WHERE id=%s"
    value = (id, )
    cursor.execute(query, value)
    db.commit()
    return redirect(url_for('index'))



@app.route('/insert')
def insert():
    return render_template('insert.html')


@app.route('/edit/<int:id>')
def edit(id):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM crud_table WHERE id=%s"
    value = (id,)
    cursor.execute(query, value)
    row = cursor.fetchone()
    return render_template('edit.html', row=row)


if __name__ == '__main__':
    app.run(debug=True)
