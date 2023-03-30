def (salary):
  salary.sort()
  salary = salary[1:-1]
  average_salary = sum(salary)/len(salary)
  return average_salary

