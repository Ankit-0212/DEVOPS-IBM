
import csv


products =[]
def loadProducts():
    with open('products.csv',newline="") as f:
        csvFile = csv.reader(f)
        for lines in csvFile:
            eachProduct = {
                "productId":lines[0],
                "productName":lines[1],
                "brand":lines[2],
                "price":lines[3],
                "quantity":lines[4]

            }
            products.append(eachProduct)
    print(products)
    return products

def write_products(productList):
    with open('products.csv','w') as f:
        csvCursor =csv.writer(f)
        for product in productList:
            csvCursor.writerows(product)

