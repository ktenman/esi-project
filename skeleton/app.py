from datetime import datetime
from flask import Flask, request
from suds.client import Client

app = Flask("__name__")
# client = Client('link to your wsdl file', cache=None)
client = Client('http://757e-193-40-12-11.ngrok.io/?wsdl', cache=None) # TODO add error handling

@app.route('/', methods=['GET'])
def index():
    args = request.args
    return str(client.service.ping(args.get("domain"), int(args.get("times"))))

@app.route('/showip')
def showip():
    args = request.args
    return str(client.service.domain_ip(args.get("domain")))

@app.route('/dns')
def dns():
    args = request.args
    return str(client.service.name_servers(args.get("domain")))


if __name__ == "__main__":
    app.run(debug=True)
