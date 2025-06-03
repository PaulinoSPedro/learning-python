L = [1, 2]
L.append(L)

'''
Since it's  referencing itself the list its now a infinite cycle of itself at index 2

'''

print(L)
print(L[2])
print(L[2][2])
print(L[2][2][2])
print(L[2][2][2][2])
