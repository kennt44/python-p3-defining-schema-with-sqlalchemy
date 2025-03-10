#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Create a base class using declarative_base
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'  # Define the name of the table

    id = Column(Integer, primary_key=True)  # Define the primary key
    name = Column(String)  # Define the name column

# Add the script to create the database schema
if __name__ == '__main__':
    # Set up the engine to point to an SQLite database
    engine = create_engine('sqlite:///students.db')

    # Create all the tables defined by models inheriting from Base (Student in this case)
    Base.metadata.create_all(engine)
