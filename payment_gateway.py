import random

class payment_gateway():
    def __init__(self,amount):
        self.amount = float(amount)
        self.tries = 0


    def process_payment(self):
        #cheap payment gateway
        if self.amount < 20:
            status = self.cheap_gateway()
        
        #Expensive payment gateway
        if self.amount >=21 and self.amount <500:
            status = self.expensive_gateway()

        # PRemium Payment Gateway
        if self.amount > 500:
            status = self.premium_gateway()
 
        return status



    def cheap_gateway(self):
        try:
            #process the payment 
            #actual payment processing with gateway
            # it randomly genrate the no 0 or 1 and divide by it
            # if it is zero rases execption which act as a transaction failure
            # if no is 1 return True payment success
            r_no = random.randint(0,1)
            flag = 4/r_no
            return True

        except:
            return False              #returns 500 internal error as payment is not processed


    def expensive_gateway(self):
        try:
            #process the payment 
            #actual payment processing with gateway
            r_no = random.randint(0,1)
            flag = 4/r_no
            return True
        except:
            #if any error in payment processing retry with cheap gateway
            return self.cheap_gateway()


    
    def premium_gateway(self):
        if tries < 3:
            try:
                #process the payment 
                #actual payment processing with gateway
                #returns true if payment process successfully
                tries += 1
                r_no = random.randint(0,1)
                flag = 4/r_no
                return True

            except:
                self.premium_gateway()
                
        else:
            return False                      #returns 500 internal error as payment is not processed

