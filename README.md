Repository Description
This repository contains a simple Python script that demonstrates basic arithmetic operations. The script includes functionality to sum three numbers and compute the factorial of one number. It serves as an introductory example for beginners to understand class creation, methods, and recursion in Python.

Detailed Explanation
Overview
The Basic-Calculations repository contains a Python script (array_01.py) that performs two main operations:

Summing three numbers.
Calculating the factorial of a given number.
Script Breakdown
The script defines a class calculations with the following components:

Initialization (__init__ method):

Takes three arguments a, b, and c and assigns them to instance variables.
Sum Method (sum method):

Returns the sum of the instance variables a, b, and c.
Factorial Method (factorial method):

Computes the factorial of the instance variable b using a helper method cal_factorial.
Helper Method (cal_factorial method):

Recursively calculates the factorial of a given number n.
Usage
To use the script, run it in a Python environment. The script will prompt the user to input three values for a, b, and c. It will then display the sum of these values and the factorial of b.

Example
python
Copy code
if __name__ == "__main__":
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))

    numbers = calculations(a, b, c)

    print("Sum of a, b, and c:", numbers.sum())
    print("Factorial of b:", numbers.factorial())
Running the Script
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/Basic-Calculations.git
Navigate to the directory:
bash
Copy code
cd Basic-Calculations
Run the script:
bash
Copy code
python array_01.py
Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

This repository serves as a practical example for beginners to understand fundamental programming concepts in Python such as class creation, methods, recursion, and basic input/output operations.
