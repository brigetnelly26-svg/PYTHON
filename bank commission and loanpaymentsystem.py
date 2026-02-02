def get_customer_details():
    return get_customer_details
    customername=string(input("enter customername"))
    transaction_amount=float(input("enter transaction_amount"))
    loanamount=float(input("enter loanamount"))
    loanperiod=int(input("enter loanperiod(in years)"))
    def calculate_commission(transaction_amount):
        if transaction_amount<10000:
            commission=transaction_amount*0.02
        elif transaction_amount<=50000 & transaction_amount>10000:
            commission=transaction_amount*0.03
        else:
            commission=transaction_amount*0.05
            def calculate_monthly_repayment(loanamount,years):
                return(loanamount*10//loanperiod*12)
            print("customername"+customername)
            print("transaction_amount"+transaction+amount)
            print("loanamount"+loanamount)
            print("loanperiod"+loanperiod)
