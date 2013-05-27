annualInterestRate=0.2
balance=3000

mir=annualInterestRate/12.0
tp=0
for p in range(10,balance,10):
    b=balance
    for m in range(1,13):
        b=b-p
        b=b*(1+mir)
    if b<0:
        break
print('Lowest Payment: '+str(p))
