# cli.py

import argparse
import json
from password_strength import evaluate_password

def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Checker"
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="Password to evaluate. If omitted, you’ll be prompted."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full result as JSON."
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        help="Save the report to FILE (in text or JSON, matching --json)."
    )
    args = parser.parse_args()

    # 1) Get the password (arg or prompt)
    if args.password:
        pw = args.password
    else:
        pw = input("Enter a password to evaluate: ")

    # 2) Evaluate
    result = evaluate_password(pw)

    # 3) Format output
    if args.json:
        out_str = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        lines = [
            f"Overall rating: {result['overall']}",
            f"Score (0–4): {result['score']}",
            f"Entropy: {result['entropy']:.1f} bits",
            f"Length: {result['length']} characters",
            f"Character classes used: {result['categories_used']}/4"
        ]
        if result['feedback']['warning']:
            lines.append(f"Warning: {result['feedback']['warning']}")
        for tip in result['feedback']['suggestions']:
            lines.append(f"- {tip}")
        out_str = "\n".join(lines)

    # 4) Print or save
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out_str)
        print(f"Report saved to {args.output}")
    else:
        print(out_str)

if __name__ == "__main__":
    main()
