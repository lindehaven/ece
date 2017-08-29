print("----------------------------")
print("Elephant Carpaccio Excercise")
print("----------------------------")

numberOfItems = input("Number of items : ")
itemPrize = input("Item prize [$] : ")
state = input("State [UT/NV/TX/AL/CA] : ")

if state in ['UT']:
    taxRate = 6.85
elif state in ['NV']:
    taxRate = 8.00
elif state in ['TX']:
    taxRate = 6.25
elif state in ['AL']:
    taxRate = 4.00
elif state in ['CA']:
    taxRate = 8.25
else:
    taxRate = 0.00
    print(state + ": No such state!")
    exit

orderSum = int(float(numberOfItems)) * float(itemPrize)

if orderSum > 50000.0:
    discountRate = 15.0
elif orderSum > 10000.0:
    discountRate = 10.0
elif orderSum > 7000.0:
    discountRate = 7.00
elif orderSum > 5000.0:
    discountRate = 5.00
elif orderSum > 1000.0:
    discountRate = 3.00
else:
    discountRate = 0.00

taxes = orderSum * taxRate / 100.0
discount = orderSum * discountRate / 100.0
totalPayment = orderSum + taxes - discount

print("----------------------------")
print("Order sum        = $%.2f" %orderSum)
print("Taxes    (%.2f%%) = $%.2f " % (taxRate, taxes))
print("Discount (%.2f%%) = $%.2f" % (discountRate, discount))
print("Total payment    = $%.2f" % (totalPayment))


