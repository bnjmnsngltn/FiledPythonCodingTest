from flask import Flask
from flask_restful import Api
from bank_api.blueprints.payment.resources import Bank

def run():
    print('Starting Bank API')
    app = Flask(__name__)
    api = Api(prefix = '/bank', app=app)

    # resource for payment
    api.add_resource(Bank, '/pay')

    print('Success!')
    app.run(port = 5555, debug = True)
