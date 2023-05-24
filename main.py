import json
import requests
import os


def get_status_and_response_time(hostname):
    """
    This function takes a hostname as an input and returns the status code and response time of the website.
    :param hostname: str
    :return: tuple (int, int)
    """
    try:
        r = requests.get(hostname)
        return r.status_code, int(r.elapsed.total_seconds() * 1000)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred while getting the status and response time of {hostname}: {e}')
        return None, None


def send_discord_message(webhook_url, content):
    """
    This function takes a webhook URL and content as inputs and sends a message to a Discord channel.
    :param webhook_url: str
    :param content: str
    """
    headers = {'Content-Type': 'application/json'}
    data = {'content': content}
    try:
        requests.post(webhook_url, headers=headers, data=json.dumps(data))
    except requests.exceptions.RequestException as e:
        print(f'An error occurred while sending a Discord message: {e}')


def main():
    """
    This is the main function that checks the status and response time of a website and sends a message to a Discord channel.
    """
    discord_url = 'discord_webhook'
    url = os.environ.get('URL')

    status_code, response_time = get_status_and_response_time(url)
    if status_code is None:
        send_discord_message(discord_url, f'{url} is unreachable!')
    else:
        send_discord_message(discord_url, f'{url} is up! Status code: {status_code}, response time: {response_time} ms')


if __name__ == '__main__':
    main()
