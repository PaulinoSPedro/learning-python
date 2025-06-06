# = 65.536
# 2 raised to the power 16
2 ** 16 

# = 0.4, division(2 / 5)
# Python converts result to float-point value 
2 / 5

# = 0.4, division(2 / 5)
# Even with mixed types the result gets converted
2 / 5.0

# = 'spameggs'
# Concatenates both strings because Str has interface to + operator
"spam" + "eggs"

# = 'eggs ham'
# Now the result has an space between the words,
# Also the concatenation occurs between a string and a variable
S = "ham"
"eggs " + S

# = 'hamhamhamhamham'
# Strings have interface for any mathematical operator and
# performs a repetition
S * 5

# = ''
# Strings are iterables and using this you are slicing it
# You are saying give me [from:up to] statement. Empty slice
S[:0]

# = 'green eggs and ham'
# This is string formatting "expressions" form based upon the C language's "printf" available since Python's inception
"green %s and %s" % ("eggs", S)

# = 'green eggs and ham'
# This is string formatting "method calls" the newer technique form added in Python 2.6 and 3.0 derived from C#/.NET
'green {0} and {1}'.format('eggs', S)

# = 'x'
# We are accessing index 0 from the tuple ('x',)
('x',)[0]

# = 'y'
# Accessing index 1 from the tuple, which is y
('x', 'y')[1]

# = [1, 2, 3, 4, 5, 6]
# Concatenating two lists with + 
L = [1,2,3] + [4,5,6]
L, 

# = [1, 2, 3, 4, 5, 6]
# [:] means accessing/slicing the full list
L[:], 

# = []
# Accessing up to but not including the value of index 0.
L[:0], 

# = 5
# Negative index access counting from the right
L[-2], 

# = [5,6]
# Slicing from the right up to 0 when the upper value is not specified
L[-2:]

# = [3, 4]
# First concatenate the lists and then slice them
([1,2,3] + [4,5,6])[2:4]

# = [3,4]
# Creating a list using the index 2 and 3 from list L
[L[2], L[3]]

# = [6, 5, 4, 3, 2, 1]
# Reverse the list in place (Descending)
L.reverse()
L

# = [1, 2, 3, 4, 5, 6] 
# Ascending the list in place
L.sort() 
L

# = 3
# Explicit providing index offset using built-in List methods
L.index(4)

# = 2
# Accessing the value from the key "b" on the dictionary 
{'a':1, 'b':2}['b']

# = 1
# First dictionary is declaredn then key "w" is added to the
# dictionary with value 0, then added value from key "x" and "w"
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
D['x'] + D['w']

# = {'x': 1, 'y': 2, 'z': 3, 'w': 0, (1, 2, 3): 4}
# Add a tuple key(1,2,3) with value 4 
D[(1,2,3)] = 4
D

# = ['x', 'y', 'z', 'w', (1, 2, 3)]
# Get the keys from dictionary and transforms in a list
list(D.keys()),

# = [1, 2, 3, 0, 4]
# Get the values from dictionary and transforms in a list
list(D.values())

# = True
# Uses the in operator to verify if the Key is in the dictionary
(1,2,3) in D

# = [[]]
# Creates an empty sublist on a list
[[]],

# Empty objects
["",[],(),{},None]