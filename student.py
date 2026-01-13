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
    name = "veeresh"
    dept = "BCA"
    sem = 3

    m1 = 80
    m2 = 80
    m3 = 80

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
