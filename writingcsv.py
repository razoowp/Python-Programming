import csv

students = [["Kedar", 23, 21], ["hari", 21, 34], ["krr", 33, 75]]

with open("example.csv", "a", newline='') as f:
    write_csv = csv.writer(f)
   # write_csv.writerow(["raju", 123, 12])
    write_csv.writerows(students)
