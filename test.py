import pprint
dictionary = {}
def createDict(ls):
    maindata = {"rank": "",
    "playlist Name": "",
    "Curator" : "",
    "Listeners" : "",
    "Streams ":""}


    counter = 0
    for k,v in maindata.items():
        maindata[k] =ls[counter]
        counter +=1

    dictionary[maindata["playlist Name"]] = maindata



createDict([94 , "play1" , "iam1" , "1000" , "1231231"])
createDict([1 , "play132" , "iam23121" , "1001231230" , "12312343423"])


pprint.pprint(dictionary)
