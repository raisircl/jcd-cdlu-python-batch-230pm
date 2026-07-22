with open("student_notes.txt", "r") as file:
    data = file.read()

print(data)

# No need to write file.close() manually
'''
with automatically closes the file.
Code becomes shorter and safer.
Use with in real projects whenever possible.

'''