from models.student import Student
from services import StudentService


class StudentController:
    """
    Controller for handling CRUD operations on Student objects.
    """

    def __init__(self) -> None:
        self.student_service = StudentService()

    def create_student(self, student_data: dict) -> None:
        """Creates a new student."""
        student = Student(**student_data)
        self.student_service.add_student(student)

    def read_student(self, student_id: int) -> Student:
        """Fetch a student by ID."""
        return self.student_service.get_student_by_id(student_id)

    def update_student(self, student_id: int, updated_data: dict) -> None:
        """Updates the student information."""
        self.student_service.update_student(student_id, updated_data)

    def delete_student(self, student_id: int) -> None:
        """Deletes a student from the database."""
        self.student_service.remove_student(student_id)
