# quipster-cli

**quipster‑cli** is a one‑file Python command‑line tool that displays a random motivational quote when executed.

## Features
- No external dependencies – pure Python 3.8+.
- Small footprint (≈ 200 LOC).
- Easy to extend with your own quotes.

## Installation
```bash
# Clone the repository (or download the single file)
git clone https://github.com/yourusername/quipster-cli.git
cd quipster-cli
# Make the script executable (optional)
chmod +x quipster.py
```

## Usage
```bash
# Run directly
python quipster.py
# Or, if made executable and on PATH
./quipster.py
```
You will see a random quote printed to stdout.

## Adding Your Own Quotes
Edit the `QUOTES` list in `quipster.py` and add any strings you like.

## License
MIT – see LICENSE file.
