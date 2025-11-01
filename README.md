✅ Selenium Login Automation (Pytest)

This project automates the login functionality of a web application using Selenium, Pytest, and HTML reporting.

📌 Project Structure
project/
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│
├── drivers/        (optional for ChromeDriver/GeckoDriver)
│
├── requirements.txt
│
└── README.md

🛠 Prerequisites

Make sure you have the following installed:

Python 3.8 or above ✅

Google Chrome / Firefox ✅

ChromeDriver or GeckoDriver (matching browser version)

📦 Install Dependencies
pip install -r requirements.txt


Example requirements:

selenium
pytest
pytest-html
webdriver-manager

▶️ How to Run Tests

From the project root, run:

pytest tests/test_login.py --html=report.html


✅ This will execute login test
📄 Generate an HTML report → report.html

🧪 Sample Test Flow

Open login page

Enter username & password

Click Login button

Validate successful login

📁 HTML Report Output

After test execution, open:

👉 report.html

in any browser to check results ✅

✨ Future Enhancements

Page Object Model (POM)

Multiple test cases for negative login

Integration with CI/CD (GitHub Actions)

Screenshot capture on failure
