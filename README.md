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
- Python 3.x (I only tested with version 3.8.12)
- Compatible with Windows, Linux, and macOS
- No extra libraries required

## How to Install
1. Download the [zorpheus.py](https://raw.githubusercontent.com/simplyYan/Zorpheus/main/zorpheus.py) file.
2. Move the file to the root of the system (on Linux, use `~`, on macOS and Windows, refer to the appropriate documentation) {OPTIONAL, BUT CAN MAKE IT EASIER TO USE}
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
#### Success criteria
This command defines which characteristics will indicate that the credentials are correct. Each site has its own way of dealing with a successful login. You need to know what action your target takes when it logs in correctly. You can do this by analyzing the target's source code or by testing, or by getting information from the great internet.
Here are the success parameters accepted by our tool:
- StatusCode: Checks the status code of the HTTP response.
- Keyword: Checks for the presence of a specific keyword in the response.
- Header: Checks for the presence of a specific header in the response.
- Cookie: Checks for the presence of a specific cookie in the response.

### Command: `wordlistgen`
The `wordlistgen` command is used to generate a wordlist file in JSON format.

#### Arguments:
- List of file paths: Paths to text files containing usernames and passwords.

#### Example:
```bash
python3 zorpheus.py wordlistgen usernames.txt passwords.txt > wordlist.json
```

## Get one of the world's largest general wordlists
You can use Worpheus, which is one of the largest wordlists in the world. It comes in .TXT by default (you can convert it to the JSON format accepted by Zorpheus using wordlistgen, just duplicate it, and merge it using wordlistgen). Worpheus has over 130,000 words and combinations for real names, usernames, passwords, server files, passwords and default names for various tools, extra words for the additional password, city names, country names, street names.
Worpheus uses only real information, taken from real platforms and the world. The wordlist is 160MB long, and one big detail: there's an 85% chance that your target's credentials (regardless of the target) are in Worpheus. It's 100% free and open-source. Download it using Google Drive or Mediafire:
1. Google Drive: https://drive.google.com/file/d/1btvUoClrL3TFreDtT51P45DK2O4jSbWG/view?usp=sharing
2. Mediafire: https://www.mediafire.com/file/1vn7x9sa79vw62u/Worpheus.txt/file
- **Note**: This wordlist is compatible with any tool, be it Zorpheus, Hydra or Medusa, but due to its size, it can take up to 20% longer to get the results. It can easily be used in Zorpheus with wordlistgen, a native and exclusive command.

## License
Zorpheus is distributed under the [BSD-3-Clause License](LICENSE).

## Disclaimer
The author is not responsible for the unethical misuse of this tool. Make sure to obtain proper permission before performing login tests on third-party systems or applications.
