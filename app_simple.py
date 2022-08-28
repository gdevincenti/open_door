from flask import Flask
from flask_restx import Api, Resource, fields
import pin_controller as pc
app = Flask(__name__)
api = Api(app)
class Helloworld(Resource):
    def __init__(self):
        pass
    def get(self):
        pc.abrir_full()
        return {
			"OK":"OK"
		}
    def create(self):
        pc.abrir_full()
        return {
			"OK":"OK"
		}
api.add_resource(Helloworld, '/')
if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)