Good day, this is my solution to the given coding exercise.

Before starting: 
    *Install the necessary dependencies first through pip
        pip install -r requirements.txt

1. I divided the problem into 5 different API, namely:
    *payment_api: the main api
    *cheap_payment_gateway_api: simulates a gateway
    *expensive_payment_gateway api: simulates a gateway
    *premium_payment_gateway_api: simulates a gateway
    *bank_api: simulates an actual bank by "confirming" a payment through logging the transaction in a csv file


2. To test the solution:
    *Run the api's individually first:
        python run_bank.py
        python run_cheap.py
        python run_exp.py
        python run_premium.py
        python run_payment.py

        **You can also choose to stop an API from running to simulate a situation in which a payment gateway or the bank is down

    *Enter the details of the transaction with the python terminal
        *Just press enter directly if you want to skip the Security Code field

        **For now, only the payment_api and bank_api checks if the given credentials are valid
        **The gateway api are just there as a buffer to pass the data around, they don't if data or valid or not

    *Witness the response of the payment_api

    ****API can also be tested through POSTMAN (https://www.postman.com/)
        *I exported the postman requests inside the postman folder 
        *In my experience, the developers here in my country often use POSTMAN to test their API's

3. Here's is how the transaction is being passed between the api's

    User -> payment_api -> gateway_api -> bank_api -> gateway_api -> payment_api -> User

4. If you have any questions regarding this solution, please let me know. Have a great day!