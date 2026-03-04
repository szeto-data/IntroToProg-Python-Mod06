# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Andrew Szeto,03/03/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
file = None  # Holds a reference to an opened file.


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    Andrew Szeto,3.3.2026,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads a JSON file and returns a list of dictionaries containing students

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param file_name: String indicating the file name
        :param student_data: The student table which is a list of dictionaries containing students
        :return: The student table which is a list of dictionaries containing students
        """
        file = None

        # When the program starts, read the file data into a list of lists (table)
        # Extract the data from the file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages(message="Error: Text file must exist before running this script.", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
            IO.output_error_messages(message="Please check that the file exists and that it is in a JSON format.")
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes a JSON file from the list of dictionaries containing students

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param file_name: String indicating the file name
        :param student_data: The student table which is a list of dictionaries containing students
        :return: None
        """
        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            print()
            print("-" * 50)
            print("The following data was saved to file!")
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with writing to the file.", error=e)
            IO.output_error_messages(message="Please check that the file is not open by another program.")
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Andrew Szeto,3.3.2026,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param message: Message output to be printed
        :param error: Error information
        :return: None
        """
        print()
        print("-" * 50)
        print(message, end="\n")
        print("-" * 50)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param menu: String containing the output menu
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :return: String with the menu choice
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(message=e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param student_data: The student table which is a list of dictionaries containing students
        :return: The student table which is a list of dictionaries containing students
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Error: There was a problem with your entered value.", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the student information to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,3.3.2026,Created function

        :param student_data: The student table which is a list of dictionaries containing students
        :return: None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        for student in student_data:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        print("-" * 50)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please choose only 1, 2, 3, or 4")

print("Program Ended")
