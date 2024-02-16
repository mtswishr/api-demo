import requests
import click
import json
import os
from dotenv import load_dotenv


@click.command()
@click.option("--phone-num", prompt="Enter the phone number you wish to query")
def lookup_num(phone_num):
    load_dotenv()
    api_key = os.environ.get("api_key")
    if api_key is None:
        print("API Key doesn't exist. Create a .env with your key")
        return

    header = {"Authorization" : f"AccessKey {api_key}"}
    try:
        res = requests.get(f"https://rest.messagebird.com/lookup/{phone_num}", headers=header) 
        match res.status_code:
            case 200:
                res = json.loads(res.content)
                print(f"Country code: {res['countryCode']}")
                print(f"Country prefix: {res['countryPrefix']}")
                print(f"Phone number as e164 format: {res['formats']['e164']}")
            case 404:
                print("In the short time that you programmed this application to presenting it, the URL seems to have changed")
            case 429:
                # Todo implement exponential backoff
                print("Client is rate limited, implement exponential backoff")
        
    except requests.ConnectionError as e:
        print("Occams razor indicates it is probably DNS")
        print(f"e is: {e}")

    except requests.RequestException as e:
        print("Requests has thrown a general request error.")
        print(f"e is: {e}")

    except Exception as e:
        print(e)

@click.command()
@click.option("--id", prompt="Enter the album ID")
def get_photos(id):
    photos = requests.get("https://jsonplaceholder.typicode.com/photos")
    albums = requests.get("https://jsonplaceholder.typicode.com/albums")

    photos = json.loads(photos.content)
    albums = json.loads(albums.content)

    for photo in photos:
        if photo["albumId"] == int(id):
            res = requests.get(photo["url"])
            with open(f"./{photo['title']}", "ab") as file:
                      file.write(res.content)
