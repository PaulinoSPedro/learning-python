s = 'apple'
l = [1,2,3]
t = ('im','a','tuple')
d = {1: 'a', 2: 'b', 3: 'c'}
# The + operator doesn't work for mixed types.
s + l # TypeError
l + t # TypeError
l + d # TypeError

# Append only works with List Type
# Append assume its subject is mutable, and strings are immutable objects
s.append('m') 
l.append('4')

# Keys method resides only with Dictionary
l.keys()

# Slicing and concatenation always returns the same type object as the object processed.  
