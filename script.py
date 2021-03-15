import math

def invest(target_value,value_today):
    difference = target_value - value_today
    invest_amount = mi + difference
    return invest_amount

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    target_value = total-a
    return target_value

mi = int(input("Enter monthly amount of your investment: "))
no_install = int(input(" Enter the total number of installments: "))
exp_ret = int(input(" Enter the expected growth rate for a year: "))
value_today=int(input("Enter current value of your investment: "))

exp_ret=exp_ret/12

target_value = sumofGP(mi, no_install+1, 1+exp_ret/100)
print("\nThe target value = " , int(target_value))

invest_amount=invest(target_value,value_today)

print("You need to invest: ",int(invest_amount))