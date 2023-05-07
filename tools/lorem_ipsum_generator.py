import requests

# https://api-ninjas.com/profile
API_KEY = "m4ds/ecCAidZmdxhHfhIEA==dO6gNCiEm2CEl6Ro"
paraghaps = int(input("How many paragraph do you want to generate: "))

# concatenate the number of paragraphs in param paragraphs
API_URL = f"https://api.api-ninjas.com/v1/loremipsum?paragraphs={paraghaps}"

# set the api key
response = requests.get(
    API_URL,
    headers={
        "X-Api-Key": API_KEY,
    },
)

text = (
    response.text
    if response.status_code == requests.codes.ok
    else f"{response.status_code} | {response.text}"
)
print(text)
