grades = []
passing_grade = 75

while True:
    user_input = input("Enter a grade (or type 'done' to stop): ").strip()
    
    if user_input.lower() == 'done': 
        break
    
    if user_input == '' or user_input.count('.') > 1:
        print("Incorrect Data. Please enter a valid number.")
        continue

    grade = user_input
    is_valid = True

    for char in grade:
        if char not in "0123456789.":
            is_valid = False
            break

    if is_valid:
        grade = float(grade)
        if 0 <= grade <= 100:
            if grade < 40:
                break
            
            else:
                grades.append(grade)
        else:
            print("Incorrect Data. Please enter a number between 0 and 100.")
    else:
        print("Incorrect Data. Please enter a valid number.")

if grades:
    total = sum(grades)
    average = total / len(grades)

    print("\nGrades entered:", grades)
    print(f"Total of grades: {total}")
    print(f"Average grade: {average:.2f}")
    
    if average >= passing_grade:
        print("Status: You Have Passed")
    else:
        print("Status: You Have Failed")