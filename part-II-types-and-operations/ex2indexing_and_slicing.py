l = [1,2,3,4]

print(l[4]) # List index out of range

print(l[-1000:1000]) # Python scales out-of-bounds slicing  but not indexing like l[4]

print(l[3:1]) # This doesn't work because Python scales the limits, and always make sure that the lower value will be the lowest possible, so l[3:1] translates into l[3:3] 

l[3:1] = ['?'] # Insertion really on position l[3:3]
print(l[3:1]) # =?
print(l) # [1,2,3,'?',4]