@app.route('/read-form', methods=['POST']) 
def read_form(): 
    data = request.form 
    print(data)
    print("hej")
    return "hej"
