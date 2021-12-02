import requests
r = requests.get("https://open.spotify.com/playlist/0SRdjSDz4RsuozwHv1zhvr")
print(r.content)
