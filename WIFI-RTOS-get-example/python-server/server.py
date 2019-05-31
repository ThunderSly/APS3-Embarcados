from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class RTC(Resource):
    def get(self):
        idRTC = request.args.get("id")
        hour = request.args.get("hour")
        minute = request.args.get("minute")
        second = request.args.get("second")
        return {'id': idRTC}

class But(Resource):
    def get(self):
        idBut = request.args.get("id")
        return {idBut: "Pressed the Button"}

class AFEC(Resource):
    def get(self):
        idAFEC = request.args.get("id")
        temp =  request.args.get("value")
        return {idAFEC : temp}

api.add_resource(HelloWorld, '/')
api.add_resource(RTC, '/RTC')
api.add_resource(AFEC, '/AFEC')
api.add_resource(But, '/BUT')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)

