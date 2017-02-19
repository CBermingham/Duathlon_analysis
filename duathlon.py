import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def straight_line(x, m, c):
	y = m*x + c
	return y

list1 = []
list2 = []
list3 = []
total = []

f = open("chilly_duathlon.csv", 'rU')
next(f)
reader = csv.reader(f, None) 
for row in reader:
    list1.append(str(row[14]))
    list2.append(str(row[17]))
    list3.append(str(row[20]))
    total.append(str(row[6]))
f.close()

list1 = [list1[i] for i in range(0, len(total)) if total[i] != "DNF"]
list2 = [list2[i] for i in range(0, len(total)) if total[i] != "DNF"]
list3 = [list3[i] for i in range(0, len(total)) if total[i] != "DNF"]


run1 = [(60*float(list1[i][:2]) + float(list1[i][3:5]))/60.0 for i in range(0, len(list1))]
ride = [(60*float(list2[i][:2]) + float(list2[i][3:5]))/60.0 for i in range(0, len(list2))]
run2 = [(60*float(list3[i][:2]) + float(list3[i][3:5]))/60.0 for i in range(0, len(list3))]

y = range(0, 30)

popt12, pcov12 = curve_fit(straight_line, run1, ride)
y12fit = [straight_line(i, popt12[0], popt12[1]) for i in run1]

popt13, pcov13 = curve_fit(straight_line, run1, run2)
y13fit = [straight_line(i, popt13[0], popt13[1]) for i in run1]

popt23, pcov23 = curve_fit(straight_line, ride, run2)
y23fit = [straight_line(i, popt23[0], popt23[1]) for i in ride]

plt.figure(tight_layout = True)

plt.subplot(3, 1, 1)
plt.scatter(run1, ride)
plt.scatter(run1[169], ride[169], color = 'r')
plt.plot(run1, y12fit, color = 'g')
plt.xlabel("run1 (mins)")
plt.ylabel("ride (mins)")

plt.subplot(3, 1, 2)
plt.scatter(run1, run2)
plt.scatter(run1[169], run2[169], color = 'r')
plt.plot(run1, y13fit, color = 'g')
plt.xlabel("run1 (mins)")
plt.ylabel("run2 (mins)")

plt.subplot(3, 1, 3)
plt.scatter(ride, run2)
plt.scatter(ride[169], run2[169], color = 'r')
plt.plot(ride, y23fit, color = 'g')
plt.xlabel("ride (mins)")
plt.ylabel("run2 (mins)")

plt.show()