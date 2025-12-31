import pyodbc
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "e0539cd6-a361-49f3-a5ac-147297338151"  # required for flash messages

# Azure SQL connection
conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:bspeechtechnologies.database.windows.net,1433;Database=free-sql-db-5234169;Uid=bpeechadmin;Pwd={AbdhulGhani@65};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
   
)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = conn.cursor()
        cursor.execute("SELECT adminpwd FROM adminresource WHERE adminusername = ?",(username,))
        
        row = cursor.fetchone()

        if row: ##and check_password_hash(row[0], password):
            return "✅ Login successful"
        else:
            flash("❌ Invalid username or password")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
