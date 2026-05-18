#!/usr/bin/env python3
"""quipster-cli – print a random motivational quote.

A tiny, dependency‑free command‑line application written in Python.
"""

import random
import sys

# ---------------------------
# Quote collection (feel free to extend)
# ---------------------------
QUOTES = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Dream big and dare to fail. – Norman Vaughan",
    "Action is the foundational key to all success. – Pablo Picasso",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Stay hungry, stay foolish. – Steve Jobs",
    "What we think, we become. – Buddha",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The best revenge is massive success. – Frank Sinatra",
]

def get_random_quote() -> str:
    """Return a random quote from the QUOTES list."""
    return random.choice(QUOTES)

def main() -> int:
    """Entry point for the CLI.

    Prints a random quote to stdout and returns exit code 0.
    """
    quote = get_random_quote()
    print(quote)
    return 0

if __name__ == "__main__":
    sys.exit(main())
