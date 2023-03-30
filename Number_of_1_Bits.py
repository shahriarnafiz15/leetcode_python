def number(n):
  binary = bin(n)[2:]
  return binary.count("1")
