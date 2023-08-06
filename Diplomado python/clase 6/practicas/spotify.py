import requests

auth_token='BQC14m__a49O8v1yNdM-_AP49IcLBSzIL8zH3lM-i7Ew-_v29t2vlA5jwtDZW01m8iCNOnT5Xr-bITpcrb1rV5O8WbMynTgwgsbv3dkk1sKgsaC9FeY'
head = {'Authorization': 'Bearer ' + auth_token}
responsePost = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds',headers=head)
print(responsePost.content)

json = responsePost.json()
print(json)