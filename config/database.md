CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    dob DATE NOT NULL,
    degree VARCHAR(100) NOT NULL,
    reg_date DATE NOT NULL,
    grad_date DATE,
    address TEXT,
    contact_number VARCHAR(15) NOT NULL
);
