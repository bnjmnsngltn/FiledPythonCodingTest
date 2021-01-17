from datetime import datetime
import json
import requests

gateway_url = {
    'cheap' : 'http://127.0.0.1:6666/cheap/pay',
    'expensive' : 'http://127.0.0.1:7777/expensive/pay',
    'premium' : 'http://127.0.0.1:8888/premium/pay'
}

headers = {
  'Content-Type': 'application/json'
}

def validate_card_number(credit_card_num: str):
    # validate card using Luhn's algorithm
    credit_card_num = str(credit_card_num)

    double = 0
    total = 0

    try:
        for i in range(len(credit_card_num) - 1, -1, -1):
            for c in str((double + 1) * int(credit_card_num[i])):
                total += int(c)
            double = (double + 1) % 2

    except ValueError:
        return False

    return (total % 10) == 0

def validate_card_holder(card_holder: str):
    return isinstance(card_holder, str)

def validate_expiration_date(expiration_date: str):
    # expiration date format is MM/YY
    # example 01/21 is January 2021

    try:
        exp_year = int(expiration_date.split('-')[1])
        exp_month = int(expiration_date.split('-')[0])

    except IndexError:
        return False

    if exp_year < 1000: # year must be 4 digits
        return False
    
    if not 1 <= exp_month <= 12: # month be between 1-12 only
        return False

    # get date now
    dt = datetime.now()
    now_year = dt.year
    now_month = dt.month

    if exp_year >= now_year:
        if exp_month >= now_month:
            return True
        return False
    else:
        return False

def validate_security_code(security_code: str):
    if security_code is not None:
        try:
            int(security_code) # check if security_code is numeric in nature

        except ValueError:
            return False

        else:
            if len(security_code) == 3: # security code must be exactly 3 digits in length
                return True

            return False
    return True

def validate_amount(amount: str):
    try:
        amount = float(amount)
    
    except ValueError:
        return False
    
    else:
        if amount > 0: # amount must be positive always 
            return True
        
        return False

def request_gateway(gateway='cheap', payload: dict = {}):
    try:
        resp = requests.request('POST', gateway_url[gateway], headers=headers, data=json.dumps(payload))

        return json.loads(resp.text)

    except Exception as e:
        return False
    

def make_payment(details):
    # assuming valid credentials based on the ordering of things, proceed with payment
    # simulate payment by writing to a csv file

    amount = float(details['amount'])

    if amount <= 20:
        # cheap payment, try only once
        print('Trying Cheap Gateway...')
        resp = request_gateway('cheap', details)

    elif 20 < amount <= 50:
        # expensive payment, if fail, try cheap once
        print('Trying Expensive Gateway...')
        resp = request_gateway('expensive', details)

        if resp == False:
            print('Expensive Gateway Failed. Trying Cheap Gateway...')
            resp = request_gateway('cheap', details)

    elif amount > 50:
        # premium, if fail, retry three times
        trial = 0

        while trial < 3:
            print(f'Trying Premium Gateway. Trial {trial+1} of 3.')
            resp = request_gateway('premium', details)

            if resp == False:
                break

            trial = trial + 1

    return resp

