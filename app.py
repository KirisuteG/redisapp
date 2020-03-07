from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
from datetime import datetime 
import time 
app = Flask(__name__)

# mysql connection

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "199856"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_DB"] = "database0"

mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

@app.route("/index")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    return render_template("index.html", data = data)

@app.route("/", methods=["POST"])
def add_contact():
    if request.method == "POST":
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temperature = request.form["temperature"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data (time, temperature) VALUES (%s, %s)", (time, temperature))
        mysql.connection.commit()
        flash("Data Added Successfully")

    return redirect(url_for("index"))



@app.route("/delete/<string:id>")
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("Data Removed Successfully")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=80, host="localhost", debug=True)
