from flask import Flask
from flask_restful import Api
from payment_api.blueprints.payment.resources import Payment

def run():
    print('Starting Payment API')
    app = Flask(__name__)
    api = Api(prefix = '/payment', app=app)

    # resource for payment
    api.add_resource(Payment, '/processpayment')

    print('Success!')
    app.run(port = 9999, debug = True)
