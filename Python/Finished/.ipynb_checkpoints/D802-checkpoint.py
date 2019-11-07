'''Bubble sort(D802)
Bubble Sort sorts an array by repeatly comparing adjacent elements, and swap them if required. 
Implement the Bubble Sort sorting algorithm. Sort the given array in the specified order.
A is the sorting order required (0 = Ascending, 1 = Descending)
'''
temp = input()
n = input()

temp = temp.split(' ')
n = n.split(' ')
n = [int(x) for x in n]

order = temp[1]

'''
if order == 0:
    print('<')
else:
    print('>')
'''
def bubble(ar,order):
    count = 0
    yeet = ''
    if order == '0':
        for k in range(len(ar)):
            for i in range(len(ar)-1):
                if ar[i] > ar[i+1]:
                    ar[i], ar[i+1] = ar[i+1], ar[i]
                    count += 1
    elif order == '1':
        for k in range(len(ar)):
            for i in range(len(ar)-1):
                if ar[i] < ar[i+1]:
                    ar[i], ar[i+1] = ar[i+1], ar[i]
                    count += 1
    for a in ar:
        yeet += str(a)
        yeet += ' '
    return(str(count)+'\n'+yeet)
# print('n: {}'.format(n))
result = bubble(n,order)
# print(count)
print(result)

'''
6 0
4 4 5 5 5 3
'''
