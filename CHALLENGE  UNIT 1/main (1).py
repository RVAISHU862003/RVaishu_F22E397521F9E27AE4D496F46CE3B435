# 1.1 Implement a recursive function to calculate the factorial of a given number.
def factorial(n):
  if (n==1 or n==0):                        # Checking the number  is 1 or 0 then return 1  other wise return factorial
    return 1
  else:
     return (n * factorial(n - 1))
num = 5;                                     # Driver Code
print("number : ",num)
print("Factorial : ",factorial(num))
