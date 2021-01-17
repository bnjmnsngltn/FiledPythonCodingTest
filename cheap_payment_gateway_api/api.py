from flask import Flask
from flask_restful import Api
from cheap_payment_gateway_api.blueprints.payment.resources import CheapPaymentGateway

def run():
    print('Starting Cheap Payment Gateway API')
    app = Flask(__name__)
    api = Api(prefix = '/cheap', app=app)

    # resource for payment
    api.add_resource(CheapPaymentGateway, '/pay')

    print('Success!')
    app.run(port = 6666, debug = True)
