from datetime import datetime

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


def make_payment(details):
    # assuming valid credentials based on the ordering of things, proceed with payment
    # simulate payment by writing to a csv file

    with open('bank_api/transactions.csv') as infile:
        transactions = infile.read().split('\n')
        
        if len(transactions) > 1:
            last_id = int(transactions[-1].split(',')[0])

            id = last_id + 1

        else:
            id = 0

    try:
        with open('bank_api/transactions.csv', 'a') as outfile:
            transaction = f"{id},{details['credit_card_num']},{details['card_holder']},{details['expiration_date']},{details['security_code']},{details['amount']}"
            outfile.write('\n'+transaction)

            details['id'] = id

    except Exception as e:
        # For any error that might occur, count it as internal server error
        print(e)
        return False, details

    else:
        return True, details
