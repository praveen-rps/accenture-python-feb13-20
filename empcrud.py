from flask import Flask
from flask import jsonify
from flask import request

app= Flask(__name__)

empdata=[
	{ 'id':'1001',
		'name':'praveen',
		'desg':'Developer'
	},
	{ 'id':'1002',
		'name':'kumar',
		'desg':'Manager'
	}
]

@app.route("/employee/all",methods=['GET'])
def getAll():
		return jsonify({'emps':empdata})



@app.route("/employee/add",methods=['POST'])
def addEmployee():
	dat = {
				'id': request.json['id'],
				'name':request.json['name'],
				'desg':request.json['desg']
			 }
	empdata.append(dat)
	return jsonify({'response':"success"})



@app.route("/employee/search/<id>", methods=['GET'])
def getEmployeeById(id):
	temp = [emp for emp in empdata if emp['id']==id]
	return jsonify({'emps':temp})



@app.route("/employee/delete/<id>",methods=['DELETE'])
def deleteEmployeeById(id):
	e = [emp for emp in empdata if emp['id']==id ]
	if len(e) ==0:
		return jsonify({'response':"data not found with given id"})
	else:
		empdata.remove(e[0])
		return jsonify({'response':"data deleted..."})



if __name__=='__main__':
	app.run(port=5002)