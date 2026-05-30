Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import ipython
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import ipython
ModuleNotFoundError: No module named 'ipython'
>>> int=("73")
>>> int
'73'
>>> x = int("73")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = int("73")
TypeError: 'str' object is not callable
>>> x == str
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x == str
NameError: name 'x' is not defined
>>> x = 1
>>> x == str
False
>>> 164**9
85821209809770512384
>>> 
>>> str(1)
'1'
>>> str(int("1"))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str(int("1"))
TypeError: 'str' object is not callable
islower("I AM DONALD TRUMP! #MAGA!")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    islower("I AM DONALD TRUMP! #MAGA!")
NameError: name 'islower' is not defined
IMPORT NUMPY
SyntaxError: invalid syntax
import numpy

numpy.char.isupper("I AM DONALD TRUMP! #MAGA!")
np.True_
my_string = "Today, President Donald J. Trump directed the Department of Justice to launch an investigation into the nation’s largest meat packing companies for potential collusion, price fixing, and price manipulation. This decisive action targets the foreign-dominated conglomerates that control America’s meat supply and have been accused of artificially inflating prices at the expense of farmers, ranchers, and working families."
my_string
'Today, President Donald J. Trump directed the Department of Justice to launch an investigation into the nation’s largest meat packing companies for potential collusion, price fixing, and price manipulation. This decisive action targets the foreign-dominated conglomerates that control America’s meat supply and have been accused of artificially inflating prices at the expense of farmers, ranchers, and working families.'
my_string.upper()
'TODAY, PRESIDENT DONALD J. TRUMP DIRECTED THE DEPARTMENT OF JUSTICE TO LAUNCH AN INVESTIGATION INTO THE NATION’S LARGEST MEAT PACKING COMPANIES FOR POTENTIAL COLLUSION, PRICE FIXING, AND PRICE MANIPULATION. THIS DECISIVE ACTION TARGETS THE FOREIGN-DOMINATED CONGLOMERATES THAT CONTROL AMERICA’S MEAT SUPPLY AND HAVE BEEN ACCUSED OF ARTIFICIALLY INFLATING PRICES AT THE EXPENSE OF FARMERS, RANCHERS, AND WORKING FAMILIES.'
my_string.lower()
'today, president donald j. trump directed the department of justice to launch an investigation into the nation’s largest meat packing companies for potential collusion, price fixing, and price manipulation. this decisive action targets the foreign-dominated conglomerates that control america’s meat supply and have been accused of artificially inflating prices at the expense of farmers, ranchers, and working families.'
import translate
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import translate
ModuleNotFoundError: No module named 'translate'
mystring.strip()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    mystring.strip()
NameError: name 'mystring' is not defined. Did you mean: 'my_string'?
my_string.strip()
'Today, President Donald J. Trump directed the Department of Justice to launch an investigation into the nation’s largest meat packing companies for potential collusion, price fixing, and price manipulation. This decisive action targets the foreign-dominated conglomerates that control America’s meat supply and have been accused of artificially inflating prices at the expense of farmers, ranchers, and working families.'
my_string.swapcase()
'tODAY, pRESIDENT dONALD j. tRUMP DIRECTED THE dEPARTMENT OF jUSTICE TO LAUNCH AN INVESTIGATION INTO THE NATION’S LARGEST MEAT PACKING COMPANIES FOR POTENTIAL COLLUSION, PRICE FIXING, AND PRICE MANIPULATION. tHIS DECISIVE ACTION TARGETS THE FOREIGN-DOMINATED CONGLOMERATES THAT CONTROL aMERICA’S MEAT SUPPLY AND HAVE BEEN ACCUSED OF ARTIFICIALLY INFLATING PRICES AT THE EXPENSE OF FARMERS, RANCHERS, AND WORKING FAMILIES.'
my_string.title()
'Today, President Donald J. Trump Directed The Department Of Justice To Launch An Investigation Into The Nation’S Largest Meat Packing Companies For Potential Collusion, Price Fixing, And Price Manipulation. This Decisive Action Targets The Foreign-Dominated Conglomerates That Control America’S Meat Supply And Have Been Accused Of Artificially Inflating Prices At The Expense Of Farmers, Ranchers, And Working Families.'
