"""
Elephant Carpaccio Excercise 2.0
"""

from __future__ import print_function

stateTaxRates = {
    'UT' : 6.85,
    'NV' : 8.00,
    'TX' : 6.25,
    'AL' : 4.00,
    'CA' : 8.25,
}

discountRates = [
    [50000.00, 15.0],
    [10000.00, 10.0],
    [ 7000.00,  7.0],
    [ 5000.00,  5.0],
    [ 1000.00,  3.0],
    [    0.00,  0.0]
]

def printLine():
    print("--------------------------------")

def printAppInfo():
    printLine()
    print("Elephant Carpaccio Excercise 2.0")
    printLine()

def printOrder(orderSum, taxRate, discountRate):
    taxes = orderSum * taxRate / 100.0
    discount = orderSum * discountRate / 100.0
    totalPayment = orderSum + taxes - discount
    printLine()
    print("Order sum        = %.2f $" %orderSum)
    print("Taxes    (%.2f%%) = %.2f $" % (taxRate, taxes))
    print("Discount (%.2f%%) = %.2f $" % (discountRate, discount))
    print("Total payment    = %.2f $" % (totalPayment))
    printLine()

def inputNumberOfItems():
    numberOfItems = 0
    while numberOfItems < 1:
        numberOfItems = input("Number of items : ")
        numberOfItems = int(float(str(numberOfItems)))
    return numberOfItems

def inputItemPrize():
    itemPrize = 0.00
    while itemPrize <= 0.00:
        itemPrize = input("Item prize [$] : ")
        itemPrize = float(str(itemPrize))
    return itemPrize

def inputState():
    stateFound = False
    while stateFound is False:
        print("State ",end='[')
        for validState in stateTaxRates.keys():
            print(validState,end=',')
        print("\b",end=']')
        state = input(" : ")
        if state in stateTaxRates.keys():
            stateFound = True
        else:
            print(state + ": No such state!")            
    return state

def getTaxRate(state):
    if state in stateTaxRates.keys():
        taxRate = stateTaxRates[state]
    else:
        taxRate = 0.00
    return taxRate

def getDiscountRate(orderSum):
    discountRate = 0.00
    for index in range(len(discountRates)):
        if orderSum > discountRates[index][0]:
            discountRate = discountRates[index][1]
            break
    return discountRate


printAppInfo()

numberOfItems = inputNumberOfItems()
itemPrize = inputItemPrize()
state = inputState()

orderSum = numberOfItems * itemPrize
taxRate = getTaxRate(state)
discountRate = getDiscountRate(orderSum)
printOrder(orderSum, taxRate, discountRate)
