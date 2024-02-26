grades = []
for i in range(0,2):
    grades.append(float(input("Enter the grade: ")))

print("The average is: ", sum(grades)/len(grades))
