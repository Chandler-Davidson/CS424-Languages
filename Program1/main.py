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


def save_to_file(contents, filePath):
    """Saves the contents to the given file path"""
    open(filePath, 'w').write(contents)


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
        try:
            # Select students that have matching grade
            sameStudents = list(filter(lambda x: x[0] == student[0], students))

            # Map each to student to only their (ID#, First, Last)
            studentIDs = list(map(lambda x: tuple(x[1:]), sameStudents))

            # Add students to the dictionary using the numeric grade as the key
            studentDict[int(student[0])] = [len(studentIDs)] + [studentIDs]
        except:
            print('There was an error parsing the following student: ' + str(student))

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
            # Capture the name
            name = student[1:]
            leaderboard += ' '.join(name)

            # Apply appropriate spacing
            if (len(name) == 2):
                leaderboard += '\t' * 1
            else:
                leaderboard += '\t' * 2

            # Add the remainder of student information
            leaderboard += student[0] + '\t' + str(grade) + '\t' + str(currentRank) + '\n'
        currentRank += len(students)
    return leaderboard


def generate_leaderboard(leaderboard):
    """Formats the leaderboard into a table."""

    output = 'NAME\t\tID\tGRADE\tRANK\n'
    output += '=' * 37
    output += '\n' + leaderboard
    return output


def count_matching(condition, seq):
    """Returns the amount of items in seq that return true from condition"""
    return sum(item[1] for item in seq if condition(item))


def generate_chart(studentDict):
    """Generates a bar chart of student grades."""

    # Should filter studentDict into number of occurrences of grade ranges.
    gradeOccurrences = list(map(lambda x: [x, studentDict[x][0]], studentDict))
    output = ''

    output += '100 - 95: ' + 'X' * \
        count_matching(lambda x: 100 >= x[0] >= 95, gradeOccurrences)
    output += '\n'

    for high in range(94, 64, -5):
        low = high - 4
        output += ' ' + str(high) + ' - ' + str(low) + ': '

        output += 'X' * \
            count_matching(lambda x: high >= x[0] >= low, gradeOccurrences)
        output += '\n'

    output += ' 60 -  0: '
    output += 'X' * count_matching(lambda x: 60 >= x[0] >= 0, gradeOccurrences)
    output += '\n'

    return output


# Print program introduction
print('This program is written to take in a file of student\n' +
      'information and grades in the following format:\n\t' +
      '<grade> <id#> <name>\n\t<grade> <id#> <name>\n' +
      'After interpretting the input data, this program will\noutput' +
      'a bar chart of grade intervals and occurrences\nas well as a final grade report.\n\n\n')

# Parse the file into a list of students
students = parse_file('indataP1.txt')

# Group students using numeric grade
studentDict = group_students(students)

# Rank students by grade
rankedStudents = rank_students(studentDict)

# Format and print the student leaderboard
leaderboard = generate_leaderboard(rankedStudents)

# Generate and print the bar chart
chart = generate_chart(studentDict)

# Print the results to the screen
print('STUDENT GRADE CHART:\n' + chart)
print('STUDENT GRADE LEADERBOARD:\n' + leaderboard)

# Sae the results to separate files
save_to_file(chart, 'barchart.txt')
save_to_file(leaderboard, 'sorted.txt')
