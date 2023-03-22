def main():
  n = int(input("Enter a number: "))
  print(f"{n}! {factorial(n)}")
  print(f"2^{n}: {base2(n)}")
  
def factorial(n):
  result = 1
  for i in range(int(n)):
    result *= (i + 1)
  return result

def base2(n):
  result = 1
  for i in range(int(n)):
    result *= 2
  return result
  
if __name__ == "__main__":
  main()

