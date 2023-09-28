DIGITMAP ={
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

def convert(str):
    try:
        number = ''
        for token in str:
            number+=DIGITMAP[token]
        x = int(number)
        print(f"converted values x = {x}")
    except(KeyError,TypeError):
        print("Conversion failed!!")
        x=-1
    return x

print(convert("one two three".split(' ')))
