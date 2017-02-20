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
gender = []

f = open("chilly_duathlon.csv", 'rU')
next(f)
reader = csv.reader(f, None) 
for row in reader:
    list1.append(str(row[14]))
    list2.append(str(row[17]))
    list3.append(str(row[20]))
    total.append(str(row[6]))
    gender.append(str(row[9]))
f.close()

list1 = [list1[i] for i in range(0, len(total)) if total[i] != "DNF"]
list2 = [list2[i] for i in range(0, len(total)) if total[i] != "DNF"]
list3 = [list3[i] for i in range(0, len(total)) if total[i] != "DNF"]
total = [total[i] for i in range(0, len(total)) if total[i] != "DNF"]


run1 = [(60*float(list1[i][:2]) + float(list1[i][3:5]))/60.0 for i in range(0, len(list1))]
ride = [(60*float(list2[i][:2]) + float(list2[i][3:5]))/60.0 for i in range(0, len(list2))]
run2 = [(60*float(list3[i][:2]) + float(list3[i][3:5]))/60.0 for i in range(0, len(list3))]
total = [(60*float(total[i][:2]) + float(total[i][3:5]))/60.0 for i in range(0, len(total))]

total_new = []
for i in total:
	if i < 40:
		total_new.append(i + 60)
	else:
		total_new.append(i)
total = total_new


popt12, pcov12 = curve_fit(straight_line, run1, ride)
y12fit = [straight_line(i, popt12[0], popt12[1]) for i in run1]

popt13, pcov13 = curve_fit(straight_line, run1, run2)
y13fit = [straight_line(i, popt13[0], popt13[1]) for i in run1]

popt23, pcov23 = curve_fit(straight_line, ride, run2)
y23fit = [straight_line(i, popt23[0], popt23[1]) for i in ride]

poptt1, pcovt1 = curve_fit(straight_line, total, run1)
yt1fit = [straight_line(i, poptt1[0], poptt1[1]) for i in total]

poptt2, pcovt2 = curve_fit(straight_line, total, ride)
yt2fit = [straight_line(i, poptt2[0], poptt2[1]) for i in total]

poptt3, pcovt3 = curve_fit(straight_line, total, run2)
yt3fit = [straight_line(i, poptt3[0], poptt3[1]) for i in total]




run1_female = [run1[i] for i in range(0, len(run1)) if gender[i] == "Female"]
run1_male = [run1[i] for i in range(0, len(run1)) if gender[i] == "Male"]

ride_female = [ride[i] for i in range(0, len(ride)) if gender[i] == "Female"]
ride_male = [ride[i] for i in range(0, len(ride)) if gender[i] == "Male"]

run2_female = [run2[i] for i in range(0, len(run2)) if gender[i] == "Female"]
run2_male = [run2[i] for i in range(0, len(run2)) if gender[i] == "Male"]

total_female = [total[i] for i in range(0, len(total)) if gender[i] == "Female"]
total_male = [total[i] for i in range(0, len(total)) if gender[i] == "Male"]

plt.figure(figsize = (8, 8), tight_layout = True)

plt.subplot(3, 2, 1)
plt.scatter(run1_male, ride_male, color = 'darkviolet', label = "Male", s = 4)
plt.scatter(run1_female, ride_female, color = 'darkturquoise', label = "Female", s = 4)
plt.scatter(run1[169], ride[169], color = 'r', s = 15)
plt.plot(run1, y12fit, color = 'k')
plt.xlabel("run1 (mins)")
plt.ylabel("ride (mins)")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.165), fontsize = 10, ncol=2)

plt.subplot(3, 2, 3)
plt.scatter(run1_male, run2_male, color = 'darkviolet', s = 4)
plt.scatter(run1_female, run2_female, color = 'darkturquoise', s = 4)
plt.scatter(run1[169], run2[169], color = 'r', s = 15)
plt.plot(run1, y13fit, color = 'k')
plt.xlabel("run1 (mins)")
plt.ylabel("run2 (mins)")

plt.subplot(3, 2, 5)
plt.scatter(ride_male, run2_male, color = 'darkviolet', s = 4)
plt.scatter(ride_female, run2_female, color = 'darkturquoise', s = 4)
plt.scatter(ride[169], run2[169], color = 'r', s = 15)
plt.plot(ride, y23fit, color = 'k')
plt.xlabel("ride (mins)")
plt.ylabel("run2 (mins)")

plt.subplot(3, 2, 2)
plt.scatter(total_male, run1_male, color = 'darkviolet', label = "Male", s = 4)
plt.scatter(total_female, run1_female, color = 'darkturquoise', label = "Female", s = 4)
plt.scatter(total[169], run1[169], color = 'r', s = 15)
plt.plot(total, yt1fit, color = 'k')
plt.xlabel("total (mins)")
plt.ylabel("run1 (mins)")

plt.subplot(3, 2, 4)
plt.scatter(total_male, ride_male, color = 'darkviolet', label = "Male", s = 4)
plt.scatter(total_female, ride_female, color = 'darkturquoise', label = "Female", s = 4)
plt.scatter(total[169], ride[169], color = 'r', s = 15)
plt.plot(total, yt2fit, color = 'k')
plt.xlabel("total (mins)")
plt.ylabel("ride (mins)")

plt.subplot(3, 2, 6)
plt.scatter(total_male, run2_male, color = 'darkviolet', label = "Male", s = 4)
plt.scatter(total_female, run2_female, color = 'darkturquoise', label = "Female", s = 4)
plt.scatter(total[169], run2[169], color = 'r', s = 15)
plt.plot(total, yt3fit, color = 'k')
plt.xlabel("total (mins)")
plt.ylabel("run2 (mins)")




plt.savefig("duathlon_analysis")
plt.show()






















