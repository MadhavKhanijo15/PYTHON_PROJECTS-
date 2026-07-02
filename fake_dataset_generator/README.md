# **Fake Dataset Generator**

## Video Demo: [Video link](https://youtu.be/7xbcnm4z6kU)

## Description: A lightweight Python-based command-line tool for generating realistic fake datasets in CSV format. It is designed for testing, learning, prototyping, and validating data analysis workflows without requiring real-world data.

## Overview

Fake Dataset Generator allows users to instantly create structured datasets through a simple command-line interface. The project currently supports two predefined dataset templates and exports the generated data directly as CSV files.

This tool can be useful for:

- Testing data analysis software
- Practicing data cleaning and preprocessing
- Building data visualization projects
- Demonstrating database operations
- Academic and learning purposes

## Features
- Command-line based interface
- Instant CSV dataset generation
- Multiple dataset templates
- User-defined dataset size
- Lightweight implementation using Python standard libraries

## Available Templates
1. Student Database
Generates a dataset containing student-related information such as:
- Student_id
- Name
- Age
- Weight
- Height
- BMI  
and other automatically generated student records.

2. Office Employees Database
Generates a dataset containing employee-related information such as:
- Employee_id
- Name
- Age
- Department
- Salary
- Joining_year
and other automatically generated employee records.

## How It Works
1. Run the program.
2. Choose a dataset template:
 1 → Student Database
 2 → Office Employees Database
3. Enter the number of records required.
4. The program automatically generates the dataset.
5. A CSV file is created instantly and saved locally.

## Example Workflow
Select Dataset Type

1 - Student Database
2 - Office Employees Database

Enter Choice: 1

Enter Number of Students: 25

Dataset Generated Successfully!
File Saved: students.csv

Output

The generated dataset is exported as a standard .csv file, making it compatible with:

- Microsoft Excel
- Google Sheets
- Python Pandas
- SQL import tools
- Business Intelligence software
- Data visualization platforms

## Technologies Used
- Python
- CSV Module
- Random Module

## Inspiration

While libraries such as Faker already exist for synthetic data generation, this project follows a different approach focused on simplicity, predefined templates, and immediate CSV export through an interactive command-line experience.

The goal is to provide a beginner-friendly and lightweight solution that can quickly generate structured datasets without requiring external packages or complex configurations.

## Future Improvements

Potential enhancements include:

- Additional dataset templates
- Custom field selection
- User-defined schema creation
- Web-based interface
- Export to JSON and Excel formats
- Advanced randomization controls
- Realistic relationship generation between datasets
