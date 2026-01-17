# Operating Systems Lab Project

## Project Title

**Banker’s Algorithm & Deadlock Detection Simulator**

## University

**DHA Suffa University, Karachi**

## Course

Operating Systems Lab

## Project Description

This project is a desktop-based simulation tool developed to demonstrate **deadlock avoidance and deadlock detection** concepts in Operating Systems.

The application provides two major modules:

**1. Banker’s Algorithm Module**
This module implements Banker’s Algorithm to determine whether a system is in a safe or unsafe state. Users can input:

* Number of processes and resources
* Allocation matrix
* Maximum demand matrix
* Available resources

Based on the inputs, the system calculates the **Need matrix**, evaluates all possible execution sequences, and displays whether the system is safe along with the **safe sequence of processes**.

**2. Deadlock Detection Module**
This module detects deadlock situations by analyzing:

* Allocation matrix
* Request matrix
* Available resources

The algorithm checks which processes can complete execution and identifies **deadlocked processes**, if any.

The project uses a graphical user interface built with **Tkinter**, allowing dynamic input generation and clear visualization of results, making it suitable for lab demonstrations and academic evaluation.

## Features

* Interactive graphical user interface (GUI)
* Dynamic input field generation
* Safe state detection with safe sequence
* Deadlock detection with identification of affected processes
* Clear success and error messages

## Technologies Used

* Python 3
* Tkinter (GUI Framework)
* ttk Styling

## How to Run the Project

1. Make sure Python 3 is installed on your system
2. Save the project file as `main.py`
3. Open a terminal in the project directory
4. Run the command:

   ```bash
   python main.py
   ```

## Input Format Guidelines

* Enter matrix values as space-separated integers
* Ensure the number of values matches the number of resources
* Provide valid numeric input to avoid errors

## Group Members

* **[Hirtik Kumar](https://github.com/Hirtik786)**
* **[Hania Fatima](https://github.com/haniak855-tech)**
* **Sunesh Kumar**
* **Mohit Kumar**
* **Chanchal**

## Acknowledgment

This project is developed as part of the **Operating Systems Lab** coursework at DHA Suffa University under the guidance of the respective course instructor.
