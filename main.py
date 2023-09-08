# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, app
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        price = request.form['price']

        # 存储数据到数据库
        conn = sqlite3.connect('signing_sheet.db')
        c = conn.cursor()
        c.execute("Insert into signing_sheet (name, phone, email, price) values (?,?,?,?)",
                  (name, phone, email, price))
        conn.commit()
        conn.close()

        return 'Thank you for signing in!'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
