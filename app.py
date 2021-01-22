import flask
from flask import Flask
from flask import request
from validator import validator
from payment_gateway import payment_gateway


app = Flask(__name__)


@app.route('/', methods=['POST'])
def ProcessPayment():
    try:
        card_number = request.json['CreditCardNumber']
        card_holder = request.json['CardHolder']
        exp = request.json['ExpirationDate']
        amount = request.json['Amount']

        try:
            sec_code = request.json['SecurityCode']
        except:
            sec_code = None
    except:
        return flask.Response(status=400)

    #Check if all deatils enterd is True
    check = validator(card_number, exp, amount, sec_code).validate_all()

    #if every detail enterd is correct process it with gateway
    if check == True:        
        payment_status = payment_gateway(amount).process_payment()
        #if there is error on gateway to process payment  internal error
        if payment_status == False:     
            return flask.Response(status=500)
        else:   #if payment is processed sucessfully
            return flask.Response(status=200)

    else:
        return flask.Response(status=400)   #check/ validation fails there is error in request like wrong card no/ expiray date etc.

    
    
if __name__ =='main':
    app.run(debug=True)


 