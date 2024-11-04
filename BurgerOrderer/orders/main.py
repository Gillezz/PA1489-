"""
Initializes the Flask app, creates the database if it doesn't exist, 
and defines routes for the home page and order processing.
Handles form submissions to create burger orders and manage success/error messages.
"""

from flask import Flask, flash, redirect,request, render_template, url_for
from config import Config, create_database_if_not_exists
from burger_model import db, Orders
from burgers import burgers

app = Flask(__name__)
create_database_if_not_exists()
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

#home page
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/order', methods=['POST']) 
def read_form():
    try:
        burger_information = request.form
        burger_name = burger_information["burgerName"]
        burger = burgers[burger_name]

        if len(burger_information) != 1:
            for ingredient in burger_information:
                if ingredient == "burgerName":
                    continue
                burger[ingredient] = False

        burger_order = Orders(**burger)
        db.session.add(burger_order)
        db.session.commit()
        flash("Order has been created!", "success")
        return redirect(url_for("home"))
    except Exception:
        db.session.rollback()
        flash("Something went wrong!", "error")
        return redirect(url_for("home"))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


