# Advanced Python Calculator for Software Engineering Graduate Course

## Summary
* This is a Calculator class with a REPL on top to allow direct user engagement. The core of it lives in calculator/calculator.py which brings together a handful of other objects. Higstory is used within the calculator to track and manipulate the storage of past calculations. Input_cleaner is used to ingest strings from the user in a way to capture user inputs appropriately. A function is used to load commands from a /commands/ folder.

## Details
* The [Command Design pattern](https://github.com/TyHys/IS601-Midterm-Spring2024/tree/ac65c3046dce1c641f598ed3cfe35e1d3a597823/commands) was used when developing the primary interface of this application by using a 'commands' filter with a plugin architecture to load individual commands. 
* A [facade pattern](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/ac65c3046dce1c641f598ed3cfe35e1d3a597823/input_cleaner/input_cleaner.py) was used in building the input cleaning process, such that the operation could run successfully.

* [An environment variable](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/ac65c3046dce1c641f598ed3cfe35e1d3a597823/main.py#L25C12-L25C21) was used to help debug to return additional information while running. This enables the user to have a dynamic feedback with additional information about how their input is being ingested into the application.
* [Logging was used](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/ac65c3046dce1c641f598ed3cfe35e1d3a597823/main.py#L20-L93) throughout the main.py application to capture any initiation, termination, or issues with the application. Logging is used throughout the main.py file so that as a user natrually interacts with the calculator, interactions are logged into a dated log file. In addition, a warning is logged if no DEBUG_MODE key appears in the .env file.
* "Look Before You Leap" (LBYL) [Example 1](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/faffa9dfd5f84a6d07c93aa9d42e2f61698ad48e/main.py#L52-L53) | [Example 2](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/faffa9dfd5f84a6d07c93aa9d42e2f61698ad48e/history/history.py#L69) | [Example 3](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/faffa9dfd5f84a6d07c93aa9d42e2f61698ad48e/history/history.py#L103) was used throughout the program to perform checks prior to code execution, such that errors could be minimized or entirely eliminated. 
* "Easier to Ask for Forgiveness than Permission" (EAFP): [Example 1](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/faffa9dfd5f84a6d07c93aa9d42e2f61698ad48e/main.py#L64-L89) | [Example 2](https://github.com/TyHys/IS601-Midterm-Spring2024/blob/faffa9dfd5f84a6d07c93aa9d42e2f61698ad48e/history/history.py#L82-L91) is used throughout the program to try process user inputs by attempting code, and catching errors to be sent for logging if it is unable to do so.

## Installation

* Clone the git repository
* Create a new python3 virtual environment.
* Install requirements from requirements.txt
* Execute main.py via "python3 main.py"
