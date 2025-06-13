# 📘 Learning Python – 5th Edition

## 📖 Solved Exercises

### ✅ Part 1 – Getting Started with Python

#### 🧪 Exercise 1 – Hello World (Command Line)

> Use your system command line, IDLE, or any interactive shell to type the expression `"Hello World"`.

**Solution:**
**File:** `ex1interaction.py`
```bash
% python
"Hello World!"
```

#### 🧪 Exercise 2 – Hello World(Text Editor)

>  With the text editor of your choice, write a simple module file containing
the single statement print('Hello module world!') and store it.
Run this file by using any launch option

**Solution:**
**File:** `ex2programs.py`

#### 🧪 Exercise 3 – Modules

>  Start Python interactive command line and import the module of exercise 2. Try moving the file to a different directory and import it again from its original directory. What happens ?

**Solution:**
**File:** `ex3modules.py`

#### 🧪 Exercise 4 – Scripts

>  If your platform supports it, add the #! line to the top of your module file, give the file executable privileges, and run it directly as an executable. 

> What does the first line need to contain? #! usually only has meaning on Unix, Linux, and Unix-like platforms such as Mac OS X; if you’re working on Windows, instead try running your file by listing just its name in a Command Prompt window without the word “python” before it (this works on recent versions of Windows), via the Start→Run... dialog box, or similar. If you are using Python 3.3 or the Windows launcher that installs with it, experiment with changing your script’s #! line to launch different Python versions you may have installed on your computer

**Solution:**
**File:** `ex4scripts.py`

#### 🧪 Exercise 5 – Erros and Debbuging

> Experiment with typing mathematical expressions and assignments at the Python interactive command line. Along the way, type the expressions 2 ** 500 and 1 / 0, and reference an undefined variable name as we did early on in this chapter. What happens?

**Solution:**
```bash
% python
2 ** 500
1 / 0 -> This triggers an exception "ZeroDivisionError" 
```

> The default handler catch an error and display the standard error showing the lines in your code were active when the error occurred, this is an useful tool of Python. Alternatively you can use -i command-line argument to enter into interactive interpreter mode when the script exits:

```bash
% python -i ex5erros_and_debugging.py

```
**File:** `ex5erros_and_debugging.py`

#### 🧪 Exercise 6 – Breaks and Cycles

> At python command line, type:

    L = [1, 2]
    L.append(L)
    L

> What happens? 

**Solution:**
**File:** `ex6breaks_and_cycles.py`

#### 🧪 Exercise 7 – Documentation

> Spend at least 15 minutes browsing the Python library and lan
guage manuals before moving on to get a feel for the available tools in the standard library and the structure of the documentation set. It takes at least this long to become familiar with the locations of major topics in the manual set; once you’ve done this, it’s easy to find what you need.

Ways to find the documentation:
<ul>
    <li>Python Module Docs on your machine</li>
    <li>https://www.python.org/doc/</li>
</ul>
