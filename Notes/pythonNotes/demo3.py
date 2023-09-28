products = [{
    'productId': 1,
    'productName': 'Iphone14',
    'price': 75634
},
{
    'productId': 2,
    'productName': 'Oneplus11',
    'price': 60000
},
{
    'productId': 1,
    'productName': 'samsungFlip',
    'price': 150000
}

]

from functools import reduce

# print(reduce(lambda p1,p2: (p1+p2)/len(list(map(lambda p:p['price'],filter(lambda product : product['price']>=70000,products))))
#              ,map(lambda p:p['price'],filter(lambda product : product['price']>=70000,products))))


prices  = list(map(lambda p:p['price'],filter(lambda product : product['price']>=70000,products)))

# prices.sort(reverse=True)

finalList = sorted(list(map(lambda p:p['price'],filter(lambda product : product['price']>=70000,products))),reverse=True)
print(finalList)

