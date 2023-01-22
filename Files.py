fname=input('Enter the file name: ')
fhand=open(fname)
inp=fhand.read()
print('Line Count:'.upper(),len(inp))
print('File Text:'.upper())
print(inp)


