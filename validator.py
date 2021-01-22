from datetime import datetime


class validator():

    def __init__(self, card, date, amount, security_code=None):
        self.card = card
        self.date = date
        self.amount = amount
        self.security_code = security_code

        '''
        card_validator =  TO VALIDATE CARD NUMBER
        exp_date_Validator = TO VALIDATE EXPIRAY DATE (it cannot be in the past)
        security_validator = TO VALIDATE SECURITY CODE (must be 3 digits)
        amount _validator = TO VALIDATE AMOUNT (decimal, positive amount)
        # All the print statements to only check where it fails or what causes return status like 400 (eg wrong card no / secrity code etc)
        '''

            
    #for the validation of the card no "luhn algorithms is used"
    def card_validator(self):

        card_number = list(self.card.strip())
        # Remove the last digit from the card number
        check_digit = card_number.pop()

        # Reverse the order of the remaining numbers
        card_number.reverse()

        processed_digits = []

        for index, digit in enumerate(card_number):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2

                # Subtract 9 from any results that are greater than 9		
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9

                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))

        total = int(check_digit) + sum(processed_digits)

        # Verify that the sum of the digits is divisible by 10
        #returns true if valid and if card is invalid returns false
        if total % 10 == 0:
            return True
        else:
            print('Issue in Card NO')
            return False



    # accept date in format month/year  (standard expirary date format for cards)
    def exp_data_validator(self):
        date_now = datetime.now()
        current_year = date_now.strftime('%y')
        current_month = date_now.strftime('%m')
        
        exp_date = self.date.split('/')
        if exp_date[1] > current_year:
            return True
        elif exp_date[1] == current_year:
            if exp_date[0] < current_month:
                return True
            else:
                print('Issue in Expiray Date')
                return False
        

    #optional parameter to check lenght of security code must be 3
    #if security_code is none means no code is passed as it is optional parameter
    def security_validator(self):
        if self.security_code == None:
            return True
        elif len(self.security_code) == 3:
            return True
        else:
            print('Issue in Security code')
            return False

    #checks if amount is posetive and in decimal format
    def amount_validator(self):
        if float(self.amount) > 0:
            return True
        else:
            print('Issue in Amount')
            return False

    #validate all the things
    def validate_all(self):
        c = self.card_validator() 
        e= self.exp_data_validator()
        a=self.amount_validator() 
        s=self.security_validator()
        if c and e and a and s == True:
            return True
        return False







