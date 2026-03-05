# Personal Expense Tracker

A simple expense tracking application built with Python.

## Features
- Load expenses from CSV file
- Save expenses to CSV file
- Track expenses by amount, category, and date

## Installation

1. Install [uv](https://github.com/astral-sh/uv)
2. Clone this repository
3. Create a virtual environment:
```bash
uv venv
```

4. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

5. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python FILE.PY
```

## Project Structure
- `FILE.PY` - Main expense tracker application
- `pyproject.toml` - UV/Python project configuration
- `requirements.txt` - Project dependencies

## License
MIT
