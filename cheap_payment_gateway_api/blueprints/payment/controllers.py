import requests
import json

BASE_URL = 'http://127.0.0.1:5555/bank/pay'

headers = {
  'Content-Type': 'application/json'
}


def make_payment(details):
  print(details)
  try:
    resp = requests.request('POST', BASE_URL, headers=headers, data=json.dumps(details))

    return json.loads(resp.text)
  except Exception as e:
    print(e)
    return False
