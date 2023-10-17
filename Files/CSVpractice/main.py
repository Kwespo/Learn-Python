import csv 

price = []

# Reading the data

with open("main.csv") as f:
  reader = csv.reader(f, delimiter = ",")
  lineNum = 0

  for row in reader:
    if lineNum == 0:
      price.append(row)
    else:
      price.append([f"#: {lineNum} Data: " + row[0], row[1]]) 
      
    lineNum += 1

print(price)


# Saving the file

with open("Main_New.csv", 'w') as f:
  writer = csv.writer(f, delimiter = ",")

  for row in price:
    writer.writerow(row)


print("YEAAAAAAAAAAAAA")