import math

def invest(target_value,value_today):
    difference = target_value - value_today
    invest_amount = mi + difference
    return invest_amount

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    total=math.ceil(total)
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
mi = int(input("Enter monthly installment amount: "))
no_install = int(input("Enter number of months installed: "))
exp_ret = int(input("Enter the expected growth rate per year in %: "))
value_today=int(input("Enter current portfolio value of your investment: "))

exp_ret=exp_ret/12

target_value = sumofGP(mi, no_install+1, 1+exp_ret/100)
target_value=math.floor(target_value)
invest_amount = invest(target_value,value_today)
invest_amount = math.floor(invest_amount)


def print_value(target_value,value_today,invest_amount,mi):
    difference=value_today-target_value
    if target_value==value_today:
        print("Portfolio value is same as target value so invest",invest_amount)
    elif target_value > value_today:
        print("Portfolio value is less than target value",target_value,"so invest",invest_amount,"which is",mi,"-",difference)
    elif target_value < value_today:
        print("Portfolio value is more than target value",target_value,"so invest",invest_amount,"which is",mi,"-",difference)

print_value(target_value,value_today,invest_amount,mi)


