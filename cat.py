def get_value():
  while True:
    try:
      return int(input("What is n? "))
    except ValueError:
      print("X is not a valid value. Try again!")

def loop_while(n):
  i  = 0
  print("Printing with while loop:")
  while i < 3:
    print("meow")
    i += 1

def loop_for(n):
  print("Printing with for loop:")
  for _ in range(3):
    print("meow")

def print_asterisk(n):
  print(f"Print with * {n}:")
  print("meow\n" * n, end="")

def main():
  try:
    n = get_value()
    loop_while(n)
    loop_for(n)
    print_asterisk(n)
  except:
    print("n is not an Integer")

main()