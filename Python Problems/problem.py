n = []
num = int(input('Enter the limit you want :'))
for a in range(0, num):
    element = int(input('Enter the numbers :'))
    n.append(element)
print(n)

d = []
num = int(input('Enter the limit you want :'))
for b in range(0, num):
    element = int(input('Enter the numbers :'))
    d.append(element)
print(d)

new = []
Dict = dict()
for i in d:
    for j in n:
        quotient = j//i
        remainder = j % i
        print(j, 'divided by', i, remainder, '-->', quotient)
        if quotient == remainder:
            new.append(j)
            print(new)
            for k in new:
                Dict[i] = [k]
            print(Dict)