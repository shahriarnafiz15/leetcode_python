def subtractProductAndSum(n): 
  n = str(n)
  number = [int(p) for p in n]

  multi = 1
  plus = 0

  for i in number:
    multi *= i
    plus  += i
  return multi-plus
