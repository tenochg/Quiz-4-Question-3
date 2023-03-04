count = 0
while True:
  x = input('Enter a string: ')
  if 'stop' in x:
    break
  if 'p' in x:
    count = count + 1
print(count)
    