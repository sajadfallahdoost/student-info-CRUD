import psycopg2
from config import Config


class DatabaseConnection:
    """Singleton class to manage the PostgreSQL database connection."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        """Creates and returns a PostgreSQL connection."""
        return psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )

    def get_connection(self):
        """Returns the database connection."""
        return self.connection
