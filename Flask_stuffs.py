from flask import Flask,request, jsonify

""" Importing Flask, jsonify, request from flask module """

from flask_restful import Api, Resource

""" Importing Api, Resource from flask_restful module """

app = Flask(__name__) # Constructor name

api = Api(app)

def checker(bmx, edx):
    
    """ A driver function which check the given values satisfies the condition """
    
    if (edx=="add"):
    
        if "x" not in bmx or "y" not in bmx: # Checking if all the required values are given or not
    
            return 301   # Returning 301 Missing Argument 
    
        else:
    
            return 200   # 200 Condition OK

class Add(Resource):
    
    """ Addition Module """
    
    def post(self):
        
        """ Method = POST """
        
        bmx = request.get_json()
        
        key = checker(bmx, "add")
        
        if not key==200: # If key!=200 strike error to User
         
            retjson = {
         
                'Message' : 'You strike an error', # Error Statement
         
                'Status Code' : key # Status Code as Key
         
            }
         
            return jsonify(retjson)  # returning retjson in the form of JSON 
        
        x = bmx["x"]   # Initializing x
        
        y = bmx["y"]   # Initializing y
        
        z = x + y      # Putting value of x and y to z
        
        retjson = {
        
            'Message' : z,   # If all condition satisfies then message required value with key 
        
            'Status Code' : key
        
        }
        
        return jsonify(retjson)

class Subtract(Resource):
    
    """ Subtraction Module """
    
    def post(self):
    
        bmx = request.get_json()
    
        key = checker(bmx, "add")
    
        if not key==200:    # If key!=200 strike error to User
    
            retjson = {
    
                'Message' : 'You strike an error', # Error Statement
         
                'Status Code' : key # Status Code as Key
    
            }
    
            return jsonify(retjson)
    
        x = bmx["x"]   # Initializing x
        
        y = bmx["y"]   # Initializing y

        if x >= y:
    
            z = x-y
    
        else:
            z = y - x
    
        retjson = {
    
            'Message' : z,   # If all condition satisfies then message required value with key 
        
            'Status Code' : key
    
        }
        return jsonify(retjson)

class Multiply(Resource):
    
    ''' Multiplication Module '''

    def post(self):
    
        bmx = request.get_json()
    
        key = checker(bmx, "add")
    
        if not key==200:    # If key!=200 strike error to User
    
            retjson = {
    
                'Message' : 'You strike an error', # Error Statement
         
                'Status Code' : key # Status Code as Key
    
            }
    
            return jsonify(retjson)
    
        x = bmx["x"]
        
        y = bmx["y"]

        z = x*y
    
        retjson = {
    
            'Message' : z,   # If all condition satisfies then message required value with key 
        
            'Status Code' : key
    
        }
        
        return jsonify(retjson)

class Divide(Resource):
    
    ''' Division Module '''

    def post(self):
        
        bmx = request.get_json()
        
        key = checker(bmx, "add")

        if not key==200:    # If key!=200 strike error to User
    
            retjson = {
    
                'Message' : 'You strike an error', # Error Statement
         
                'Status Code' : key # Status Code as Key
    
            }
            return jsonify(retjson)
        
        x = bmx["x"]
        
        y = bmx["y"]
        
        if y==0:
            
            retjson = {
                'Message' : 'ZeroDivisionError',   # If y==0 then throw Zero Division Error
                
                'Status Code' : 304
            }
         
            return jsonify(retjson)
       
        z = x/y

        retjson = {
    
            'Message' : z,   # If all condition satisfies then message required value with key 
        
            'Status Code' : key
    
        }

        return jsonify(retjson)


api.add_resource(Add, "/add")           # Adding Add Resource to Api which is listening on port 5000 with /add  

api.add_resource(Subtract, "/sub")      # Adding Subtract Resource to Api which is listening on port 5000 with /sub

api.add_resource(Multiply, "/mul")      # Adding Multiply Resource to Api which is listening on port 5000 with /mul

api.add_resource(Divide, "/div")        # Adding Divide Resource to Api which is listening on port 5000 with /div

if __name__ == "__main__":
    ''' Main() Function '''
    
    app.run(debug=True)     # run function with active debugging function