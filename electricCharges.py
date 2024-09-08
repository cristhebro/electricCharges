rate_until_1000 = 7.633
rate_above_1000 = 9.259
for i in range(4):
    hours = float(input("Please enter kilowatt hours used this month to calculate your bill:\n"))
    if hours <= 1000:
        total_bill = hours * rate_until_1000
    else:
        first_1000_hours = 1000
        extra_hours = hours - 1000
        cost_of_first_1000_hours = first_1000_hours * rate_until_1000
        cost_of_extra_hours = extra_hours * rate_above_1000
        total_bill = cost_of_first_1000_hours + cost_of_extra_hours
    bill_in_dollars = total_bill / 100
    print("Your electric bill for this month is: $" + str(bill_in_dollars), "\n")