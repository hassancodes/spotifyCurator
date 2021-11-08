import json
fp = open("dump.json", "r")
dataDict = json.loads(fp.read())
dt = []
for playlistName,data in dataDict.items():
    dt.append(data)
print(dt[0]["rank"])
