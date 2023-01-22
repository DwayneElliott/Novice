def cal():
    print()
    print()
    print('Dwayne Elliott')
    print('01/22/2023')
    print('MAX,MIN,TOTAL,AVERAGE CALCULATOR')
    numlist=list()
    while True:
        inp=input('Enter a number:\n')
        if inp=='done' or inp=='Done':break
        value=float(inp)
        numlist.append(value)
    print('Count List:',len(numlist))
    print('Max Number:',max(numlist))
    print('Min  Number:',min(numlist))
    print('Total:',sum(numlist))
    print('Average:',sum(numlist)/len(numlist))
cal()
