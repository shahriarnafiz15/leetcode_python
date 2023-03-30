def number(low,high):
  if low % 2 == 0:
    low +1
  elif high % 2 == 0:
    high -1
  return (high-low) // 2
