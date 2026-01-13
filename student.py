def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")

    m1 = int(input("Enter marks in Subject 1: "))
    m2 = int(input("Enter marks in Subject 2: "))
    m3 = int(input("Enter marks in Subject 3: "))

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("\n----- Student Report -----")
    print("Name       :", name)
    print("Department :", dept)
    print("Semester   :", sem)
    print("Marks      :", m1, m2, m3)
    print("Average    : {:.2f}".format(avg))
    print("Grade      :", grade)
    print("--------------------------")


if __name__ == "__main__":
    main()