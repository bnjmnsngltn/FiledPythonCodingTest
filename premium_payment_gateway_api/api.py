from flask import Flask
from flask_restful import Api
from premium_payment_gateway_api.blueprints.payment.resources import PremiumPaymentGateway

def run():
    print('Starting Cheap Payment Gateway API')
    app = Flask(__name__)
    api = Api(prefix = '/premium', app=app)

    # resource for payment
    api.add_resource(PremiumPaymentGateway, '/pay')

    print('Success!')
    app.run(port = 8888, debug = True)
