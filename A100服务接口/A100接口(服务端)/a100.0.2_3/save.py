# [Data:2015-01-01 12:00:01|000000|B|一]
import  pymongo
def save():
    client_db = pymongo.MongoClient('127.0.0.1', 27017)
    db = client_db.A100_test
    collection = db.a100
    info = collection.find()
    p = []
    for i in info:
        p.append(i)
    print(p)


# save()

def insert():
    data = data_zidian(data_rec)
    client_db = pymongo.MongoClient('127.0.0.1', 27017)
    db = client_db.A100_test
    collection = db.a100
    collection.insert(data)


def data_zidian(data_rec):
    ii = []
    for i in data_rec.split('|'):
        ii.append(i)
    # k = ii[0].split(':')[1:]
    #	print(k)
    time_t = ii[0][6:]
    adress = ii[3][:1]
    print(ii)
    data = {
        "time": time_t,
        "id": ii[1],
        "name": ii[2],
        "adress": adress
    }
    return data


data_rec = "[Data:2015-01-01 12:00:01|000000|B|哈]"
insert()