import datetime
print("can i get id?")
while True:
    id = input()
    if id == None:
        print("you must enter id")
        continue
    try:
        floatid = float(id)
    except:
        print("not valid id, try again")
        continue
    datenum = (floatid / 4194304) + 1420070400000
    time = datetime.datetime.utcfromtimestamp(datenum/1000.0)
    print("creation date is: " + time.strftime('%Y-%m-%d %H:%M:%S'))
    print("something else?")