from flask_restful import Resource, reqparse
from bank_api.blueprints.payment.controllers import validate_card_number, validate_card_holder, validate_expiration_date, validate_security_code, validate_amount, make_payment

parser = reqparse.RequestParser()
parser.add_argument('credit_card_num', type=str, help='Credit card number field required.', required=True)
parser.add_argument('card_holder', type=str, help='Card holder field required.', required=True)
parser.add_argument('expiration_date', type=str, help='Expiration date field required.', required=True)
parser.add_argument('security_code', type=str, help='Security code.', required=False)
parser.add_argument('amount', type=str, help='Amount field required.', required=True)

class Bank(Resource):
    def post(self):
        args = parser.parse_args()
        
        credit_card_num = args['credit_card_num']
        card_holder = args['card_holder']
        expiration_date = args['expiration_date']
        security_code = args['security_code']
        amount = args['amount']

        details  = {'credit_card_num': credit_card_num,
                    'card_holder': card_holder,
                    'expiration_date': expiration_date,
                    'security_code': security_code,
                    'amount': amount
                    }

        # validate fields
        if not validate_card_number(credit_card_num):
            return {'status': 400, 'message': 'Invalid credit card number.', 'details': details}
        
        if not validate_card_holder(card_holder):
            return {'status': 400, 'message': 'Invalid card holder name.', 'details': details}

        if not validate_expiration_date(expiration_date):
            return {'status': 400, 'message': 'Invalid expiration date. Format must be MM-YYYY (Ex. 01-2021 (January 2021))', 'details': details}

        if not validate_security_code(security_code):
            return {'status': 400, 'message': 'Invalid security code.', 'details': details}

        if not validate_amount(amount):
            return {'status': 400, 'message': 'Invalid amount.', 'details': details}


        res, details = make_payment(details)

        if res:
            return {'status': 200, 'message': 'Payment Successful', 'details': details}
        
        return {'status': 500, 'message': 'Internal server error.', 'details': details}