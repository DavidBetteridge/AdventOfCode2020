# Advent of Code 2020

## Day 1 - Report Repair

### Part 1 - Find two numbers in your list which sum to 2020

+ Store the list into a dictionary.
+ Look at each number in turn and subtract it from 2020.  
+ Check to see if that number in the list.

#### Notes

+ One number must be more than 1010 and the other less than 1010

### Part 2 - Find three numbers in your list which sum to 2020

+ Same idea as part 1 but with an extra loop
+ Number of checks required can be reduced by sorting the list

---

## Day 2 - Password Philosophy

### Parts 1 and 2 - How many passwords are valid according to their policies?

+ Used regular expressions to parse the input.

+ Different policy is required for part 2.   Reused code by passing in the desired policy as a function

---

## Day 3 - Toboggan Trajectory

### Part 1 - How many trees would you hit moving right 3, down 1?

+ Forest wraps around (right->left->right) so the toboggan's x positions needs to be mod the forest with.

### Part 2 - How many trees would you hit with multiple slopes?

+ Same code as part 1,  but passing in different slopes (other than 3,1)

---

## Day 4 - Passport Processing

### Part 1 - Number of passports which contain all fields

+ Nice trick when parsing the input which is to separate the passports with `.split('\n\n')`

### Part 2 - Number of valid passports

+ Created a function called `is_in_range` and then used `partial` from `functools` in order to supply the first argument.

+ Used regular expressions for other validations

---

## Day 5 - Binary Boarding

### Part 1 - What is the highest seat ID on a boarding pass?

+ Trick here is to spot the seat ids are just binary numbers!

### Part 2 - What is the ID of your seat?

+ Found it easier to ignore `the seats with IDs +1 and -1 from yours will be in your list.` in the problem statement!

---

## Day 6 - Custom Customs

+ The idea is to use the intersection of sets to give you anyone who answered yes to a question

+ Part 2 is the same,  but using the union of sets

---

## Day 7 - Handy Haversacks

+ As the definitions of which bags contain which other bags are nested,  it means that recursion should be used.

---

## Day 8 - Handheld Halting

+ Very simple VM with just three instructions and two registers (`accumulator` and `instruction pointer`)

+ Part 2 is harder as one instruction is corrupted.  I just brute forced changing the instructions one by one.

---

## Day 9 - Encoding Error

+ Requires a sliding window of length 25 over the list of numbers

