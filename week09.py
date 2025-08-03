def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW
def sum_of_digits(n):
    """Computes recursively the sum of digits in an integer
    """
    if n < 10: #if n is less than ten then sum of digits is n, because its a single digit as well
        # Base case
        result = n
    else:
        # Recursive case
        result = (n % 10) + sum_of_digits(n // 10) # if n has multiple digits, then it gets the last digit then removes that last digit and the last digit is then added to the sum and the remaining digits go into the next recursive call
    return result

def count_occurrences(data_list, target):
    """Computes recursively how many times target appears in data_list
    """
    if len(data_list) == 0: # if list is empty return 0
        # Base case
        result = 0
    else:
        # Recursive case
        if data_list[0] == target: # if first digit of list matches target you add 1
            result = 1 + count_occurrences(data_list[1:], target)
        else:
            result = 0 + count_occurrences(data_list[1:], target) # if first digit does not match target add 0 or dont count it
    return result

def factorial_iterative(n):
    """Computes iteratively n! = 1 * 2 * ... * (n-1) * n
    """
    result = 1 # start with one or assume
    for i in range(1, n + 1): # go through numbers 1 to n
        result *= i # multiply result by each digit or i one by one
    return result

def fibonacci_iterative(n): # fibonacci is when the digits on a list are the sum of the two before it
    """Computes iteratively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2: # if n is 1 or 2 return n
        # Base case
        result = n
    else:
        # Iterative case
        a = 1 # start with first two fibonacci numbers 1 and 2
        b = 2
        for i in range(3, n + 1): # starts at 3 because we already have 1 and 2 and will run until i = n 
            temp = a + b # calc next fibonacci number adding last two numbers and temp is now the new fibonacci number
            a = b # now b, the last fibonacci number is a, which makes a the second to last number
            b = temp # now b is the new fibonacci number
        result = b
    return result

#Reflection
# in person.py I used only _birthday when I should have mixed _birthdy and birthday since _ only means it is private
# comments in my version are disorganized while the solutions one is in  proper docstrings
# in birthday.py for set_month i overexplained when i could have made it simpler in the if statement and made self month private with an underscore
# again should've used docstrings for comments
# and different methodology in calculation of day of year so its not readable to many