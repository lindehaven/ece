"""
Elephant Carpaccio Excercise 3.0
"""

from ececlass import ececlass

ece = ececlass()
ece.printAppInfo('3.0')
numberOfItems = ece.inputNumberOfItems()
itemPrize = ece.inputItemPrize()
state = ece.inputState()
orderSum = numberOfItems * itemPrize
taxRate = ece.getTaxRate(state)
discountRate = ece.getDiscountRate(orderSum)
(totalPayment, taxes, discount) = ece.calculateOrder(orderSum, taxRate, discountRate)
ece.printOrder(totalPayment, orderSum, taxRate, taxes, discountRate, discount)