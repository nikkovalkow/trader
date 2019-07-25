try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["kufar"]
    mycol_dead = mydb["data_dead"]
    mycol=mydb["data"]
    mycol_sold=mydb["data_sold"]