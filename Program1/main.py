def parse_file(filePath):
    """Parses the given file then
    returns a list of students:
    [ ['87', 'B345', 'Pocahontas'],
      [ '78', 'B999', 'Grace', 'Allen' ] ]"""

    # Open the file, then split into an array of lines (one student per line)
    inputLines = open(filePath, 'r').read().splitlines()

    # Remove any duplicated students
    inputLines = remove_duplicates(inputLines)

    # Split the student information via spaces
    return list(map(lambda x: x.split(' '), inputLines))


def remove_duplicates(arr):
    """Removes duplicate elements within an array."""

    clean_arr = []
    for el in arr:
        if set(el) not in [set(x) for x in clean_arr]:
            clean_arr.append(el)
    return clean_arr


def group_students(students):
    """Group students based on their numeric grade:
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
    the leaderboard as a string."""

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


def generate_leaderboard(leaderboard):
    """Formats the leaderboard into a table."""

    output = 'RANK\tID #\t\tFIRST\t\tLAST\n'
    output += '=' * 47
    output += '\n' + leaderboard + '\n'
    return output

def count_matching(condition, seq):
    """Returns the amount of items in seq that return true from condition"""
    return sum(1 for item in seq if condition(item))

def generate_chart(studentDict):
    """Generates a bar chart of student grades."""

    # Should filter studentDict into number of occurrences of grade ranges.
    gradeOccurrences = list(map(lambda x: [x, studentDict[x][0]], studentDict))
    output = ''

    for high in range(100, 0, -5):
        low = high - 4
        output += str(high) + ' - ' + str(high - 4) + ':\t'
        output += 'X' * count_matching(lambda x: high >= x[0] >= low, gradeOccurrences)
        output += '\n'

    return output

# Parse the file into a list of students
students = parse_file('indataP1.txt')

# Group students using numeric grade
studentDict = group_students(students)

# Rank students by grade
rankedStudents = rank_students(studentDict)

# Format and print the student leaderboard
# print(generate_leaderboard(rankedStudents))

# Generate and print the bar chart
print(generate_chart(studentDict))
