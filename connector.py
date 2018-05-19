from pymongo import MongoClient

Mongo = MongoClient('127.0.0.1', 27017)['ActionDB']

if __name__ == '__main__':
    res = Mongo.action.find()
    print(res)

