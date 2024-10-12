from flask import Flask
from database import fetch_table

app = Flask(__name__)

@app.route("/")
def hello_world():
    orders = fetch_table()
    result = ""
    for order in orders:
        order = ", ".join(order)
        print(order)
        result += f"<p>{order}</p>"
            
    return result