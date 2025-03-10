#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_sandbox import Student  # Import your Student model

# Create an engine that connects to the SQLite database
engine = create_engine('sqlite:///students.db')

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()  # This will pause the script and allow interactive debugging

    # You can now interact with the database within the ipdb shell
    # Example query: Retrieve all students from the table
    students = session.query(Student).all()

    # Print out all the students
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")

    # Make sure to close the session when done
    session.close()
