import cowsay
import sys

try:
  if len(sys.argv) >= 2:
    cowsay.cow(f"Hello {sys.argv[1]}")
    cowsay.trex(f"Hello {sys.argv[1]}")
    cowsay.turtle(f"Hello {sys.argv[1]}")
    cowsay.miki(f"Hello {sys.argv[1]}")
    cowsay.dragon(f"Hello {sys.argv[1]}")
    cowsay.tux(f"Hello {sys.argv[1]}")
except IndexError:
  sys.exit("Too few arguments.")