class Student:
        def __init__(self, **kwargs):
            """
            Initialize a Student object.

            :param kwargs: Dictionary of keyword arguments containing student attributes.
            :key name: The first name of the student (str).
            :key last_name: The last name of the student (str).
            :key email: The email address of the student (str).
            :key user_name: The username of the student (str).
            """
            self.name = self._validator_str(kwargs.get('name') or "")
            self.last_name = self._validator_str(kwargs.get('last_name') or "")
            self.email = self._validator_str(kwargs.get('email') or "")
            self.username = self._validator_str(kwargs.get('username') or "")

        @staticmethod
        def _validator_str(__name: str) -> str:
            """
            Validate that the input is a string.

            :param __name: The input to validate.
            :type __name: str
            :raises ValueError: If the input is not a string.
            :return: The validated string.
            :rtype: str
            """
            if type(__name) is not str:
                raise ValueError("It must be a string")
            return __name

        def __repr__(self):
            """
            Return a string representation of the Student object.

            :return: A string containing the student's name, last name, email, and username.
            :rtype: str
            """
            return f"Student(name={self.name}, last_name={self.last_name}, email={self.email}, username={self.username})"

        def __str__(self):
            """
            Return a string representation of the Student object.

            :return: A string containing the student's name, last name, email, and username.
            :rtype: str
            """
            return f"{self.name} {self.last_name}"

if __name__ == "__main__":
    student = [Student(name="John", last_name="Doe", email=""), Student(name="Jane", last_name="Smith", email=""), Student(name="Alice", last_name="Brown", email="")]
    print(student[0])
