from flask_restful import Resource, reqparse
from cheap_payment_gateway_api.blueprints.payment.controllers import make_payment

parser = reqparse.RequestParser()
parser.add_argument('credit_card_num', type=str, help='Credit card number field required.', required=True)
parser.add_argument('card_holder', type=str, help='Card holder field required.', required=True)
parser.add_argument('expiration_date', type=str, help='Expiration date field required.', required=True)
parser.add_argument('security_code', type=str, help='Security code.', required=False)
parser.add_argument('amount', type=str, help='Amount field required.', required=True)

class CheapPaymentGateway(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        resp = make_payment(args)
        
        if resp == False:
            return {'status': 404, 'gateway': 'CheapPaymentGateway', 'message': 'Cannot reach bank API', 'details': args}

        status = resp['status']
        details = resp['details']
        message = resp['message']

        return {'status': status, 'gateway': 'CheapPaymentGateway', 'message':message, 'details':details}
