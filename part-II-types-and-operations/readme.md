# 📘 Learning Python – 5th Edition

## 📖 Solved Exercises

### ✅ Part 2 – Types and Operations

#### 🧪 Exercise 1 – The Basics

> Experiment interactively with the common type operations found in the various operation tables in this part of the book. To get started, bring up the Python interactive interpreter, type each of the following expressions, and try to explain what’s happening in each case.

**Solution:**
**File:** `ex1thebasics.py`

#### 🧪 Exercise 2 – Indexing and Slicing

> At the interactive prompt, define a list named L that contains four strings or numbers (e.g., L=[0,1,2,3]). Then, experiment with the following boundary cases.

> What happens when you try to index out of bounds (e.g., L[4])?

> What about slicing out of bounds (e.g., L[−1000:100])?

> Finally, how does Python handle it if you try to extract a sequence in reverse,
with the lower bound greater than the higher bound (e.g., L[3:1])? 

> Hint: try assigning to this slice (L[3:1]=['?']), and see where the value is put. Do you
think this may be the same phenomenon you saw when slicing out of bounds?

**Solution:**
**File:** `ex2indexing_and_slicing.py`

#### 🧪 Exercise 3 – Indexing Slicing and Del

> Define another list L with four items, and assign an empty
list to one of its offsets (e.g., L[2]=[]). . What happens? 

> Then, assign an empty list to a slice (L[2:3]=[]). What happens now?

> The del statement deletes offsets, keys, attributes, and names. Use it on your list to delete an item (e.g., del L[0]). What happens if you delete an entire slice (del L[1:])?

> What happens when you assign a nonsequence to a slice (L[1:2]=1)?

**Solution:**
**File:** `ex3indexing_slicing_del.py`

#### 🧪 Exercise 4 – Tuple Assignment

> Type the following lines:

```bash
% python
X = 'spam'
Y = 'eggs'
X, Y = Y, X
```

> What do you think is happening to X and Y when you type this sequence?

**Solution:**
**File:** `ex4tuple_assignment.py`

#### 🧪 Exercise 5 – Dictionary keys

> Consider the following code fragments:

```bash
D = {}
D[1] = 'a'
D[2] = 'b'
```

> You’ve learned that dictionaries aren’t accessed by offsets, so what’s going on here?

> Does the following shed any light on the subject?

```bash
D[(1,2,3)] = 'c'
```

> Strings, integers, and tuples share which type category?

**Solution:**
**File:** `ex5dictionary_keys.py`

#### 🧪 Exercise 6 – Dictionary Indexing

> Create a dictionary named D with three entries, for keys 'a', 'b', and 'c'. What happens if you try to index a nonexistent key (D['d'])?

> What does Python do if you try to assign to a nonexistent key 'd' (e.g., D['d']='spam')?

> How does this compare to out-of-bounds assignments and references for lists?

> Does this sound like the rule for variable names?

**Solution:**
**File:** `ex6dictionary_indexing.py`

#### 🧪 Exercise 7 – Generic Operations

> Run interactive tests to answer the following questions:

> What happens when you try to use the + operator on different/mixed types (e.g., string + list, list + tuple)?

> Does + work when one of the operands is a dictionary?

> Does the append method work for both lists and strings?
> How about using the keys method on lists?
> What does append assume about its subject object?

> Finally, what type of object do you get back when you slice or concatenate two lists or two strings?

**Solution:**
**File:** `ex7generic_operations.py`

#### 🧪 Exercise 8 – String Indexing

> Define a string S of four characters: S = "spam". Then type the following expression: S[0][0][0][0][0]. Any clue as to what’s happening this time?

>  Does this indexing expression still work if you apply it to a list such as ['s', 'p', 'a', 'm']? Why?

**Solution:**
**File:** 

#### 🧪 Exercise 9 – Immutable Types

> Define a string S of four characters again: S = "spam". Write an assignment that changes the string to "slam", using only slicing and concatenation. Could you perform the same operation using just indexing and concatenation? 

> How about index assignment?

**Solution:**
**File:** 

#### 🧪 Exercise 10 – Nesting

> Write a data structure that represents your personal information: name (first, middle, last), age, job, address, email address, and phone number. You may build the data structure with any combination of built-in object types you like (lists,tuples, dictionaries, strings, numbers). Then, access the individual components of your data structures by indexing. Do some structures make more sense than others for this object?

**Solution:**
**File:** 

#### 🧪 Exercise 11 – Files

> Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" into it.

> Then write another script that opens my file.txt and reads and prints its contents.

> Run your two scripts from the system command line. Does the new file show up in the directory where you ran your scripts?

> What if you add a different directory path to the filename passed to open?

**Solution:**
**File:** 