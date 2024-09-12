from typing import Optional
from datetime import date


class Student:
    """
    Student model to represent the data fields of a student.
    """
    def __init__(self,
                student_id: int,      
                name: str,
                last_name: str,
                gender: str,
                dob: date,
                degree: str,
                reg_date: date,
                grad_date: Optional[date],
                address: str,
                contact_number: str) -> None:
        self.student_id = student_id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.degree = degree
        self.reg_date = reg_date
        self.grad_date = grad_date
        self.address = address
        self.contact_number = contact_number

    def __repr__(self) -> str:
        return f"<Student {self.student_id}: {self.name} {self.last_name}>"
