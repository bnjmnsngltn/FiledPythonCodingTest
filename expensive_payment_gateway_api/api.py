from flask import Flask
from flask_restful import Api
from expensive_payment_gateway_api.blueprints.payment.resources import ExpensivePaymentGateway

def run():
    print('Starting Expensive Payment Gateway API')
    app = Flask(__name__)
    api = Api(prefix = '/expensive', app=app)

    # resource for payment
    api.add_resource(ExpensivePaymentGateway, '/pay')

    print('Success!')
    app.run(port = 7777, debug = True)
