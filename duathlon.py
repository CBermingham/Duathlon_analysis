import csv
import matplotlib.pyplot as plt

list1 = []
list2 = []
list3 = []

f = open("chilly_duathlon.csv", 'rU')
next(f)
reader = csv.reader(f, None) 
for row in reader:
    list1.append(str(row[14]))
    list2.append(str(row[17]))
    list3.append(str(row[20]))
f.close()

run1 = [(60*float(list1[i][:2]) + float(list1[i][3:5]))/60.0 for i in range(0, len(list1))]
ride = [(60*float(list2[i][:2]) + float(list2[i][3:5]))/60.0 for i in range(0, len(list2))]
run2 = [(60*float(list3[i][:2]) + float(list3[i][3:5]))/60.0 for i in range(0, len(list3))]

y = range(0, 30)

plt.scatter(run1, run2)
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.scatter(run1[169], run2[169], color = 'r')
plt.plot(y, y)

plt.show()