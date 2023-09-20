# File: P2_04_intermezzo_debugging_1/getting_visibility.py

# Our most powerful tool for Discovery Debugging is 'getting visibility' — 
# using print to print out values in the program.

def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 1:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")
      
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")