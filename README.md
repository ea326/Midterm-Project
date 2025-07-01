# Enhanced Calculator Command-Line Application

---

# 1. Installation Instructions

## 1.1 Clone the repository

```bash
git clone https://github.com/ea326/Midterm-Project.git
cd YOUR_REPO_NAME
```

## 1.2 Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate.bat  # Windows
```

## 1.3 Install dependencies

```bash
pip install -r requirements.txt
```

---

# 2. Configuration Setup

1. Create a file named `.env` in the project root:

   ```env
   CALCULATOR_HISTORY_DIR=./history
   LOGGING_LEVEL=INFO
   ```

2. The application uses `python-dotenv` to load these variables at runtime.

---

# 3. Usage Guide

1. Run the application:

   ```bash
   python main.py
   ```

2. Enter commands in the format:

   ```
   operation operand1 operand2
   ```

   **Examples:**

   ```text
   add 4 5
   power 2 3
   ```

3. Supported operations:

   - `add`
   - `subtract`
   - `multiply`
   - `divide`
   - `power`
   - `root`
   - `modulus`
   - `int_divide`
   - `percent`
   - `abs_diff`

4. Special commands:

   - `undo` — revert the last operation  
   - `redo` — reapply the last undone operation  
   - `history` — display all past calculations  
   - `exit` — quit the application  

---

# 4. Testing Instructions

To run unit tests and generate a coverage report:

```bash
pytest --cov=app tests/
```

Ensure your virtual environment is active before running the tests.

---

# 5. CI/CD Information

This project uses GitHub Actions to:

- Run all unit tests on every push and pull request  
- Check code coverage with `pytest-cov`  
- Prevent regressions by enforcing test success  

Workflow definition: `.github/workflows/python-app.yml`

---

# 6. Developer Notes

- **Factory pattern** for operation creation  
- **Memento pattern** for undo/redo functionality  
- **Observer pattern** for logging observers  
- History persisted as CSV via **pandas**  
- Configuration loaded via `.env` and **python-dotenv**  
- Code organized into modules for clarity and reuse  

---

# 7. Example `.env` File

```env
CALCULATOR_HISTORY_DIR=./history
LOGGING_LEVEL=DEBUG
```

---

# 8. Useful Commands Cheat Sheet

| Action                                     | Command                                                              |
|--------------------------------------------|----------------------------------------------------------------------|
| Clone repository                           | `git clone <repo-url>`                                               |
| Create virtual environment                 | `python3 -m venv venv`                                               |
| Activate virtual environment (Mac/Linux)   | `source venv/bin/activate`                                           |
| Activate virtual environment (Windows)     | `venv\Scripts\activate.bat`                                          |
| Install dependencies                       | `pip install -r requirements.txt`                                    |
| Run the calculator                         | `python main.py`                                                     |
| Run tests with coverage                    | `pytest --cov=app tests/`                                            |
| Push code to GitHub                        | `git add . && git commit -m "message" && git push`                   |

---

# 9. Notes

- Use Python 3.10 or newer.  
- Always work inside the virtual environment.  
- Ensure the `.env` file exists before running the app.  
- History directory will be created automatically if missing.  



