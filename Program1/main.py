def remove_duplicates(arr):
    """Removes duplicate elements within an array."""

    clean_arr = []
    for el in arr:
        if set(el) not in [set(x) for x in clean_arr]:
            clean_arr.append(el)
    return clean_arr


def group_students(students):
    """Group students based on numeric grade.
    This function will return in the following format:
        {'87': [2, ('B345', 'Pocahontas'), ('B456', 'Sally', 'Sharp')]}"""

    # Student directory data structure
    studentDict = {}

    # Group students by numeric grade
    for student in students:
        # Select students that have matching grade
        sameStudents = list(filter(lambda x: x[0] == student[0], students))

        # Map each to student to only their (ID#, First, Last)
        studentIDs = list(map(lambda x: tuple(x[1:]), sameStudents))

        # Add students to the dictionary using the numeric grade as the key
        studentDict[int(student[0])] = [len(studentIDs)] + [studentIDs]

    return studentDict


def rank_students(studentDict):
    """Rank students by grade, returning
    a string of the leaderboard."""

    # Sort the student grades
    rankedGrades = sorted(studentDict, reverse=True)
    currentRank = 1
    leaderboard = ''

    # Iterate through student grades
    for grade in rankedGrades:

        # The list of students with the given grade
        students = studentDict[grade][1]

        # Add the student to the leaderboard
        for student in students:
            studentStr = '\t\t'.join(student)
            leaderboard += str(currentRank) + '\t' + studentStr + '\n'
        currentRank += len(students)
    return leaderboard

def generate_chart(studentDict):
    """Generates a bar chart of student grades."""

    # Should filter studentDict into number of occurrences of grade ranges.

    rangesStr = []

    for i in range(100, 0, -5):
        low = i -4
        applicableGrades = len(list(filter(lambda x: x <= i and x >= low, grades)))
        rangesStr.append(str(i) + ' - ' + str(i - 4) + ':\t' + 'X' * applicableGrades)
    return '\n'.join(rangesStr)


# Open the file, then split into an array of lines (one student per line)
inputLines = open('indataP1.txt', 'r').read().splitlines()

# Remove any duplicated students
inputLines = remove_duplicates(inputLines)

# Split the student information via spaces
students = list(map(lambda x: x.split(' '), inputLines))

# Group students using numeric grade
studentDict = group_students(students)

# Rank students by grade
leaderboard = rank_students(studentDict)

# Pretty print the leaderboard
print('RANK\tID#\t\tFIRST\t\tLAST')
print('=' * 47)
print(leaderboard)

print(generate_chart(studentDict))