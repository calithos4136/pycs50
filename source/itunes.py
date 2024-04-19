import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
# pulling json from the link specified
response = requests.get("https://itunes.apple.com/search?entity=song&limit=25&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

obj = response.json()
for result in obj["results"]:
    print(result["trackName"])