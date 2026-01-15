def calculate_commission(sales):
    if sales>=100000:
        commission=sales*0.10
        remarks="excellent sales"
    elif sales>=50000:
        commission=sales*0.07
        remarks="good sales"
    else:
          commission=sales*0.05
          remark="needs improvement"
          return commission,remark
    #input 
    sales_amount=float(input("enter sales amount(kes):"))
    #function call
    commission,remark
    calculate_commission(sales_amount)
    #output
    print("commission:",commission)
    print("remark:",remark)