with open('data.txt','r') as f:
    data = f.readlines()

print(data)
print("Number : "+data[0])
data[1]='14\n'
with open('data.txt','w') as file:
    file.writelines(data)

print(data)