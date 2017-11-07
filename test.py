

i = [310,]
proc = 0.01
num_days = 300
a = 0.0


def summa (i,a):
  sum = 0
  for item in i:
    sum += item
  sum += a
  return sum

for day in range(1, num_days):
  for item in i:
    a = a + item * proc
  if a > 10:
    i.append(a)
    a = 0
  print (day, summa(i,a))
