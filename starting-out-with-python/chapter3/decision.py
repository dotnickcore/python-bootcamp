# Expression    Meaning
# x > y         Is x greater than y?
# x < y         Is x less than y?
# x >= y        Is x greater than or equal to y?
# x <= y        Is x less than or equal to y?
# x == y        Is x equal to y?
# x != y        Is x not equal to y?

BONUS = 500.00
COMMISSION_RATE = 0.12

sales = float(input("Enter the sales: "))

if sales > 50000:
    commission_calculate = sales * COMMISSION_RATE + BONUS
    print("You met your sales quota!")
    print("Sales including Bonus: $" + format(commission_calculate, '.2f'))
else:
    commission_calculate = sales * COMMISSION_RATE
    print("Sales: $" + format(commission_calculate, '.2f'))