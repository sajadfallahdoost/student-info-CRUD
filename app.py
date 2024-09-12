from controllers import StudentController
from utils.logger import setup_logger
import jdatetime
from typing import Optional

# Initialize the logger and controller
logger = setup_logger()
controller = StudentController()


def create_student() -> None:
    """Creates a new student with input from the user."""
    try:
        name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        gender = input("Enter student's gender (Male/Female): ")

        # Get and validate date of birth
        dob_input = input("Enter student's date of birth (Persian YYYY-MM-DD): ")
        try:
            dob = jdatetime.date(*map(int, dob_input.split('-'))).togregorian()
        except ValueError:
            logger.error("Invalid date format for DOB. Please use Persian YYYY-MM-DD.")
            return

        # Get and validate registration date
        degree = input("Enter student's degree (e.g., Bachelors, Masters): ")
        reg_date_input = input("Enter registration date (Persian YYYY-MM-DD): ")
        try:
            reg_date = jdatetime.date(*map(int, reg_date_input.split('-'))).togregorian()
        except ValueError:
            logger.error("Invalid date format for registration date. Please use Persian YYYY-MM-DD.")
            return

        # Get and validate optional graduation date
        grad_date_input = input("Enter graduation date (optional, Persian YYYY-MM-DD) or leave blank: ")
        grad_date: Optional[jdatetime.date] = None
        if grad_date_input:
            try:
                grad_date = jdatetime.date(*map(int, grad_date_input.split('-'))).togregorian()
            except ValueError:
                logger.error("Invalid date format for graduation date. Please use Persian YYYY-MM-DD.")
                return

        # Collect other data and create student
        address = input("Enter student's address: ")
        contact_number = input("Enter student's contact number: ")

        student_data = {
            "name": name,
            "last_name": last_name,
            "gender": gender,
            "dob": dob,
            "degree": degree,
            "reg_date": reg_date,
            "grad_date": grad_date,
            "address": address,
            "contact_number": contact_number
        }

        controller.create_student(student_data)
        logger.info(f"Student {name} {last_name} created successfully")

    except Exception as e:
        logger.error(f"Error creating student: {e}")


def read_student() -> None:
    """Fetch and display a student's details by ID."""
    try:
        student_id = int(input("Enter the student ID to read: "))
        student = controller.read_student(student_id)
        if student:
            print(f"Student: {student.name} {student.last_name}, Gender: {student.gender}, DOB: {student.dob}")
        else:
            logger.info(f"Student with ID {student_id} not found")
    except ValueError:
        logger.error("Invalid student ID format. Please enter a valid number.")
    except Exception as e:
        logger.error(f"Error reading student: {e}")


def update_student() -> None:
    """Update a student's information based on input."""
    try:
        student_id = int(input("Enter the student ID to update: "))

        updated_data = {}
        name = input("Enter new name (or leave blank to keep current): ")
        if name:
            updated_data['name'] = name

        last_name = input("Enter new last name (or leave blank to keep current): ")
        if last_name:
            updated_data['last_name'] = last_name

        gender = input("Enter new gender (or leave blank to keep current): ")
        if gender:
            updated_data['gender'] = gender

        if updated_data:
            controller.update_student(student_id, updated_data)
            logger.info(f"Student with ID {student_id} updated successfully")
        else:
            logger.info("No updates provided")
    except ValueError:
        logger.error("Invalid student ID format. Please enter a valid number.")
    except Exception as e:
        logger.error(f"Error updating student: {e}")


def delete_student() -> None:
    """Delete a student by ID with confirmation."""
    try:
        student_id = int(input("Enter the student ID to delete: "))

        student = controller.read_student(student_id)
        if student is None:
            logger.info(f"Student with ID {student_id} does not exist")
            return

        confirmation = input(f"Are you sure you want to delete student with ID {student_id}? (yes/no): ")

        if confirmation.lower() == "yes":
            try:
                # Perform the deletion
                controller.delete_student(student_id)
                logger.info(f"Student with ID {student_id} deleted successfully")
            except Exception as e:
                logger.error(f"Failed to delete student with ID {student_id}: {e}")
        else:
            logger.info("Delete operation canceled")

    except ValueError:
        logger.error("Invalid student ID format. Please enter a valid number.")
    except Exception as e:
        logger.error(f"Error deleting student: {e}")


def run_app() -> None:
    """Main entry point for the application."""
    logger.info("Application started")

    while True:
        print("\nChoose an operation:")
        print("1. Add Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter the operation number: ")

        try:
            if choice == "1":
                create_student()
            elif choice == "2":
                read_student()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                logger.info("Application stopped")
                break
            else:
                print("Invalid choice, please try again")
        except Exception as e:
            logger.error(f"Error during operation: {e}")

if __name__ == "__main__":
    run_app()
