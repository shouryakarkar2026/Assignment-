# Create student records dictionary
# Key = Roll Number, Value = [Name, Branch, (Marks Tuple)]
students = {
    1: ["arun", "CS", (85, 90, 88)],
    2: ["dhairya", "IT", (75, 80, 82)],}


new_details = ("ishan", "Mechanical")
students[3] = [new_details[0], new_details[1], (90, 92, 95)]
print("Added student 3.")


del students[2]
print("Deleted student 2.")

students[1][1] = "Data Science"  # Update branch
print("Updated student 1.")


print("\n--- FINAL RECORDS ---")
print("Student 1:", students[1])
print("Student 3:", students[3])




