# this contains all the functions that are used in the webapp.py
def sortJson(jsonfile):
    with open(jsonfile, "r") as fl:
        for i in dict(fl).items():
            print(i)
            break


sortJson("sevendays.json")
