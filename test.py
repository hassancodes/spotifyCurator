import requests
a = requests.get("https://open.spotify.com/artist/4MCBfE4596Uoi2O4DtmEMz/discovered-on")
print(a.content)
