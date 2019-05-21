class Payment():
    def __init__(self, paymentamount):
        self.paymentamount=paymentamount
    
    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        response="Your payment today will be " + str(self.paymentamount)
        return response