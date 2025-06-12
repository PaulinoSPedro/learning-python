D = {}
print(D)

# Since dictionaries doesn't index, we are creating new pairs of key-value
D[1] = 'a' # D{1: 'a'}
D[2] = 'b' # D{1: 'a', 2: 'b'}
print(D)

# We can use immutable types for creating keys on a dictionarie thats why using a tuple works
# Strings, integers, and tuples are immutable while lists, dictionaries and sets are mutable
D[(1,2,3)] = 'c'
print(D)

L = (1,2,3)
S = {1,2,3}
D2 = {1: 'C'}
# All below occurs an error , unhashable type (list/set/dict)
D[L] = 'A' 
D[S] = 'B' 
D[D2] = 'C'