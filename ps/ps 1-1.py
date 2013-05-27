
balance=3329
annualInterestRate=0.2
monthlyPaymentRate =0.04

mir=annualInterestRate/12.0
b=balance
tp=0
for m in range(1,13):
    print ('Month: '+str(m))
    p=b*monthlyPaymentRate
    tp+=p
    print('Minimum monthly payment: '+str(round(p,2)))
    b=b-p
    b=b*(1+mir)
    print('Remaining balance: '+str(round(b,2)))
    
print('Total paid: '+str(round(tp,2)))
print('Remaining balance: '+str(round(b,2)))
