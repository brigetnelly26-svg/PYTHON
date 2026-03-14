def get_customer_details():
    name = input("Enter Customer Name: ")
    
    while True:
        transaction = float(input("Enter Transaction Amount: "))
        if transaction > 0:
            break
        print("Enter a positive number.")
    
    while True:
        loan = float(input("Enter Loan Amount: "))
        if loan > 0:
            break
        print("Enter a positive number.")
    
    while True:
        years = int(input("Enter Loan Period (in years): "))
        if years > 0:
            break
        print("Enter a positive number.")
    
    return name, transaction, loan, years


def calculate_commission(transaction):
    if transaction < 10000:
        return transaction * 0.02
    elif transaction <= 50000:
        return transaction * 0.03
    else:
        return transaction * 0.05


def calculate_monthly_repayment(loan, years):
    total_with_interest = loan + (loan * 0.10)
    monthly = total_with_interest / (years * 12)
    return monthly


name, transaction, loan, years = get_customer_details()

commission = calculate_commission(transaction)
monthly_payment = calculate_monthly_repayment(loan, years)

print("\n--- Customer Financial Summary ---")
print("Customer Name:", name)
print("Transaction Amount:", transaction)
print("Bank Commission:", commission)
print("Loan Amount:", loan)
print("Loan Period (Years):", years)
print("Monthly Loan Repayment:", monthly_payment)

