s = "abcdefgh"

for char in s:
    print(ord(char))

sum = 0

for char in s:
    sum += ord(char)

print(sum)

# Map takes an function and a iterable object as arguments to return a generator. 
for ascii_char in map(ord,s):
    print(ascii_char)

print([ord(char) for char in s])