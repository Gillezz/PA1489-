"""
setting up flask framework 
"""

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

    return f"Order accepted {burger_name} with add-ons contents: {', '.join(add_ons.keys())}"

if __name__ == '__main__':
    kitchen.run(debug = True, host = '0.0.0.0', port = 5000)
