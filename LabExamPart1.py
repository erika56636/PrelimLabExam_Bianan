class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.students = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_students = [None] * new_capacity

        for index in range(self.size):
            new_students[index] = self.students[index]

        self.students = new_students
        self.capacity = new_capacity

        print(f"Array capacity increased to {self.capacity}.")

    def add(self, student):
        if self.size == self.capacity:
            self.resize()

        self.students[self.size] = student
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return None

        return self.students[index]

    def set(self, index, student):
        if index >= 0 and index < self.size:
            self.students[index] = student

    def search(self, student_id):
        for index in range(self.size):
            if self.students[index].student_id.lower() == student_id.lower():
                return index

        return -1

    def remove(self, student_id):
        index = self.search(student_id)

        if index == -1:
            return False

        for position in range(index, self.size - 1):
            self.students[position] = self.students[position + 1]

        self.students[self.size - 1] = None
        self.size -= 1

        return True

    def display(self):
        if self.size == 0:
            print("No student records found.")
            return

        print("\n========== STUDENT RECORDS ==========")

        for index in range(self.size):
            print(f"\nStudent {index + 1}")
            self.students[index].display()


def read_non_empty_string(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty.")


def read_integer(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter a valid number.")


def read_positive_integer(message):
    while True:
        number = read_integer(message)

        if number > 0:
            return number

        print("Please enter a positive number.")


def display_menu():
    print("================================")
    print("     STUDENT RECORD MANAGER")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")


def add_student(student_records):
    print("\n========== ADD STUDENT ==========")

    student_id = read_non_empty_string("Enter Student ID: ")

    if student_records.search(student_id) != -1:
        print("Student ID already exists.")
        return

    student_name = read_non_empty_string("Enter Student Name: ")
    course = read_non_empty_string("Enter Course: ")
    year_level = read_positive_integer("Enter Year Level: ")

    new_student = Student(student_id, student_name, course, year_level)
    student_records.add(new_student)

    print("Student added successfully.")


def search_student(student_records):
    print("\n========== SEARCH STUDENT ==========")

    student_id = read_non_empty_string("Enter Student ID to search: ")
    index = student_records.search(student_id)

    if index == -1:
        print("Student not found.")
    else:
        print("\nStudent found:")
        student_records.get(index).display()


def update_student(student_records):
    print("\n========== UPDATE STUDENT ==========")

    student_id = read_non_empty_string("Enter Student ID to update: ")
    index = student_records.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    student = student_records.get(index)

    print("\nCurrent Information:")
    student.display()

    new_name = read_non_empty_string("\nEnter new Student Name: ")
    new_course = read_non_empty_string("Enter new Course: ")
    new_year_level = read_positive_integer("Enter new Year Level: ")

    student.student_name = new_name
    student.course = new_course
    student.year_level = new_year_level

    student_records.set(index, student)

    print("Student updated successfully.")


def remove_student(student_records):
    print("\n========== REMOVE STUDENT ==========")

    student_id = read_non_empty_string("Enter Student ID to remove: ")

    if student_records.remove(student_id):
        print("Student removed successfully.")
    else:
        print("Student not found.")


def display_array_information(student_records):
    print("\n========== ARRAY INFORMATION ==========")
    print(f"Current number of students: {student_records.size}")
    print(f"Current array capacity: {student_records.capacity}")


def main():
    student_records = DynamicArray()

    while True:
        display_menu()
        choice = read_integer("Enter your choice: ")

        if choice == 1:
            add_student(student_records)

        elif choice == 2:
            student_records.display()

        elif choice == 3:
            search_student(student_records)

        elif choice == 4:
            update_student(student_records)

        elif choice == 5:
            remove_student(student_records)

        elif choice == 6:
            display_array_information(student_records)

        elif choice == 7:
            print("Exiting Student Record Manager...")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.")

        print()


if __name__ == "__main__":
    main()