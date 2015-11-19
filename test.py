from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

def getFile(file):
	with open(file) as file_data:
		data=json.load(file_data)
	print data

getFile("/Users/praveengupta/Desktop/Wokstudy/sunburst/solr/AbdomenCT/461570125.json")