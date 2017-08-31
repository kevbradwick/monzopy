import os
from monzopy import MonzoClient


ACCESS_TOKEN = os.getenv('MONZO_ACCESS_TOKEN')


client = MonzoClient(ACCESS_TOKEN)

print(client.accounts)