import random

class payment_gateway():
    def __init__(self,amount):
        self.amount = float(amount)
        self.tries = 0
        
        '''
        Process_payment() return status of payment after processing with gateway according to amount
        Print statements  are just to check where the issue is happening or due to which gateway status is returned
        All 3 gateways works on random process logic "It pretends to be a actual gateway"
            # it randomly genrate the no 0 or 1 and divide by it
            # if it is zero rases execption which act as a transaction failure
            # if no is 1 return True payment success
            # "All 3 gateways works on same logic"
        '''


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
            
            r_no = random.randint(0,1)
            flag = 4/r_no
            return True

        except:
            print('CheapGateway Issue')
            return False              #returns 500 internal error as payment is not processed


    def expensive_gateway(self):
        try:
            #process the payment 
            #actual payment processing with gateway
            r_no = random.randint(0,1)
            flag = 4/r_no
            return True
        except:
            print('Issue in Expensive gateway Trying CheapGateway')
            #if any error in payment processing retry with cheap gateway
            return self.cheap_gateway()


    
    def premium_gateway(self):
        if self.tries < 3:
            try:
                #process the payment 
                #actual payment processing with gateway
                #returns true if payment process successfully
                self.tries += 1
                r_no = random.randint(0,1)
                flag = 4/r_no
                return True

            except:
                print('Retrying PremiumGateway', self.tries)
                self.premium_gateway()
                
        else:
            print('Issue in PremiumGateway')
            return False                      #returns 500 internal error as payment is not processed

