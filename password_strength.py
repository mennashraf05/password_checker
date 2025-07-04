# password_strength.py

import string
import math
from zxcvbn import zxcvbn

def load_common_passwords(filepath: str = 'common_passwords.txt') -> set:
    """
    Load a list of common passwords (one per line) into a set.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return set()

COMMON_PASSWORDS = load_common_passwords()

def evaluate_password(password: str) -> dict:
    """
    Analyze a password and return a dict with:
      - score (0–4 from zxcvbn)
      - guesses (estimated number of guesses)
      - entropy (bits, computed from guesses_log10)
      - length
      - categories_used (number of character classes)
      - overall rating ('Very Weak', 'Weak', 'Fair', 'Strong')
      - feedback (warning and suggestions)
    """
    pw_lower = password.lower()
    if pw_lower in COMMON_PASSWORDS:
        return {
            'score': 0,
            'guesses': 0,
            'entropy': 0.0,
            'length': len(password),
            'categories_used': 0,
            'overall': 'Very Weak',
            'feedback': {
                'warning': 'This password is too common.',
                'suggestions': ['Use a less common password.']
            }
        }

    zx = zxcvbn(password)
    guesses = zx.get('guesses', 0)
    guesses_log10 = zx.get('guesses_log10', 0.0)
    entropy_bits = guesses_log10 * math.log2(10)  # ≈ guesses_log10 * 3.3219

    score = zx['score']        # 0 to 4
    feedback = zx['feedback']  # dict with 'warning' & 'suggestions'

    # Check character categories
    categories = {
        'lower': any(c.islower() for c in password),
        'upper': any(c.isupper() for c in password),
        'digits': any(c.isdigit() for c in password),
        'symbols': any(c in string.punctuation for c in password)
    }
    categories_used = sum(categories.values())
    length = len(password)

    # Derive a simple overall rating
    if score <= 1 or length < 8 or categories_used < 2:
        overall = 'Weak'
    elif score == 2 or length < 12 or categories_used < 3:
        overall = 'Fair'
    else:
        overall = 'Strong'

    return {
        'score': score,
        'guesses': guesses,
        'entropy': entropy_bits,
        'length': length,
        'categories_used': categories_used,
        'overall': overall,
        'feedback': feedback
    }

if __name__ == '__main__':
    pw = input("Enter a password to evaluate: ")
    result = evaluate_password(pw)
    print(f"\nOverall rating: {result['overall']}")
    print(f"Score (0–4): {result['score']}")
    print(f"Guesses: {result['guesses']}")
    print(f"Entropy: {result['entropy']:.1f} bits")
    print(f"Length: {result['length']} characters")
    print(f"Character classes used: {result['categories_used']}/4")
    if result['feedback']['warning']:
        print(f"\nWarning: {result['feedback']['warning']}")
    for suggestion in result['feedback']['suggestions']:
        print(f"- {suggestion}")
