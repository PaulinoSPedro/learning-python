D = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

D['d'] # KeyError, in dictionaries we access keys and not index.

D['d'] = 'spam' # Python creates a new pair of key-value on dict.

# In lists using L[x] is for Indexing and returns an error if x is not in the list
# While in dict is for Accessing key when it exists and create a new pair of key-value when using D[x] = 'y'
# Variable name works like dictionary keys, they must have been assigned before you can reference to it, but they are created when first assigned.