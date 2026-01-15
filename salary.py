def calculate_net_salary(basic_salary,allowance):
    gross_salary= basic_salary+allowance
    paye=gross_salary*0.10
    nhif=1500
    nssf=1000
    net_salary=gross_salary-(paye+nhif+nssf)
    if net_salary>=80000:
        remark="high income earner"
    elif net_salary>=40000:
     remarks="middle icome earner"
    else:  
     remark="low icome earner"
    return net_salary,remark
#input
basic=float(input("enter basic salary:"))
allowances=float(input("enter allowance:"))
#function call
net,remark=calculate_net_salary(basic ,allowances)
#output
print("net salary:",net)
print("remark:",remark)