import requests
import json

url = 'http://127.0.0.1:9999/payment/processpayment'
headers = {
  'Content-Type': 'application/json'
}

while True:

    cc = input('Credit Card Number >>> ')
    ch = input('Card Holder >>> ')
    exp_date = input('Expiration Date (MM-YYYY) >>>> ')
    sc = input('Security Code (press enter to skip) >>> ')

    if len(sc) == 0:
        sc = None

    amount = input('Amount in £ >>>')

    payload = {
        'credit_card_num': cc,
        "card_holder": ch,
        'expiration_date': exp_date,
        'security_code': sc,
        'amount': amount
    }

    resp = requests.request('POST', url, headers=headers, data=json.dumps(payload))
    print(resp.text)


