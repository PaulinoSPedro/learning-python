# 📘 Learning Python – 5th Edition

## 📖 Solved Exercises

### ✅ Part 3 – Statements and Syntax

#### 🧪 Exercise 1 – Basic Loops

> Write a for loop that prints the ASCII code of each character in a string named S. 

> Change your loop to compute the sum of the ASCII codes of all the characters in a string.

> Modify your code again to return a new list that contains the ASCII codes of each character in the string. Does the expression map(ord, S) have a similar effect? How about [ord(c) for c in S]? Why?

**Solution:**
**File:** `ex1basic_loops.py`

#### 🧪 Exercise 2 – Backslash Characters

> What happens on your machine when you type the following code interactively?

```bash
    for i in range(50):
        print('hello %d\n\a' % i)
```

**Solution:**
**File:** ``

#### 🧪 Exercise 3 – Sorting Dictionaries

> Write a for loop that prints a dictionary’s items in sorted (ascending) order.

**Solution:**
**File:** ``

#### 🧪 Exercise 4 – Program Logic Alternatives

> Consider the following code, which uses a while loop and found flag to search a list of powers of 2 for the value of 2 raised to the fifth power (32). It’s stored in a module file called power.py.

> First, rewrite this code with a while loop else clause to eliminate the found flag and final if statement.

> Next, rewrite the example to use a for loop with an else clause, to eliminate the explicit list-indexing logic.

> Next, remove the loop completely by rewriting the example with a simple in operator membership expression.

> Finally, use a for loop and the list append method to generate the powers-of-2list (L) instead of hardcoding a list literal

> Do you think it would improve performance to move the 2 ** X expression outside the loops? How would you code that?

> As we saw in exercise 1, Python includes a map(function, list) tool that can generate a powers-of-2 list, too: map(lambda x: 2 ** x, range(7)). Would a list comprehension help here ?

**Solution:**
**File:** ``
