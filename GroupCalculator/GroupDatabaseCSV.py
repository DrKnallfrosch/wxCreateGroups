from GroupCalculator.GroupInterface import GroupInterface
from GroupCalculator.Student import Student
import configparser
import random
import csv

class GroupDatabaseCSV(GroupInterface):
    """
    A class to manage group assignments, supporting both CSV input and manual student lists.
    """

    def __init__(self, group_size: int):
        if group_size < 1:
            raise ValueError("Group size must be at least 1.")
        self.group_size = group_size
        self.students = []  # List of students
        self.groups = {}  # Dictionary to store groups per round
        self.current_round = 1
        self.config = configparser.ConfigParser()

    def add_students(self, students: list[str]) -> None:
        """
        Manually add students to the system.

        :param students: A list of student names.
        """
        if not students:
            raise ValueError("Student list cannot be empty.")
        self.students = students

    def select_from_file(self, file_path: str) -> None:
        """
        Loads student names from a CSV file and allows the user to select a column.

        :param file_path: Path to the CSV file.
        """
        self.config.read('../config.ini')
        header = self.config.getboolean('CSV file', 'header')
        delimiter = self.config['CSV file']['delimiter']
        delimiter = delimiter.replace('"', '')

        name = self.config.getint('columns', 'name')
        lastname = self.config.getint('columns', 'lastname')
        email = self.config.getint('columns', 'email')
        username = self.config.getint('columns', 'username')

        with open(file_path, 'r', encoding="UTF-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=delimiter)
            if header:
                next(reader)
            for row in reader:
                student = Student(name=row[name], last_name=row[lastname], email=row[email], username=row[username])
                self.students.append(student)


    def create_groups(self) -> None:
        """
        Creates groups randomly from the student list.
        """
        if not self.students:
            raise ValueError("No students available. Add students manually or load from CSV.")

        random.shuffle(self.students)
        num_groups = len(self.students) // self.group_size
        remainder = len(self.students) % self.group_size

        group_labels = [chr(65 + i) for i in range(num_groups + (1 if remainder > 0 else 0))]  # A, B, C, ...

        self.groups[self.current_round] = {}
        index = 0
        for label in group_labels[:-1] if remainder > 0 else group_labels:
            self.groups[self.current_round][label] = self.students[index:index + self.group_size]
            index += self.group_size

        # If there are remaining students, place them in a separate smaller group
        if remainder > 0:
            self.groups[self.current_round][group_labels[-1]] = self.students[index:]

        self.current_round += 1

    def visualise_groups(self) -> dict[int, dict[str, list[Student]]]:
        return self.groups

    def get_current_groups(self) -> dict[int, dict[str, list[Student]]]:
        return {self.current_round - 1: self.groups.get(self.current_round - 1, {})}

    def get_all_groups(self) -> dict[int, dict[str, list[Student]]]:
        return self.groups

    def reset_group(self) -> None:
        """
        Resets all group assignments.
        """
        self.groups.clear()
        self.current_round = 1

    def can_repeat(self) -> int:
        """
        Returns the maximum number of unique group arrangements possible.
        """
        num_groups = len(self.students) // self.group_size
        return max(1, num_groups)

if __name__ == "__main__":
    a = GroupDatabaseCSV(4)  # Group size of 3
    a.select_from_file("../dqi_user.csv")
    a.create_groups()
    print(a.get_all_groups())