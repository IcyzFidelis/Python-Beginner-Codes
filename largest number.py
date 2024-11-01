numbers = [5, 10, 20, 50, 100, 200, 500, 1000]
largest_number = numbers[0]
for figures in numbers:
  if figures > largest_number:
    largest_number = figures
print("The largest number is:",largest_number)
