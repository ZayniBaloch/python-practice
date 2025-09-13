num_Students = int(input("Enter the number of students: "))  

names = []
grades_list = []
averages = []

for i in range(num_Students): 
    name = input(f"\nEnter name for student #{i+1}: ")
    grades_str = input(f"Enter grades for {name} (comma separated): ")
    grades = [int(g.strip()) for g in grades_str.split(",")]
    names.append(name)
    grades_list.append(grades)

for grades in grades_list:
    total = 0
    for grade in grades:
        total += grade
    avg = total / len(grades)
    averages.append(avg)

print("\n--- Student Grade Report --")
for i in range(num_Students):
    print(f"\nName: {names[i]}")
    print(f"Grades: {grades_list[i]}")
    print(f"Average: {averages[i]:.2f}")
    status = "PASS" if averages[i] >= 60 else "FAIL"
    print(f"Status: {status}")

class_total = 0
for avg in averages:
    class_total += avg
class_average = class_total / num_Students
print(f"\nOverall Class Average: {class_average:.2f}")