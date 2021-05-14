'''
Again a simplified class, this just returns a string of the amount
of payment due.
'''

class Payment():
    def __init__(self, paymentamount):
        self.paymentamount=paymentamount
    
    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        response="Your payment today will be " + str(self.paymentamount)
        return response