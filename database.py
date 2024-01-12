from pymongo import MongoClient
import certifi
import json


def conn_db():
    client = MongoClient("localhost", 27017)

    db = client.demo

    w = db.workers

    return w


def insert(mail, psd, name):
    db = conn_db()

    # print(f"Inside insert function of {db}")

    # try:
    #     db.insertOne({'e-mail': mail, "password": psd, "name": name})
    # except Exception as e:
    #     raise ValueError

    return f"Welcome {name} with e-mail {mail} and password {psd}"


def usr(a):
    db = conn_db()

    for name in db.find():
        if name['name'] == a:
            print("Worker was found")
            print("...")
            print(name['name'])
            return name['name']