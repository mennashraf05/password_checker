# 🚀 Password Strength Checker

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org/) [![Flask](https://img.shields.io/badge/flask-★-green)](https://flask.palletsprojects.com/) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

A versatile tool to evaluate and improve password security, available as both a **command-line** utility and a **web application**.

---

## 🔍 Table of Contents

* [✨ Features](#-features)
* [⚙️ Installation](#️-installation)
* [💻 Command-Line Usage](#-command-line-usage)
* [🌐 Web Interface Usage](#-web-interface-usage)
* [🎨 Customization](#-customization)
* [🛠️ Development & Contributing](#️-development--contributing)
* [📄 License](#-license)

---

## ✨ Features

* **Robust Analysis** using [zxcvbn](https://github.com/dropbox/zxcvbn):

  * Score (0–4)
  * Estimated guesses & entropy (bits)
  * Character class breakdown (lowercase, uppercase, digits, symbols)
  * Actionable warnings & suggestions
* **Common Password Detection** (top 10,000 list)
* **Command-Line Interface** (`cli.py`):

  * Interactive or one-shot modes
  * JSON output & file export
* **Web Interface** (`app.py` + `templates/index.html`):

  * Real-time strength bar & labels
  * Generate strong random passwords
  * Copy-to-clipboard button
  * Responsive, modern UI with Bootstrap & FontAwesome

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/youruser/password-strength-checker.git
   cd password-strength-checker
   ```
2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Download common passwords list**

   ```bash
   curl -L -o common_passwords.txt \
     https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt
   ```

---

## 💻 Command-Line Usage

```bash
# Interactive prompt
python cli.py

# One-shot evaluation
python cli.py "My$ecureP@ssw0rd"

# JSON output
python cli.py "password123" --json

# Save report to file
python cli.py "correcthorsebatterystaple" -o report.json
```

---

## 🌐 Web Interface Usage

1. **Start the Flask server**

   ```bash
   python app.py
   ```

2. **Open** your browser and navigate to:

   > [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. **Interact** with the UI to check, generate, or copy passwords.

---

## 🎨 Customization

* **Strength thresholds** can be adjusted in `password_strength.py`:

  ```python
  if score <= 1 or length < 8:
      overall = 'Weak'
  elif score == 2 or length < 12:
      overall = 'Fair'
  else:
      overall = 'Strong'
  ```
* **UI styling** lives in `templates/index.html` (Bootstrap & embedded CSS).
* **Extend** functionality by adding:

  * Password history/log
  * API endpoints for remote checks
  * Docker containerization

---

## 🛠️ Development & Contributing

1. Fork the repo and create your feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
2. Commit your changes and push:

   ```bash
   git commit -m "Add new feature"
   git push origin feature/YourFeature
   ```
3. Open a Pull Request and describe your changes.

Please follow the [contribution guidelines](CONTRIBUTING.md).

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
