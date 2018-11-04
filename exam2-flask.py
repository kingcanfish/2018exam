import requests
from bs4 import BeautifulSoup
from flask import Flask, request, abort, jsonify
import json
from flask import render_template

app = Flask(__name__)



@app.before_request
def app_before_request():
    print("HTTP {}  {}".format(request.method, request.url))


@app.after_request
def app_after_request(response):
    response.headers["From"] = "Ncuhome"
    return response

@app.route("/get", methods=['GET'])
def main():
	url = "https://blog.snowstar.org"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	content1 = soup.find_all("h2")
	content2 = soup.find_all("span")
	content=[]
	num=[1,2,3,4,5,6,7,8,9,10,11]

	for i in content1:
		content.append(i.string)
	dictionary = dict(zip(num,content))
	j = json.dumps(dictionary)
	return j


	
	







if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True,debug=True)
