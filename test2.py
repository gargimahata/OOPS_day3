class bank:
    def transaction(self):
        print("total transaction value.")
    def account_opening(self):
        print("this will show your account open status. ")
    def deposite(self):
        print("this will show your deposited amount")
    def test(self):
        print("test method from bank class")




class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici through hdfc")
    def test(self):
        print("test method from HDFC bank class")

class icici(bank, HDFC_bank):      #Multiple class inheritance
    pass

i = icici()
i.hdfc_to_icici()
i.transaction()
i.deposite()
i.account_opening()
i.test()
