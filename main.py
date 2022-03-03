"""
Given a number n as input, calculate the nth power of 2. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> 4
Output-> 16
"""

def recur(n):
  if (n==0):
    return 1
  else:
    return (2 * recur(n-1))

n=4
print(recur(n))