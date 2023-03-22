import sys

try:
  for arg in sys.argv[1:]:
    print(arg)
  if len(sys.argv) <= 2:
    print(f"Hello, my name is , {sys.argv[1]}")
  else:
    sys.exit("Too many arguments.")
except IndexError:
  sys.exit("Too few arguments.")