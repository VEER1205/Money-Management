# Money Management CLI

A simple command-line interface (CLI) application built with Python to help you track your income, expenses, and manage a basic budget. Uses the `rich` library for enhanced terminal output.

## Features

*   Track income transactions.
*   Track expense transactions.
*   View a list of all transactions.
*   Display a summary (total income, total expenses, current balance).
*   Set a simple budget limit.
*   Check current spending against the set budget.
*   Persistent data storage using a `data.json` file.
*   User-friendly CLI with formatted tables and colors (thanks to `rich`).

<!-- Add screenshots/GIFs here showing the application in action -->
**Please consider adding screenshots or a GIF to showcase the application's interface and features. This will significantly improve user understanding and engagement.**

## Requirements

*   Python 3.x
*   Libraries listed in `requirements.txt` (`rich`).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/VEER1205/Money-Management.git
    ```
2.  Navigate to the directory:
    ```bash
    cd Money-Management
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

*   Run the main script:
    ```bash
    python main.py
    ```
*   Follow the on-screen menu prompts to add income/expenses, view data, etc.

## Data Storage

Your financial data (income, expenses, budget) is stored locally in a file named `data.json` within the project directory. Make sure not to delete this file unless you want to reset your data.  **Consider backing up this file periodically.**

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for bugs, feature requests, or suggestions.

## License

This project is currently unlicensed. Please add a LICENSE file if you intend for others to use, modify, or distribute your code.  **It is highly recommended that you choose a license (e.g., MIT, Apache 2.0) to clarify the terms of use.**

## Author

Created by [VEER1205](https://github.com/VEER1205)