# SauceDemo Automation Testing

Automated testing framework for the [SauceDemo](https://www.saucedemo.com/) e-commerce application using **Python, Playwright, and Pytest**.

The project follows the **Page Object Model (POM)** design pattern and includes automated test execution, test data management, screenshots, videos, traces, HTML reports, and GitHub Actions CI/CD.

---

## 🚀 Project Overview

This project automates functional testing of the SauceDemo web application.

The main modules covered are:

* Login
* Products
* Shopping Cart
* Checkout
* Logout

The framework is designed to be maintainable, reusable, and suitable for running both locally and in a CI/CD environment.

---

## 🛠️ Tech Stack

* **Python 3.13+**
* **Playwright**
* **Pytest**
* **Pytest HTML**
* **python-dotenv**
* **Git & GitHub**
* **GitHub Actions**
* **Page Object Model (POM)**

---

## 📂 Project Structure

```text
SauceDemo-Automation/
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test_data/
│   └── login_data.py
│
├── screenshots/
├── videos/
├── traces/
│
├── conftest.py
├── config.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
├── test_login.py
├── test_products.py
├── test_cart.py
├── test_checkout.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Biwash-2002/SauceDemo-Automation.git
cd SauceDemo-Automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browsers

```bash
playwright install
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
BASE_URL=https://www.saucedemo.com/
STANDARD_USERNAME=standard_user
STANDARD_PASSWORD=secret_sauce
```

The `.env` file is excluded from Git using `.gitignore`.

**Never commit sensitive credentials to GitHub.**

---

## ▶️ Running Tests

Run the complete test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest test_login.py
```

Run only login tests:

```bash
pytest test_login.py -v
```

---

## 🧪 Test Coverage

### Login Testing

The login test suite covers:

* Valid login
* Invalid username
* Invalid password
* Invalid username and password
* Empty username
* Empty password
* Empty username and password
* Locked-out user
* Logout

### Products Testing

The product module covers:

* Product page loading
* Product count
* Product names
* Product prices

### Cart Testing

The cart module covers:

* Adding products
* Cart badge count
* Opening cart
* Product visibility in cart

### Checkout Testing

The checkout module covers:

* Opening checkout
* Customer information
* Required field validation
* Checkout completion
* Order confirmation

---

## 🏗️ Framework Design

This framework uses the **Page Object Model (POM)**.

Each major application page has its own class.

For example:

```text
LoginPage
ProductsPage
CartPage
CheckoutPage
```

Common browser actions are handled by:

```text
BasePage
```

This reduces duplicate code and makes the framework easier to maintain.

---

## 📊 Test Data Management

Login test data is maintained separately in:

```text
test_data/login_data.py
```

Pytest parametrization is used to execute the same test with multiple sets of data.

Example:

```python
@pytest.mark.parametrize(
    "username, password, expected_error",
    LOGIN_TEST_DATA
)
```

---

## 📸 Failure Evidence

The framework captures debugging evidence when a test fails.

### Screenshot

Failed tests automatically generate screenshots inside:

```text
screenshots/
```

### Video

Browser recordings are stored inside:

```text
videos/
```

### Trace

Playwright traces are generated inside:

```text
traces/
```

These files help investigate test failures and understand what happened during execution.

---

## 📄 HTML Test Report

Pytest HTML reporting is included in the project.

Generate an HTML report using:

```bash
pytest --html=report.html --self-contained-html
```

The generated report can be opened in a browser.

---

## 🔄 CI/CD with GitHub Actions

This project uses **GitHub Actions** to automatically execute the test suite.

The workflow is located at:

```text
.github/workflows/pytest.yml
```

The CI pipeline:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Installs Chromium
5. Loads environment variables from GitHub Secrets
6. Runs the Pytest test suite

Tests are automatically executed when changes are pushed to the `main` branch or when a pull request is created.

---

## 🔒 GitHub Secrets

The CI workflow uses GitHub Secrets for environment configuration:

```text
BASE_URL
STANDARD_USERNAME
STANDARD_PASSWORD
```

This keeps credentials outside the source code.

---

## 🎯 QA Skills Demonstrated

This project demonstrates practical knowledge of:

* Manual testing concepts
* Test case design
* Functional testing
* Regression testing
* Negative testing
* Test data management
* Python
* Playwright
* Pytest
* Page Object Model
* Fixtures
* Parametrization
* Environment configuration
* Screenshot/video/trace debugging
* HTML test reporting
* Git
* GitHub
* CI/CD
* GitHub Actions

---

## 📈 Future Improvements

Planned improvements include:

* Cross-browser testing
* Parallel test execution
* Allure reporting
* More extensive API testing
* Improved test data management
* Scheduled nightly test execution
* Test result publishing in CI/CD

---

## 👨‍💻 Author

**Biwash Thapa**

QA Automation Tester | Frontend Developer

GitHub: [Biwash-2002](https://github.com/Biwash-2002)

---

## ⭐ Project

If you find this project useful, feel free to give it a ⭐ on GitHub.

## 📋 Manual Testing Documentation

I have created manual test cases for the SauceDemo application covering:

- Login Testing
- Products Testing
- Cart Testing
- Checkout Testing

📊 **[View / Download Manual Test Cases](./test_cases/SauceDemo%20QA%20Project.xlsx)**

CI/CD configured with GitHub Actions.