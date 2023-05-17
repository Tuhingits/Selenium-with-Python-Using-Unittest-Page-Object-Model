# Automated a login module using selenium python with page object model and data driven testing
Automated Login Module using Selenium Python with Page Object Model and Data-Driven Testing is a project that demonstrates how to automate the login functionality of a web application using Selenium WebDriver in Python. The project follows the Page Object Model (POM) design pattern to create reusable and maintainable code. It also incorporates data-driven testing, allowing the same login test to be executed with multiple sets of input data.

By utilizing Selenium WebDriver, the project interacts with the web application's login page, enters the username and password, and submits the form. The Page Object Model design pattern is implemented to encapsulate the login page's functionality into a separate class, making it easier to manage and reuse in other test cases.

Furthermore, the project leverages data-driven testing techniques by retrieving input data from external sources, such as xlsx files or databases. This allows running the login test with various combinations of usernames and passwords, enhancing test coverage and identifying potential issues across different scenarios.

Automating the login process using Selenium, following the Page Object Model, and incorporating data-driven testing simplifies and streamlines the testing process, saving time and effort while ensuring the login functionality remains robust and reliable.

## Table of Contents
- Introduction
- Installation
- Writing Tests


## Introduction
The aim of this project is to demonstrate how to use Selenium with Python and the Unittest framework to write robust and scalable automated tests. The tests are organized using the Page Object Model design pattern, which promotes reusability and maintainability by encapsulating the functionality of each page into separate classes.
Additionally, this project showcases data-driven testing, which allows running the same test with different sets of input data. This approach enhances test coverage and helps identify potential issues across various scenarios.
## Installation
To get started with this project, follow these steps:

1. Clone this repository to your local machine:
- git clone  https://github.com/Tuhingits/Selenium-with-Python-Using-Unittest-Page-Object-Model.git
2. Change to the project's directory:
- cd Selenium-with-Python-Using-Unittest-Page-Object-Model

## Writing Tests
To create a new test case, follow these steps:

- Create a new Python file in the tests directory with a name that starts with test_.
- Import the necessary modules, including the required page object classes.
- Create a new test class that inherits from unittest.TestCase.
- Implement individual test methods within the test class. Each test method should start with the word test_.
- Use the page object classes to interact with the application's pages
and verify the expected behavior using assertions.



