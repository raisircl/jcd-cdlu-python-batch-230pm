try:
    with open("missing_file.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found. Please check file name.")
