# The Collatz Sequence
def collatz(value):
    if value%2==0:
        answer = value//2
    elif value%2==1:
        answer=(value*3 + 1)
    return(answer)


print ('Hello give me a number')

while True:
    try:
        number=int(input())
    except ValueError:
        print('Please enter a valid integer value')
        continue
    newValue=collatz(number)
    while newValue != 1:
      print(newValue)
      newValue=collatz(newValue)
      if newValue==1:
          print(newValue)
          break
    break


print('Done!')
