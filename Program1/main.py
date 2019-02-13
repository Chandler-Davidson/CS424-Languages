def remove_duplicates(arr):
    """Removes duplicate elements within an array."""

    clean_arr = []
    for el in arr:
        if set(el) not in [set(x) for x in clean_arr]:
            clean_arr.append(el)
    return clean_arr

def groupStudents(students):
    """Group students based on numeric grade.
    This function will return in the following format:
        {'87': [2, ('B345', 'Pocahontas'), ('B456', 'Sally', 'Sharp')]}"""

    # Student directory data structure
    combinedStudents = {}

    ## Group students by numeric grade
    for student in students:
        sameStudents = list(filter(lambda x: x[0] == student[0], students))
        studentInfo = list(map(lambda x: x[1], sameStudents))
        combinedStudents[student[0]] = [len(studentInfo)] + studentInfo[:]

    return combinedStudents

# Open the file, then split into an array of lines (one student per line)
inputLines = open("indataP1.txt", "r").read().splitlines()

# Remove any duplicated students
inputLines = remove_duplicates(inputLines)

# Split the student information via spaces
students = list(map(lambda x: x.split(' '), inputLines))

# Restructure the student info into: [Grade, (ID, First, Last)] 
students = list(map(lambda x: [x[0], tuple(x[1:])], students))

# Group students using numeric grade
groupedStudents = groupStudents(students)

print(groupStudents)
