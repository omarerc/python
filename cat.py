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
  n = int(input("What's n?"))
  loop_while(n)
  loop_for(n)
  print_asterisk(n)

main()