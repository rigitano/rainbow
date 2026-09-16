from flask import Flask, render_template, request, jsonify
import json


app = Flask(__name__)

def load_config():
    with open('config.json') as f:
        return json.load(f)
    
def load_colorconfig():
    with open('colorconfig.json') as f:
        return json.load(f)

@app.route('/')
def index():
    config_data = load_config()
    colorconfig_data = load_colorconfig()
    return render_template('index.html', config=config_data, colorconfig=colorconfig_data)

@app.route('/submit', methods=['POST'])
def submit():
    # This endpoint receives the data when an OK button is clicked.
    d_received_from_frontend = request.get_json()
    print("Received data:", d_received_from_frontend)  # Process or call the specific function here.

    #get the function name and arguments. these are the keys in the dictionary "received_from_frontend"
    function_name = d_received_from_frontend['functionCall']
    arguments = d_received_from_frontend['data']

    #the function stored in function_name will be called. so we need to import the file where the function is present
    import myfunctions

    #call the function with those arguments. the function should be present in myfunctions.py
    if hasattr(myfunctions, function_name):#check if the function is present in myfunctions.py
        func = getattr(myfunctions, function_name)
        if callable(func):
            try:
                if isinstance(arguments, dict):
                    result = func(**arguments)  # HERE IS THE FUNCTION CALL with keyword arguments
                elif isinstance(arguments, list):
                    result = func(*arguments)   # HERE IS THE FUNCTION CALL with positional arguments
                else:
                    raise TypeError(f"Expected 'arguments' to be a dictionary or list, got {type(arguments).__name__}.")
                
                #print("Function called:", f"{function_name}({arguments})")
                print("Function result:\n", result)
            except TypeError as e:
                raise TypeError(f"Error calling function '{function_name}': {e}")
        else:
            raise TypeError(f"{function_name} is not callable.")
    else:
        raise AttributeError(f"Function {function_name} not found in myfunctions.")


    #return string explainig what funcion was called and the results to js, to be displayed in the frontend as a alert message
    explanatory_string = f"Function called: {function_name}({arguments})\nResult: {result}"
    return jsonify(result=explanatory_string)





if __name__ == '__main__':
    app.run(debug=True)
