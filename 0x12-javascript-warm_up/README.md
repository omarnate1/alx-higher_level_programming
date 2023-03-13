0x12. Javascript - Warm up
Resources📚
Read or watch:

Writing JavaScript Code
Variables
Data Types
Operators
Operator Precedence
Controlling Program Flow
Functions
Objects and Arrays
Intrinsic Objects
Module patterns
var, let and const
Javascript Tutorial
Modern JS
Learning Objectives💡
What you should learn from this project:

Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
How to run a Javascript script
How to create variables and constants
What are differences between var, const and let
What are all the data types available in Javascript
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use while and for loops
How to use break and continue statements
What is a function and how do you use functions
What does a function that does not use any return statement return
Scope of variables
What are the arithmetic operators and how to use them
How to manipulate dictionary
How to import a file
0. First constant, first print
Write a script that prints “Javascript is amazing”:
You must create a constant variable called myVar with the value “Javascript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
1. 3 languages
Write a script that prints 3 lines:
The first line: “C is fun”
The second line: “Python is cool”
The third line: “Javascript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
2. Arguments
Write a script that prints a message depending of the number of arguments passed:
If no arguments are passed to the script, print “No argument”
If only one argument is passed to the script, print “Argument found”
Otherwise, print “Arguments found”
You must use console.log(...) to print all output
You are not allowed to use var
Reference: process.argv

guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
guillaume@ubuntu:~/0x12$ 
3. Value of my argument
Write a script that prints the first argument passed to it:
If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
guillaume@ubuntu:~/0x12$ 
4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: “ is ”
You must use console.log(...) to print all output
You are not allowed to use var
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
5. An Integer
Write a script that prints My number: if the first argument can be converted to an integer:
If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
guillaume@ubuntu:~/0x12$ 
6. Loop to languages
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
The first line: “C is fun”
The second line: “Python is cool”
The third line: “Javascript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use any if/else statement
You can use only one console.log
You must use a loop (while, for, etc.)
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
7. I love C
Write a script that prints x times “C is fun”
Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
8. Square
Write a script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
9. Add
Write a script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
10. Factorial
Write a script that computes and prints a factorial
The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer

If no argument passed, print 0

If the number of arguments is 1, print 0

You must use console.log(...) to print all output

You are not allowed to use var

guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
12. Object
Update this script to replace the value 12 with 89:
You are not allowed to use var
guillaume@ubuntu:~/0x12$ cat 12-object.js
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
13. Add file
Write a function that returns the addition of 2 integers.

The function must be visible from outside The name of the function must be add You are not allowed to use var

Tip from Jared

guillaume@ubuntu:~/0x12$ cat 13-main.js
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
14. Const or not const
Write a file that modifies the value of myVar to 333
guillaume@ubuntu:~/0x12$ cat 100-main.js
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
Do you get it? Tweet! Post! Talk about it!

Hint: Scope

This exercise doesn’t pass semistandard so don’t worry about it.

15. Call me Moby
Write a function that executes x times a function.
The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
guillaume@ubuntu:~/0x12$ cat 101-main.js
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
16. Add me maybe
Write a function that increments and calls a function.
The function must be visible from outside
Prototype: function (number, theFunction)
You are not allowed to use var
guillaume@ubuntu:~/0x12$ cat 102-main.js
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
17. Increment object
Update this script by adding a new function incr that increments the integer value.
You are not allowed to use var
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }

