# BeatBlitz Award Management System

The **BeatBlitz Award Management System** is a Python-based application designed to streamline the process of managing awards, nominations, and recipients. It provides an efficient way to handle award-related data and automate workflows.

---

## Features

### Voter Module
- **Sign Up**: Create an account with a username and password (minimum 8 characters).
- **Sign In**: Log in securely with password validation (maximum 3 attempts).
- **Vote**: 
  - Vote for award categories:
    - **Song of the Year**
    - **Best Music Video**
    - **Album of the Year**
  - Each user can vote only once per category.
- **Suggestions**: Submit feedback or suggestions, stored in a CSV file.

### Admin Module
- **Sign In**: Admins can log in securely (maximum 3 attempts).
- **Manage Awards**:
  - Add, edit, or delete award categories.
  - View all award categories and their details.
- **View Results**: Access voting results and statistics.

### Results Visualization
- Voting results are displayed as pie charts for better clarity and engagement.

---

## Technologies Used

- **Python**: Core programming language.
- **MySQL**: Database for storing user credentials, admin credentials, and award details.
- **Matplotlib**: For visualizing voting results as pie charts.
- **Pillow**: For displaying images during the voting process.
- **Tabulate**: For displaying tabular data in a readable format.
- **CSV**: For storing user suggestions.

---

## Prerequisites

- Python 3.x installed on your system.
- MySQL database set up with the required tables.

---

## Setup Instructions

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up the MySQL database:
   - Create a database named `Project`.
   - Add the required tables (`Credentials`, `Admin`, `Song_of_the_Year`, etc.) as per the application's requirements.
5. Run the application:
   ```bash
   python project.py
   ```

## Usage

1. Launch the application.
2. Choose between Admin and Voter options.
3. Follow the on-screen instructions to manage awards, vote, or view results.

## File Structure

- `project.py`: Main application file.
- `welcome.txt`: Welcome message displayed at the start of the program.
- `thankyou.txt`: Thank-you message displayed at the end of the program.
- `instructions.txt`: Instructions for using the application.
- `suggestions.csv`: Stores user suggestions.
- `README.md`: Project documentation.

## Author

Created by **C.V. Akshaya** as part of a Grade 12 project.