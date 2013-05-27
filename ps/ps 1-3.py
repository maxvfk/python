
balance=4800
annualInterestRate=0.2


mir=0.12
lo=balance/15.0
hi=balance*(1+mir)**15/15.0
b=float(balance)
tp=0
while abs(b)>=0.001:
    b=balance
    p=(hi+lo)/2.0
    for m in range(15):
        b=b-p
        b=b*(1+mir)
    if b>0:
        lo=p
    else:
        hi=p
print('Lowest Payment: '+str(round(p/12,2)))
print ('Total payment: ' + str(round(p*12,2)))
