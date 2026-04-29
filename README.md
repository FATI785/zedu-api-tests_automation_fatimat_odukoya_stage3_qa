# ZEDU API Test Automation Project

## Project Overview
This project is an API automation test suite built using Python and pytest.

It validates core backend functionalities including:
- Authentication (register, login, protected routes)
- User management
- Organisation management
- Channel operations (create, join, leave)
- Role management
- Protected endpoint access control

The suite is designed to ensure API reliability, correctness, and proper access control across all modules.

---

## Prerequisites

Ensure the following are installed:

- Python 3.10+
- pip (Python package manager)
- pytest
- requests
- python-dotenv

All dependencies are listed in `requirements.txt`.

---

## Project Structure
tests/
│── test_auth.py
│── test_organisations.py
│── test_channels.py
│── test_roles.py
│── test_users.py
│── test_protected_endpoints.py

utils/
│── auth.py
│── helpers.py

conftest.py
requirements.txt
.env.example
README.md


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/FATI785/zedu-api-tests_automation_fatimat_odukoya_stage3_qa.git
cd zedu-api-tests_automation_fatimat_odukoya_stage3_qa
