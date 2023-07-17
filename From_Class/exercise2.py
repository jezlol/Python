hw = int(input("Enter the number of hours worked: " ))
pr = int(input("Enter the hourly pay rate: " ))

if hw > 40:
    ot = hw - 40
    total_pay = (40 * pr) + (ot * pr * 1.5)
else:
    total_pay(hw * pr)

print("The gross pay is: ", total_pay)