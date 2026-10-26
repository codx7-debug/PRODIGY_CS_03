# Password Complexity Checker

## About the Project
A simple Python program that checks password complexity based on several basic security requirements. It helps users understand whether their password meets minimum complexity rules.

## Features
- Checks whether the password contains at least 8 characters.
- Checks for at least one uppercase letter.
- Checks for at least one lowercase letter.
- Checks for at least one special character.
- Evaluates password strength as **Weak**, **Moderate**, or **Strong** based on the number of requirements met.

## Technologies Used
- Python 3
- Python standard library (`time` module)

## How to Run

1. Install Python 3 if it is not already installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/codx7-debug/PRODIGY_CS_03.git
   ```

3. Navigate to the project directory:

   ```bash
   cd PRODIGY_CS_03
   ```

4. Run the program:

   ```bash
   python PassWordChecker.py
   ```

## Password Requirements
| Requirement | Description |
|---|---|
| Length | At least 8 characters |
| Uppercase | At least one uppercase letter (A–Z) |
| Lowercase | At least one lowercase letter (a–z) |
| Special character | At least one character from `!@#$%&*` |

## Learning Objectives
- Practice Python functions and conditional statements.
- Use built-in string methods to validate input.
- Work with generators and the `any()` function.
- Learn basic Git and GitHub workflow.

## Disclaimer
This project checks basic password complexity rules only. It does not estimate real-world resistance to password guessing and should not be used as a complete password-security solution.
