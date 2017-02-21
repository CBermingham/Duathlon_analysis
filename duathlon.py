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
t1 = []
t2 = []

f = open("chilly_duathlon.csv", 'rU')
next(f)
reader = csv.reader(f, None) 
for row in reader:
    list1.append(str(row[14]))
    list2.append(str(row[17]))
    list3.append(str(row[20]))
    total.append(str(row[6]))
    gender.append(str(row[9]))
    t1.append(str(row[16]))
    t2.append(str(row[19]))
f.close()


list1 = [list1[i] for i in range(0, len(total)) if total[i] != "DNF"]
list2 = [list2[i] for i in range(0, len(total)) if total[i] != "DNF"]
list3 = [list3[i] for i in range(0, len(total)) if total[i] != "DNF"]
total = [total[i] for i in range(0, len(total)) if total[i] != "DNF"]
gender = [gender[i] for i in range(0, len(total)) if total[i] != "DNF"]
t1 = [t1[i] for i in range(0, len(total)) if total[i] != "DNF"]
t2 = [t2[i] for i in range(0, len(total)) if total[i] != "DNF"]


run1 = [(60*float(list1[i][:2]) + float(list1[i][3:5]))/60.0 for i in range(0, len(list1))]
ride = [(60*float(list2[i][:2]) + float(list2[i][3:5]))/60.0 for i in range(0, len(list2))]
run2 = [(60*float(list3[i][:2]) + float(list3[i][3:5]))/60.0 for i in range(0, len(list3))]
total = [(60*float(total[i][:2]) + float(total[i][3:5]))/60.0 for i in range(0, len(total))]

t1_new = []
for i in range(0, len(t1)):
	if ":" not in t1[i]:
		t1_new.append(float(t1[i][:2])/60.0)
	else:
		t1_new.append((float(t1[i][:2])*60 + float(t1[i][3:5]))/60.0)
t1 = t1_new

t2_new = []
for i in range(0, len(t2)):
	if ":" not in t2[i]:
		t2_new.append(float(t2[i][:2])/60.0)
	else:
		t2_new.append((float(t2[i][:2])*60 + float(t2[i][3:5]))/60.0)
t2 = t2_new

total_new = []
for i in total:
	if i < 40:
		total_new.append(i + 60)
	else:
		total_new.append(i)
total = total_new

splits = []
split_totals = []
for i in range(0, len(total)):
	splits.append([run1[i], t1[i], ride[i], t2[i], run2[i]])
	split_totals.append([run1[i], run1[i] + t1[i], run1[i] + t1[i] + ride[i], run1[i] + t1[i] + ride[i] + t2[i], run1[i] + t1[i] + ride[i] + t2[i] + run2[i]])

differences = []
for i in range(1, len(splits)):
	diff = [(x - y) for x, y in zip(split_totals[0], split_totals[i])]
	differences.append(diff)

split_totals = [[0] + i for i in split_totals]
differences = [[0] + i for i in differences]
markers = [(split_totals[0][i]+ split_totals[0][i+1])/2 for i in range(0, len(split_totals[0])-1)]

plt.plot(split_totals[0], [0, 0, 0, 0, 0, 0])
for i in range(0, 50):
	plt.plot(split_totals[0], differences[i])
plt.plot(split_totals[0], differences[169], linewidth = 5)
plt.xlim(xmin = 0)
plt.yticks([2, 0, -2, -4, -6, -8, -10, -12, -14], [-2, 0, 2, 4, 6, 8, 10, 12, 14])
plt.ylabel("Time behind winner (mins)")
plt.xticks(markers, ["Run 1", "T1", "Ride", "T2", "Run2"])
plt.savefig("Split_analyser")
plt.show()
plt.clf()



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






#plt.savefig("duathlon_analysis")
#plt.show()
























