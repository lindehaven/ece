"""
Elephant Carpaccio Excercise
"""

class ececlass:

    def __init__(self):
        self.stateTaxRates = {
            'UT' : 6.85,
            'NV' : 8.00,
            'TX' : 6.25,
            'AL' : 4.00,
            'CA' : 8.25,
        }
        self.discountRates = [
            [50000.00, 15.0],
            [10000.00, 10.0],
            [ 7000.00,  7.0],
            [ 5000.00,  5.0],
            [ 1000.00,  3.0],
            [    0.00,  0.0]
        ]

    def printLine(self):
        print("--------------------------------")

    def printAppInfo(self, version=''):
        self.printLine()
        print("Elephant Carpaccio Excercise %s" %str(version))
        self.printLine()

    def calculateOrder(self, orderSum, taxRate, discountRate):
        taxes = orderSum * taxRate / 100.0
        discount = orderSum * discountRate / 100.0
        totalPayment = orderSum + taxes - discount
        return (totalPayment, taxes, discount)

    def printOrder(self, totalPayment, orderSum, taxRate, taxes, discountRate, discount):
        self.printLine()
        print("Order sum        = %.2f $"  % (orderSum))
        print("Taxes    (%.2f%%) = %.2f $" % (taxRate, taxes))
        print("Discount (%.2f%%) = %.2f $" % (discountRate, discount))
        print("Total payment    = %.2f $"  % (totalPayment))
        self.printLine()

    def inputNumberOfItems(self):
        numberOfItems = 0
        while numberOfItems < 1:
            numberOfItems = input("Number of items : ")
            numberOfItems = int(float(str(numberOfItems)))
        return numberOfItems

    def inputItemPrize(self):
        itemPrize = 0.00
        while itemPrize <= 0.00:
            itemPrize = input("Item prize [$] : ")
            itemPrize = float(str(itemPrize))
        return itemPrize

    def inputState(self):
        stateFound = False
        while stateFound is False:
            print("State ",end='[')
            for validState in self.stateTaxRates.keys():
                print(validState,end=',')
            print("\b",end=']')
            state = input(" : ")
            if state in self.stateTaxRates.keys():
                stateFound = True
            else:
                print(state + ": No such state!")            
        return state

    def getTaxRate(self, state):
        if state in self.stateTaxRates.keys():
            taxRate = self.stateTaxRates[state]
        else:
            taxRate = 0.00
        return taxRate

    def getDiscountRate(self, orderSum):
        discountRate = 0.00
        for index in range(len(self.discountRates)):
            if orderSum > self.discountRates[index][0]:
                discountRate = self.discountRates[index][1]
                break
        return discountRate
