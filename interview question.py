#1.DATA TYPES
#1.What are Data Types?
#A data type is a set of values and a set of operations defined on data.
 #An implementation of a data type is an expression of data and operations
  #in terms of a specific programming language such as Java, C ++, or Python.

  #Data Types	Examples
#Numbers	        1234, 3.1415, 3+4j
#Strings       	‘spam’, “Bob’s”, b’a\x01c’,
#Lists	       [1, [2, ‘three’], 4.5]
#Dictionaries	 {‘food’: ‘spam’, ‘taste’: ‘yum’}
#Tuples      	(1, ‘spam’, 4, ‘U’)
#Sets	        set(‘abc’), {‘a’, ‘b’, ‘c’}

#2.Name four of the main data types in Python?

#Numbers, strings, lists, dictionaries, tuples, files, and sets are generally
 #considered the main types of data. Types, None, and Booleans are sometimes 
 #also classified this way. The integer, floating-point, complex, 
 #fraction and decimal are numerical data types and simple strings and Unicode 
 #strings in Python 2 and text strings and byte strings in Python 3 are the types
  #of string data types


 #3. Why are these data types known as Python’s core data types?

#They are known as the core data types because they are part of the Python language
 #itself and are always available to create other objects, you usually need to
  #call functions in imported modules.

#Most of the data types have a specific syntax for generating objects:
 #“spam”, for example, is an expression that creates a string and determines
  #the set of operations that can be applied to it. For this reason,
   #main types are built into Python syntax. Instead, you must call
    #the built-in open function to create a file object.


#4.What does immutable mean and what three types of Python core data types are considered immutable?

#An immutable data type is a type of object which cannot be modified after its creation. Numbers, strings,
 #and tuples in Python fall into this category. Although you cannot modify an immutable object in place,
  #you can always create a new one by running an expression.



#5.What does sequence mean and which three types of data fall into this category?

#A sequence data type is a collection of objects ordered by a specific position.
 #In Python, Strings, lists, and tuples are the data types based on sequences. 
 #The Sequences share common sequence operations, such as indexing, concatenation,
  #and slicing, but also have type-specific method calls.



#6.What does mapping mean and what kind of data type is based on mapping?

#The term mapping refers to an object that maps keys to associated values.
# The Python dictionary is the only type of mapping in the base typeset.
#  Mappings do not maintain any left-to-right position order; they support
#   access to stored data by key, as well as type-specific method calls.


#   7.What is polymorphism and why should you care?
#Polymorphism means that the meaning of an operation (like a+) depends on the objects 
#being operated. This turns out to be a key idea behind good use of Python, not 
#coercing code to specific types makes that code automatically applied to many types



#OPERATORS

#1.What is an Operator in general?
#In general, an operator is defined as a Character used in Mathematics or in Programming 
#to execute a specific function. For example, operators are used differently in different
# fields. 


#2.What is meant by an Operator in Python?
#These are the special symbols in python and are used to execute an Arithmetic or
# Logical computation. An operator alone cannot perform an activity, it needs an
#  Operand.
#   What is an operand? 
#An Operand is a value that the operator needs to complete a task.

# example 

#>>>10/2       
#5



#CONDITIONAL STATEMENT

#1.What constitutes “True” in Python?
#Answer:
#A true expression is any expression that does not evaluate to 0, 
#the empty list [ ], tuple ( ), dictionary { } or the objects None or False.

#2.What are the three main conditional statements in Python?
#Answer:
#if, elif, and else

#3.What are the comparison operators in Python?
#Answer:
#< Less than, > Greater than, <= Less than or equal to, >= Greater than or equal to, = Equal to,
# != not equal, o alternative not equal. Note a single = is NOT a Python comparison operator, 
# it is an assignment operator only.

#4.Illustrate a basic if, elif, else structure.
#Answer:
#if <condition>:
#. . .
#elif<another condition>:
#. . .
#else:
#. . .

#Python Program to Find nth Prime Number
#Python Data Persistence – Decision Control
#Python Program to Calculate BMI

#5.In Python 2.5+, the equivalent of a tertiary operator has been added to the language. Provide an example of its use.
#Answer:
#myValue = ‘Positive’ if myNumber > 0 else ‘Negative or Zero’

#6.What does elif mean?
#Answer:
#It means else if. It is used after an if statement, to do another comparison.



#7.What would the output be from the following code?
# a =4 If a = 5:
#Print “True”
#Else:
#Print “False”
#Answer:
#This is a trick question. The a = 5 is not a comparison operator, but an assignment. 
#It will yield “True”. The correct coding would be a == 5.

#8.How are if, elif, and else blocks defined?
#Answer:
#All blocks in Python are defined by indenting. All lines of a particular code 
#block must have the same level of indenting.


#9.Illustrate a switch-case equivalent using if-elif-else.
#Answer:
#if item=valueA:
#. . .
#elif item == valueB:
#. . .
#elif item = =  valueC:
#. . .
#elifitem = valueN:
#. . .
#else:
#… #default code

#10.How is the Python switch statement used?
#Answer:
#This is a trick question, there is no built-in switch statement in Python,
# which is unusual. A switch statement can be easily created using if-elif using 
# lambda or with Python dictionaries.


#11.Using a dictionary, create an equivalent to a switch case statement.
#Answer:
#deffunc1( ):
#. . .
#deffunc2( ):
#. . .
#switch = {
#‘Aardvark’: fund1,
#‘Armadillo’: fund2,
#}
#mySwi tchKey= “Armadillo ”
#switch[mySwitchKey]( ) #callsJunc2( )
#switch[‘Aardvark’]( ) #calls func1( )


#12.Illustrate comparing two strings for equality in a case insensitive manner.
#Answer:
#if stringl. lower ( ) = string2.lower ( ):
#Note: .upper( ) is equally valid.


