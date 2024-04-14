# Pocket CMD Networking App

The Pocket CMD Networking App is a Python script designed to provide quick access to common networking utilities through a command-line interface. It allows users to perform tasks such as obtaining their IP address, tracing the route to a specified website, and pinging a target address.

**Important Note:**
This project was mainly for me to try out a cool library I found within standard Python libraries that makes running command-line commands in Python easy. It's not meant to be taken too seriously.

## Features

- Get the local machine's IPv4 address.
- Trace the route to a specified website.
- Ping a target address to check connectivity.
- Clear and user-friendly command-line interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sampise/Pocket-CMD-Networking-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pocket-cmd-networking
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the on-screen menu to choose an action:
    - Enter `1` to get your IP address.
    - Enter `2` to trace the route to a website.
    - Enter `3` to ping a target address.
    - Enter `0` to exit the application.

3. Follow the prompts to enter necessary details such as the website to trace or the target address to ping.

## Dependencies

- [Python](https://www.python.org/): 3.x
- [Subprocess](https://docs.python.org/3/library/subprocess.html): Standard Library (for running command-line processes)

## Contribution

This project is overall pretty useless and it was made just for educational puropses, you are welcome to contribute but I would advise against it.
