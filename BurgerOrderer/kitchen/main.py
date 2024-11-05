"""
Initializes the Flask application, sets up the database, 
and defines a route to display filtered orders from the database.
"""

from flask import Flask, render_template
from config import Config
from burger_model import db, Orders
import unittest
from test import TestCreateDatabaseIfNotExists

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/', methods=['GET'])
def display_orders():
    orders = Orders.query.all()
    orders_list = [order.to_dict() for order in orders]
    filtered_orders_list = [
        {key: value for key, value in order.items() if value is not False and key != 'id' and key != 'burgerName'}
        for order in orders_list
    ]            
    return render_template('index.html', orders=filtered_orders_list)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDatabaseIfNotExists)
    unittest.TextTestRunner().run(suite)
    app.run(host="0.0.0.0", port=5001, debug=True)