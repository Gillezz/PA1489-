# setting up flask framework 

from flask import Flask, request

kitchen = (__name__)

@kitchen.route('/buy/<burger_name>')

def receive_order(burger_name):
    
# add-ons list

    add_ons = request.args.to_dict()

# order details printed to the display image

    print(f'Ordering {burger_name} with the following add-ons: ')

    for add_ons, content in add_ons.items():
        print(f"- {add_ons}: {content}")

    return f"Order accepted {burger_name} with add-ons contents: {', '.join(add_ons.keys())}",

if __name__ == '__main__':
    
    kitchen.run(debug = True, host = '0.0.0.0', port = 5000)



