from flask import Flask
from flask_restx import Api, Resource, fields
import RPi.GPIO as GPIO
import pin_controller as pc


app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='RESTful Pi',
          description='A RESTful API to control the GPIO pins of a Raspbery Pi',
          doc='/docs')

ns = api.namespace('triggered', description='Just trigger')

trigger_model = api.model('triggered', {
    'trigger': fields.String(required=True, description='shoots function')
})


class TriggerUtil(object):
    def __init__(self):
        self.counter = 0
        self.triggered = []

    def create(self, data):
        
        if self.triggered['trigger'] == 'on':
            pc.abrir_full()
            self.triggered['trigger'] == 'off'
        return self.triggered


@ns.route('/')  # keep in mind this our ns-namespace (pins/)
class TriggerList(Resource):
    @ns.marshal_list_with(trigger_model)
    def get(self):
        return trigger_util.triggered

    @ns.expect(trigger_model)
    @ns.marshal_with(trigger_model, code=201)
    def post(self):
        return trigger_util.create(api.payload)


@ns.route('/<int:id>')
@ns.response(404, 'pin not found')
@ns.param('trigger', 'on/off')
class Trigger(Resource):

    @ns.expect(trigger_model, validate=True)
    @ns.marshal_with(trigger_model)
    def put(self):
        """Update a pin given its identifier"""
        return trigger_util.update(api.payload)
    
    @ns.expect(trigger_model)
    @ns.marshal_with(trigger_model)
    def patch(self):
        """Partially update a pin given its identifier"""
        return trigger_util.update(api.payload)


GPIO.setmode(GPIO.BCM)

trigger_util = PinUtil()
trigger_util.create({'trigger': 'off'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
