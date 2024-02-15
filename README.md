# Zorpheus

## Brief Description
Zorpheus is a command-line tool developed in Python for performing login tests on web pages. It is designed to be easy to use, fast, lightweight, and highly customizable, allowing users to define their own success criteria to determine whether a login attempt was successful or not.

## Features
- **Easy to Use:** Zorpheus is designed to be accessible to users of all skill levels.
- **Fast:** By combining a simple approach with efficient execution, Zorpheus performs login tests quickly and effectively.
- **Lightweight:** With few dependencies and a minimalist design, Zorpheus is light on resources and easy to install.
- **Highly Customizable:** Users can define their own success criteria to adapt to different testing environments.
- **Open-source:** Zorpheus is distributed under the BSD-3-Clause license, allowing users to modify and distribute the code as needed.

## Requirements
- Python 3.x
- Compatible with Windows, Linux, and macOS
- No extra libraries required

## How to Install
1. Download the [zorpheus.py](https://raw.githubusercontent.com/simplyYan/Zorpheus/main/zorpheus.py) file.
2. Move the file to the root of the system (on Linux, use `~`, on macOS and Windows, refer to the appropriate documentation).
3. Run the file using Python:

```bash
python3 zorpheus.py
```

## Usage

### Command: `knock`
The `knock` command is used to perform login tests on web pages.

#### Arguments:
- `URL`: The URL of the login page.
- `Username`: (Optional) The name of the username field in the login form.
- `Password`: (Optional) The name of the password field in the login form.
- `Wordlist`: The path to the wordlist file containing usernames and passwords.
- `SuccessCriteria`: (Optional) A dictionary containing custom success criteria.

#### Example:
```bash
python3 zorpheus.py knock '{"URL": "http://example.com/login", "Username": "username", "Password": "password", "Wordlist": "wordlist.json", "SuccessCriteria": {"StatusCode": 200, "Keyword": "Welcome"}}'
```

### Command: `wordlistgen`
The `wordlistgen` command is used to generate a wordlist file in JSON format.

#### Arguments:
- List of file paths: Paths to text files containing usernames and passwords.

#### Example:
```bash
python3 zorpheus.py wordlistgen usernames.txt passwords.txt > wordlist.json
```

## License
Zorpheus is distributed under the [BSD-3-Clause License](LICENSE).

## Disclaimer
The author is not responsible for the unethical misuse of this tool. Make sure to obtain proper permission before performing login tests on third-party systems or applications.
