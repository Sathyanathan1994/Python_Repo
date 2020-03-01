n = [int(x) for x in input('Enter the values :')]

d = [int(y) for y in input('Enter the values :')]

l = []
for i in d:
    for j in n:
        quotient = j//i
        remainder = j%i
        print(j, 'divided by', i, remainder, '-->', quotient)
        if quotient == remainder:
            l.append(j)
            # print(l)
            Dict = {i:[j] for d in l}
            print(Dict)