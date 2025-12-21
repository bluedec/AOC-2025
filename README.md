# Advent of Code – Python Solutions

This project contains solutions for daily programming challenges, organized by day and runnable from a single entry point.

The project is written in **Python 3** and uses **pytest** for automated testing.

This README was created with the help of ChatGPT, the code is not.

---

## Project Structure

```
.
├── src/
│   ├── main.py        # Entry point to run solutions
│   └── days/
│       ├── __init__.py
│       ├── day1.py
│       ├── day2.py
│       └── ...
├── tests/
│   ├── conftest.py
│   ├── test_day1.py
│   ├── test_day2.py
│   └── ...
├── README.md
```

- Each day’s solution lives in `src/days/dayX.py`
- Tests for each day live in `tests/`
- All solutions are executed through `src/main.py`

---

## Requirements

- Python **3.x**
- `pytest`

If you are using Nix, make sure `python3` and `pytest` are available in your shell.

---

## Running a Day

You can run a specific day using the main entry point:

```bash
python src/main.py <day>
```

### Example

```bash
python src/main.py 1
```

This will execute the solution for **Day 1**.

---

## Running Tests

All tests are written using **pytest**.

From the project root, run:

```bash
pytest
```

This will automatically discover and run all tests inside the `tests/` directory.

To run tests for a specific file:

```bash
pytest tests/test_day2.py
```

---
