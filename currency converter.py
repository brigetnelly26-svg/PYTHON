# exchange rates
# 1 usd=150 kes
# 1eur =165 kes
kes_to_usd=lambda kes:kes/150
usd_to_kes=lambda usd:usd*150
kes_to_eur=lambda kes:kes/165
eur_to_kes=lambda eur: eur*165
print("===CURRENCY CONVERTER===")
print("1. kes_to_usd")
print("2.usd_to_kes")
print("3. kes_to_eur")
print("4.eur_to_kes")
choice=int(input("choose an option (1_4)"))
amount=float(input("enter amount:"))
if choice==1:
    print ("amount in usd:",round(kes_to_usd(amount),2))
elif choice==2:
    print ("amount in kes:",round(usd_to_kes(amount), 2))
elif choice==3:
    print("amount in eur:",round(eur_to_kes(amount), 2))
elif choice==4:
    print("amount in kes:",round(kes_to_eur(amount), 2))
else:
    print("invalid choice")