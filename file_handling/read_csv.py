with open("students.csv", "r") as file:
    header = file.readline().strip().split(",")

    print(header)
    for h in header:
        print("%10s | " %(h), end="")
    print()

    for line in file:
        data = line.strip().split(",")
        student_id = data[0]
        name = data[1]
        attendance = data[2]
        marks = data[3]

        print("%10s | %10s | %10s | %10s |" % (student_id, name, attendance, marks))
