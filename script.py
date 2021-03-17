import math

def invest(target_value,value_today):
    difference = target_value - value_today
    invest_amount = mi + difference
    return invest_amount

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    target_value = total-a
    return target_value

print("""


 /$$    /$$          /$$                            /$$$$$$                                                   /$$                          
| $$   | $$         | $$                           /$$__  $$                                                 |__/                          
| $$   | $$ /$$$$$$ | $$ /$$   /$$  /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$  /$$ /$$$$$$$   /$$$$$$       
|  $$ / $$/|____  $$| $$| $$  | $$ /$$__  $$      | $$$$$$$$|  $$  /$$//$$__  $$ /$$__  $$|____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$      
 \  $$ $$/  /$$$$$$$| $$| $$  | $$| $$$$$$$$      | $$__  $$ \  $$/$$/| $$$$$$$$| $$  \__/ /$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  \ $$      
  \  $$$/  /$$__  $$| $$| $$  | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$      
   \  $/  |  $$$$$$$| $$|  $$$$$$/|  $$$$$$$      | $$  | $$   \  $/  |  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$      
    \_/    \_______/|__/ \______/  \_______/      |__/  |__/    \_/    \_______/|__/      \_______/ \____  $$|__/|__/  |__/ \____  $$      
                                                                                                    /$$  \ $$               /$$  \ $$      
                                                                                                   |  $$$$$$/              |  $$$$$$/      
                                                                                                    \______/                \______/       
 /$$$$$$                                           /$$     /$$                                                                             
|_  $$_/                                          | $$    |__/                                                                             
  | $$   /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$   /$$ /$$$$$$$   /$$$$$$                                                          
  | $$  | $$__  $$|  $$  /$$//$$__  $$ /$$_____/|_  $$_/  | $$| $$__  $$ /$$__  $$                                                         
  | $$  | $$  \ $$ \  $$/$$/| $$$$$$$$|  $$$$$$   | $$    | $$| $$  \ $$| $$  \ $$                                                         
  | $$  | $$  | $$  \  $$$/ | $$_____/ \____  $$  | $$ /$$| $$| $$  | $$| $$  | $$                                                         
 /$$$$$$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$                                                         
|______/|__/  |__/    \_/    \_______/|_______/    \___/  |__/|__/  |__/ \____  $$                                                         
                                                                         /$$  \ $$                                                         
                                                                        |  $$$$$$/                                                         
                                                                         \______/                                                          
  /$$$$$$            /$$                     /$$             /$$                                                                           
 /$$__  $$          | $$                    | $$            | $$                                                                           
| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$                                                    
| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$                                                   
| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/                                                   
| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$                                                         
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$                                                         
 \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/   \______/ |__/                                                         
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           


 """)
mi = int(input("Enter monthly amount of your investment: "))
no_install = int(input("Enter the total number of installments: "))
exp_ret = int(input("Enter the expected growth rate for a year: "))
value_today=int(input("Enter current value of your investment: "))

exp_ret=exp_ret/12

target_value = sumofGP(mi, no_install+1, 1+exp_ret/100)
target_value=math.ceil(target_value)
invest_amount =invest(target_value,value_today)
invest_amount = math.ceil(invest_amount)


def print_value(target_value,value_today,invest_amount):
    if target_value==value_today:
        print("Portfolio value is same as target value so invest ",invest_amount)
    elif target_value > value_today:
        print("Portfolio value is less than target value ",target_value," so invest",invest_amount)
    elif target_value < value_today:
        print("Portfolio value is more than target value ",target_value," so invest",invest_amount)

print_value(target_value,value_today,invest_amount)


