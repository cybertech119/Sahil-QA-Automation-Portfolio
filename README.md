✅ Selenium Login Automation (Pytest)

--------------------------------------------------------------------------------------------------------------------------------

This project automates the login functionality of a web application using Selenium, Pytest, and HTML reporting.

--------------------------------------------------------------------------------------------------------------------------------
📌 Project Structure
project/
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│
├── drivers/        (optional: ChromeDriver/GeckoDriver)
│
├── requirements.txt
│
└── README.md

--------------------------------------------------------------------------------------------------------------------------------

**🛠 Prerequisites**

Python 3.8+

Google Chrome / Firefox

Matching ChromeDriver / GeckoDriver

--------------------------------------------------------------------------------------------------------------------------------

**📦 Install Dependencies**
pip install -r requirements.txt

--------------------------------------------------------------------------------------------------------------------------------

**Example requirements:**

selenium
pytest
pytest-html
webdriver-manager

--------------------------------------------------------------------------------------------------------------------------------

**▶️ Test Execution Commands**

Run a specific test with HTML report:

pytest tests/test_login.py --html=report.html

--------------------------------------------------------------------------------------------------------------------------------

**⏱ Test Execution Duration**

When you run the HTML report, you will see:

✅ Start Time → When test execution began
✅ End Time → When execution completed
✅ Total Duration → How long the test took

You can open:

👉 report.html

in your browser to view these timing details along with pass/fail results.

--------------------------------------------------------------------------------------------------------------------------------

**🧪 Test Scenario**

Launch browser

Navigate to login page

Enter username & password

Click login

Validate successful login

--------------------------------------------------------------------------------------------------------------------------------

**📝 Future Enhancements**

Convert to Page Object Model (POM)

Capture screenshots on failure

Add multiple negative test cases

Integrate with CI/CD pipelines
