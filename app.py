from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

dataBase = mysql.connector.connect(host = 'boidata1.chhi9kfzkjf7.ap-northeast-1.rds.amazonaws.com', user = 'admin', passwd = 'rootroot', database = 'boidatainitial')
headings=('timestamp', '_id', '_index', 'type', 'appid', 'data_center', 'env',
       'filename', 'hf04', 'hostname', 'hrest', 'logtype', 'message', 'target',
       'logclass', 'Ticket_ID')



@app.route('/')
def index():
    return render_template('table1.html')

@app.route('/predict', methods = ["POST"])
def predict():
	if request.method == 'POST':
		cursorObject = dataBase.cursor()
		query = "SELECT * FROM boidatainitial.TICKET_GEN_BOI7"
		cursorObject.execute(query)
		myresult = cursorObject.fetchall()
		for x in myresult:
			print(x)

		return jsonify({'Result': myresult})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port =8080)