#13.Illustrate comparing two strings, printing if the first string is longer,
# equal, or shorter than the second string.
#Answer:
#if len(stringl) > len(string2):
#print “Stringl is longer than string2.”
#elif len(stringl) < len(string2):
#print “String1 is shorter than string2.”
#else:
#print “String1 is the same length as string2.”


#14.When comparing two d^tes, what method is used?
#Answer:
#Date.toordinal( ) Otherwise, Python would compare the dates by their object address.

#15.In comparing dates and DateTime objects, what happens when one comparand is naive and the other aware?
#Answer:
#A TypeError is raised.


#16.What happens when you try to compare a DateTime object with other classes of objects?
#Answer:
#A TypeError is raised.

#17.When are dictionaries considered equal?
#Answer:
#If and only if their sorted lists compare equally.


#18.How is collection membership determined?
#Answer:
#Using the in and not in operators.

#19Illustrate how collection membership determination would be written.
#Answer:
#if x in collection:
#print “It is in the collection”
#else:
#print “Not in the collection.”

#20.How is object identity tested? Illustrate with an example.
#Answer:
#Using the is and is not operators.
#if x is objecttype:
#print “x is the type you thought it was.
#else:
#print “x isn’t an objecttype.”



#LOOPING STATEMENT

#1. What keyword is used for looping?
#A) while
#B) for
C#) loop

#Answer: for

#2. What function can generate a list of numbers?
#A) for
#B) list
#C) range

#Answer: range

#3. Name the 2 keywords used for looping?
#A) while loop
#B) for loop
#C) for while

#Answer: for while

#4. What module is used for generating random values?
#A) math
#B) random
#C) randrange

#Answer: random

#5. What keyword is used to skip back to the beginning of a loop?
#A) break
#B) while
#C) continue

#Answer: continue

#6. What keyword is used to end looping completely?
#A) end
#B) break
#C) continue

#Answer: break

#7. Use range to generate a list from 1 through 5?
#A) range(1, 5)
#B) range(5)
#C) range(1,6)

#Answer: range(1,6)

#8. Select the code needed to generate a random number between 1 through 50 and assign it to rand_num?
#A) random.randrange(1, 51)
#B) random.randrange(1, 50)
#C) random(1, 50)

#Answer: random.randrange(1, 51)

#9. What numbers does the following Range generate: range(5,10)?
#A) 5,6,7,8,9,10
#B) 6,7,8,9,10
#C) 5,6,7,8,9

#Answer: 5,6,7,8,9

#Explanation: Range starts at 5 and goes up to (but not including) 10

#10. What numbers does the following range generate range(3)?
#A) 3
#B) 1,2,3
#C) 0,1,2,3
#D) 0,1,2

#Answer: 0,1,2

#Explanation: Range will start at 0 and go up to (but not including) 3

#11. What is printed out after the following code nums = range(1,5) print(nums)?
#A) 1,2,3,4
#B) range(1,5)

#Answer: range(1,5)

#Explanation: Printing range does not print out all the numbers in the range.
# We have to iterate over the range with a loop to print the numbers.

#12. What numbers does the following range generate range(8,0,-2):
#A) 0,2,4,6
#B) 8,6,4,2
#C) 8,6,4,2,0

#Answer: 8,6,4,2

#Explanation: The 3rd argument(step) indicates that range should work backwards from 8,
# moving 2 numbers at a time.

#13. What does the following loop do?

#i = 1
#while i < 5:
#i + i
#print(i)

#A) It prints 1,2,3,4,5 and then exits
#B) It prints 1,2,4 then exits
#C) It prints 1 forever

#Answer: It prints 1 forever

#Explanation: Don't forget to add the + before the = sign when incrementing!

#14. What does the following loop do?

# print 1 to 5
#i = 0
#while i <= 5:
#i =+ 1
#print(i)

#A) It prints 1 through 5 because it increments i each time
#B) It prints 0 through 5 because i starts at zero
#C) It prints 1 forever because there is a typo with the increment which should be += instead of =+.
#D) It prints zero through four because i starts at zero and goes up until 5.

#Answer: It prints 1 forever because there is a typo with the increment which should be += instead of =+.

#15. What can we do to get out of the infinite loop below?

#this code runs forever...
#x = 0
#while x != 11:
#x += 2
#print(x)

#A) Change the condition to x ! = 10
#B) Change the condition to x < 11
#C) Add logic that says if x == 10: break
#D) Press control + C while your program is running to kill it
#E) All of the above

#Answer: All of the above

#16. For loops are used to loop over:
#A) Loopy objects
#B) Numbers
#C) Iterable objects
#D) Lines of code

#Answer: Iterable objects

#17. What is the tradeoff when using while loops for looping?
#A) While loops are more flexible since you explicitly set the start and end conditions, but they require more setup than for loops
#B) While loops are faster than for loops but require more setup
#C) While loops can loop infinitely and give you more control, but they cannot be used to iterate over iterable objects

#Answer: While loops are more flexible since you explicitly set the start and end conditions, but they require more setup than for loops

#18. What does the break keyword do?
#A) Exits the loop at the beginning of the next iteration
#B) Breaks your code
#C) Exits the loop at the end of this iteration
#D) Exits the loop immediately

#Answer: Exits the loop immediately

#Explanation: break is the fastest way to get out of a loop -- it won't run any code after the break

#19. What does the following code print?

#for x in range(5):
#print(x)

#A) 1 2 3 4 5
#B) 1 2 3 4
#C) 0 1 2 3 4

#Answer: 0 1 2 3 4

#Explanation: Python ranges start at zero by default and count up to, but not including, the end number


#FUNCTIONS

#1, what is function?
#A function is defined as a relation between a set of inputs having one output each

