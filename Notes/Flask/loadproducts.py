import json

def laod_products():
    with open('products.json') as f:
        return json.load(f)


def write_products(products):
    with open('products.json','w') as f:
        json_object = json.dumps(products)
        f.write(json_object)