def main():
  numbers = get_values()
  print('The numbers in the list are:')
  print(numbers)

def get_values():
  values = []
  again = 'y'
  while again == 'y':
    num = int(input('Enter a number: '))
    values.append(num)
    print('Do you want to add another number?')
    again = input('y = yes, anything else = no: ')
    print()
  return values

main()
