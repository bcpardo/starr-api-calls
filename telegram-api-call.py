import requests, os

def telegram_send(bot_token,chat_id,message):
    api_method = "sendMessage"
    api_url = f"https://api.telegram.org/bot{bot_token}/{api_method}"
    parse_mode = "MarkdownV2"

    message_json = {
        "chat_id" : chat_id,
        "text" : message,
        "parse_mode" : parse_mode
    }

    response = requests.get(api_url, json = message_json)

    return response.json()

def main():
    SCRIPT_PATH = os.path.realpath(__file__)
    SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
    ENV_FILE = f"{SCRIPT_DIR}/ARR_ENV.txt"

    # set api_token and chat_id environment variables with
    # export api_token="xxxxx"
    # export chat_id="12345"
    api_token = os.environ['api_token']
    chat_id = os.environ['chat_id']

    envs = {}

    # Checking all potentiall environment variables
    with open(ENV_FILE, 'r') as f:
        for line in f:
            env = line.rstrip()
            if env in os.environ:
                envs[env] = os.environ[env]

        # No environment variables were found
        # Either the script was run manually as a test (ie Not ran by *arr)
        #  or, something went wrong : )
        if len(envs) == 0:
            message = 'no starr envs'
            # raise Exception('No *arr Environment variables were found.')
        else:
            message = os.environ["RADARR_EVENTTYPE"]

    json_response = telegram_send( api_token, chat_id, message )
    print(json_response)

if __name__ == "__main__":
    main()