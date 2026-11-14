def main():
  infile = open('numberlist.txt', 'r')
  numbers = infile.readlines()
  infile.close()
  index = 0
  while index < len(numbers):
    numbers[index] = int(numbers[index])
    index += 1
  print(numbers)

main()
