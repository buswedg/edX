
#Introduction to Computer Science and Programming Using Python

##Simple Algorithms

###Problem 1


```python
num = 0
while num <= 5:
    print num
    num += 1

print "Outside of loop"
print num
```

    0
    1
    2
    3
    4
    5
    Outside of loop
    6
    


```python
num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop' 
```

    10
    9
    8
    7
    Breaking out of loop
    Outside of loop
    

###Problem 2A

Convert the following into code that uses a while loop:

print 2
print 4
print 6
print 8
print 10
print Goodbye!


```python
num = 2
while num < 11:
    print num
    num += 2
print "Goodbye!"
```

    2
    4
    6
    8
    10
    Goodbye!
    

###Problem 2B

Convert the following into code that uses a while loop:

print Hello!
print 10
print 8
print 6
print 4
print 2


```python
print "Hello!"
num = 10
while num > 0:
    print num
    num -= 2
```

    Hello!
    10
    8
    6
    4
    2
    

###Problem 2C

Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.


```python
total = 0
current = 1
end = 6
while current <= end:
    total += current
    current += 1

print total
```

    21
    

###Problem 3


```python
myStr = '6.00x'

for char in myStr:
    print char

print 'done' 
```

    6
    .
    0
    0
    x
    done
    


```python
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter

print 'done'
```

    H
    e
    e
    l
    l
    l
    o
    !
    !
    done
    


```python
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons) 
```

    M
    numVowels is: 11
    numCons is: -25
    

###Problem 4


```python
num = 10
for num in range(5):
    print num
print num 
```

    0
    1
    2
    3
    4
    4
    


```python
divisor = 2
for num in range(0, 10, 2):
    print num/divisor 
```

    0
    1
    2
    3
    4
    


```python
for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!' 
```

    0
    Foo!
    4
    8
    12
    16
    Foo!
    


```python
for letter in 'hola':
    print letter  
```

    h
    o
    l
    a
    


```python
count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 
```

    Letter # 0 is S
    1
    

###Problem 5A

Convert the following code into code that uses a for loop:

print 2
print 4
print 6
print 8
print 10
print "Goodbye!"


```python
for count in range(11):
    if count != 0 and count % 2 == 0:
        print count
print "Goodbye!"
```

    2
    4
    6
    8
    10
    Goodbye!
    

###Problem 5B

Convert the following code into code that uses a for loop:

print "Hello!"
print 10
print 8
print 6
print 4
print 2


```python
print "Hello!"
for num in range(0, 10, 2):
    print 10 - num
```

    Hello!
    10
    8
    6
    4
    2
    

###Problem 5C

Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.


```python
total = 0
end = 6
for next in range(1, end+1):
    total += next
print total
```

    21
    

###Problem 6


```python
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
```

    Iteration 0; count is: 12
    Iteration 1; count is: 24
    Iteration 2; count is: 36
    Iteration 3; count is: 48
    Iteration 4; count is: 60
    


```python
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
```

    Iteration 0; count is: 12
    Iteration 1; count is: 12
    Iteration 2; count is: 12
    Iteration 3; count is: 12
    Iteration 4; count is: 12
    


```python
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
```

    Iteration 0; count is: 1
    Iteration 1; count is: 12
    Iteration 2; count is: 1
    Iteration 3; count is: 12
    Iteration 4; count is: 1
    

###Problem 7


```python
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
```

    Iteration 0; count is: 12
    Iteration 1; count is: 24
    Iteration 2; count is: 36
    Iteration 3; count is: 48
    Iteration 4; count is: 60
    

We wish to re-write the above code, but instead of nesting a for loop inside a while loop, we want to nest a while loop inside a for loop. Which of the following loops gives the same output as the Code Sample?


```python
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

    Iteration 0; count is: 12
    Iteration 1; count is: 24
    Iteration 2; count is: 36
    Iteration 3; count is: 48
    Iteration 4; count is: 60
    


```python
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

    Iteration 0; count is: 12
    Iteration 1; count is: 24
    Iteration 2; count is: 36
    Iteration 3; count is: 48
    Iteration 4; count is: 60
    


```python
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

    Iteration 0; count is: 12
    Iteration 1; count is: 24
    Iteration 2; count is: 36
    Iteration 3; count is: 48
    Iteration 4; count is: 60
    

###Problem 8


```python
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
```

    succeeded: 5.0
    

###Problem 9

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!


```python
print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
```

    Please think of a number between 0 and 100!
    Is your secret number 50?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
    Game over. Your secret number was: 50
    
