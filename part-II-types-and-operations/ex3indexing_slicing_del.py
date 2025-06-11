l = [1,2,3,4]

l[2] = [] # Replace and inserts an empty sublist in index 2 = [1,2,[],4]

l[2:3] = [] # Assigning an empty list to a slice deletes the slide = [1,2,4]

del l[0]  # Delete at index 0 = [2,4]

del l[1:] # = [2]

l[1:2] = 1 # TypeError, slice expects another sequence , it inserts inside the sequence not the sequence itself

l[1:2] = [1] # Works, since it's a list wich is an iterable = [2, 1]