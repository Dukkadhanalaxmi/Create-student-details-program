name = input("Enter student name : ")
roll_no = input("Enter roll number : ")
branch = input("Enter branch : ")
age = int(input("Enter age : "))
marks = float(input("Enter marks : "))
if marks >= 35:
    result = "PASS"
else:
    result = "FAIL"


print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_no)
print("Branch:", branch)
print("Age:", age)
print("Marks:", marks)
print("Result:", result)
