import requests
import argparse
import json

class Zorpheus:
    def knock(self, args):
        url = args["URL"]
        redirect_url = args.get("RedirectURL", None)  # Novo argumento para URL de redirecionamento
        username_field = args.get("Username", None)
        password_field = args.get("Password", None)
        wordlist_path = args["Wordlist"]
        
        with open(wordlist_path, "r") as f:
            wordlist = json.load(f)

        for username in wordlist["Usernames"]["words"]:  # Corrigido para usar usernames do wordlist
            for password in wordlist["Passwords"]["words"]:
                data = {}
                if username_field:
                    data[username_field] = username
                if password_field:
                    data[password_field] = password

                response = requests.post(url, data=data)

                # Verificar os critérios de sucesso, incluindo redirecionamento para URL específica
                if self.check_success(response, args.get("SuccessCriteria", {}), redirect_url):
                    print("Credentials Found:")
                    if username_field:
                        print(f"Username: {username}")  # Corrigido para mostrar o username do wordlist
                    if password_field:
                        print(f"Password: {password}")
                    return

        print("Credentials not found in the wordlist.")

    def check_success(self, response, success_criteria, redirect_url):
        success_count = 0

        # Verificar critérios de sucesso existentes
        if "StatusCode" in success_criteria and response.status_code == success_criteria["StatusCode"]:
            success_count += 1
        if "Keyword" in success_criteria and success_criteria["Keyword"] in response.text:
            success_count += 1
        if "Header" in success_criteria and success_criteria["Header"] in response.headers:
            success_count += 1
        if "Cookie" in success_criteria and success_criteria["Cookie"] in response.cookies:
            success_count += 1

        # Verificar o redirecionamento para a URL especificada
        if redirect_url and response.status_code == 302 and redirect_url in response.headers['Location']:
            success_count += 1

        # Pelo menos 75% dos critérios devem ser atendidos para considerar como sucesso
        return success_count >= len(success_criteria) * 0.75  

    def wordlistgen(self, args):
        output = {}

        for file_path in args:
            field_name = file_path.split('.')[0].capitalize() + "s"
            words = []

            with open(file_path, 'r') as f:
                words = [line.strip() for line in f.readlines()]

            output[field_name] = {"words": ", ".join(words)}

        return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zorpheus - A tool for ethical hacking")
    parser.add_argument("command", choices=["knock", "wordlistgen"], help="Choose a command to execute")
    parser.add_argument("arguments", nargs="+", help="Arguments for the command")
    args = parser.parse_args()

    zorpheus = Zorpheus()
    if args.command == "knock":
        arguments = json.loads(args.arguments[0])
        if "RedirectURL" in arguments:
            arguments["RedirectURL"] = args.arguments[1]
        zorpheus.knock(arguments)
    elif args.command == "wordlistgen":
        arguments = args.arguments
        output = zorpheus.wordlistgen(arguments)
        print(json.dumps(output, indent=2))
