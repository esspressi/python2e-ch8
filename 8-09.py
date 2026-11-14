def main():
  scores = [2.5, 8.3, 6.5, 4.0, 5.2]
  total = 0.0
  for value in scores:
    total += value
  average = total / len(scores)
  print('The average of the elements is', average)
  
main()
