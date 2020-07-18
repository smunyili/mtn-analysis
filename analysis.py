from reader import Reader
from numpy import genfromtxt

class Analysis:
    def __init__(self):
        print("Initiaised the Analysis")

    def get_read_data(self):
        reader = Reader()
        data = reader.read_from_csv("data/Telcom_dataset3.csv")
        # print(data)

        # my_data = genfromtxt('data/Telcom_dataset3.csv')
        # print(my_data)

        dictionary = {"PRODUCT": "Voice", "Value": "61", "date":  "2012-05-08 23:01:28.0", "site_id": "547385b9d5"}
        dictionary2 = {"PRODUCT": "Voice", "Value": "100", "date":  "2012-07-08 23:01:28.0"}
        dictionary3 = {"PRODUCT": "Voice2", "Value": "100", "date":  "2012-07-08 23:01:28.0"}
        list = [dictionary, dictionary2, dictionary3]


        cities = dict()
        myList = []

        for record in list:
            cities["site_id"] = "Abobo"
            myList.append(record["PRODUCT"])
            mySet.add(record["PRODUCT"])

        print(mySet)
        print(myList)



# nested list
# List of dictionaries

    def analyse():
        pass