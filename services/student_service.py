from models.student import Student
from services.database import DatabaseConnection
from typing import Optional


class StudentService:
    """
    Service layer to handle business logic and data persistence for students.
    """

    def __init__(self) -> None:
        self.db_conn = DatabaseConnection().get_connection()

    def add_student(self, student: Student) -> None:
        """Adds a new student to the database."""
        with self.db_conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO students (name, last_name, gender, dob, degree, reg_date, grad_date, address, contact_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (student.name, student.last_name, student.gender, student.dob, student.degree,
                student.reg_date, student.grad_date, student.address, student.contact_number))
        self.db_conn.commit()

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """Fetch a student by ID from the database."""
        with self.db_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            result = cursor.fetchone()
            if result:
                return Student(*result)
        return None

    def update_student(self, student_id: int, updated_data: dict) -> None:
        """Update student information."""
        query = "UPDATE students SET " + ", ".join([f"{key} = %s" for key in updated_data]) + " WHERE id = %s"
        with self.db_conn.cursor() as cursor:
            cursor.execute(query, (*updated_data.values(), student_id))
        self.db_conn.commit()

    def remove_student(self, student_id: int) -> None:
        """Removes a student from the database."""
        with self.db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.db_conn.commit()
