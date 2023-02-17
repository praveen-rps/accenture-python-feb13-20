from flask import Flask
from flask import jsonify
from flask import request
      
app = Flask(__name__) #creating the Flask class object   
     
employee = {"id":"1001","name":"kumar"}



@app.route("/get/employee")
def getEmp():  
    return employee



@app.route("/employee/add", methods=['POST'])
def postEmployee():
	data = {
	'id': request.json['id'],
	'name':request.json['name']
	}
	return data
		

@app.route('/get') #decorator defines the   
def home():  
    return "Get Method is called..." 


@app.route("/customer/<empid>", methods=['POST'])
def test1(empid):
	return "Captured employee id from url is : "+empid


@app.route("/put", methods=['PUT'])
def test2():
	return "Put method is called..."


@app.route("/delete", methods=['DELETE'])
def test3():
	return "Post method is called..."


     
if __name__ =='__main__':  
    app.run(debug = True, port=5001)