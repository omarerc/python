from series import base2

def main():
  # Ask user name
  name = input("What's your name? ")
  message = hello(name)
  print(message)
  loop()
  n = input("Enter a number: ")
  result = base2(n)
  print(f"2^{n}: {result}")

def loop():
  i = 0
  while i < 3: 
    # Compare two numbers
    a = input("Insert number A: ")
    b = input("Insert number B: ")
    message = compare(a, b)
    print(f"{i}: {message}")
    i += 1

def compare(a=0, b=0):
  if a > b:
    return (f"{a} es mayor que {b}")
  elif b > a:
    return (f"{a} es menor que {b}")
  else:
    return (f"{a} es igual que {b}")

def hello(to="World"):
  # Say hello to user
  return(f"Hello, {to}:\nHave a great day!!!")

main()