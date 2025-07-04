Password Strength Checker

A simple, yet powerful tool to evaluate password strength both via command-line and a web interface.

Features

Password Analysis using zxcvbn

Score (0–4)

Estimated guesses and entropy (bits)

Character classes used (lowercase, uppercase, digits, symbols)

Warnings & suggestions

Common Password Detection (top 10,000) to flag very weak passwords

Command-Line Interface (cli.py)

Interactive prompt or pass password as argument

JSON output option

Save report to file (text or JSON)

Web Interface (app.py + templates/index.html)

Real-time strength bar and label

Generate strong random passwords

Copy-to-clipboard functionality

Responsive design with Bootstrap and FontAwesome

Installation

Clone the repository

git clone <repo-url>
cd password-strength-checker

Create & activate a virtual environment

python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

Install dependencies

pip install zxcvbn-python Flask

Download common passwords list

curl -o common_passwords.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt

Usage

Command-Line

# Interactive prompt
python cli.py

# One-shot evaluation
python cli.py "My$ecureP@ssw0rd"

# JSON output
python cli.py "password123" --json

# Save to file
python cli.py "correcthorsebatterystaple" -o report.txt

Web Interface

Run Flask app

python app.py

Open http://127.0.0.1:5000 in your browser.

Enter a password to check, generate a new one, or copy the result.

Customization

Adjust strength thresholds in password_strength.py:

if score <= 1 or length < 8 or categories_used < 2:
    overall = 'Weak'
elif score == 2 or length < 12 or categories_used < 3:
    overall = 'Fair'
else:
    overall = 'Strong'

Change UI styles in templates/index.html and embedded CSS.

Extend with additional features (e.g., password history, API endpoint).

License

This project is licensed under the MIT License. Feel free to use and modify!

