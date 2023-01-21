print('Find Smallest and Largest Value')
print('Author: Dwayne Elliott')
print('Date: 01/21/2023')
print()
def Smallest():
    smallest=None
    count=0
    print('FIND SMALLEST VALUE')
    for value in [5,2,3,5,4,5,2,3,5]:
        if smallest is None:
            smallest=value
        elif value < smallest:
            smallest = value
        count=count+1
        print('Count:',count,'Value:',value,)
    print('Smallest Value:',smallest)
def Largest():
    largest=None
    count=0
    print('FIND LARGEST VALUE')
    for value in [5,2,3,5,4,5,2,3,5]:
        if largest is None:
            largest=value
        elif value > largest:
            largest = value
        count=count+1
        print('Count:',count,'Value:',value,)
    print('Largest Value:',largest)
Smallest()
Largest()
