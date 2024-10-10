"""
setting up flask framework 
"""
import json
from datetime import datetime
from flask import Flask, request

kitchen = Flask(__name__)

@kitchen.route('/')
def home():
    """
    Starting site display
    """
    return "Welcome to the Burger Ordering Service!"

@kitchen.route('/buy/<burger_name>')
def receive_order(burger_name):
    """
    order info about what items to get
    """
    # add-ons list

    add_ons = request.args.to_dict()

    # order details printed to the display image

    print(f'Ordering {burger_name} with the following add-ons: ')

    for add_on, content in add_ons.items():
        print(f"- {add_on}: {content}")

    # Adding timestamp to the order

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Order recived at: {timestamp}")

    # Adding json response

    response = {
        "message": f"Order accpted: {burger_name} with options: {','.join(add_ons.keys())}",
        "timestamp": timestamp
    }



    return json.dumps(response)

if __name__ == '__main__':
    kitchen.run(debug = True, host = '0.0.0.0', port = 5000)
