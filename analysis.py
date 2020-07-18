from reader import Reader
import numpy as np

class Analysis:
    def __init__(self):
        self.reader = Reader()
        self.cities = self.get_cities_names()

    def get_cities_names(self):
        data = self.reader.read_from_csv("data/cells_geo.csv", ";")
        cities = dict()

        for row in np.array(data):
            city = ''
            for idx, record in enumerate(row):
                if idx == 1:
                    city = record
                elif idx == 11:
                    cities[record] = city

        return cities

    def get_most_calls_city(self):
        day_1_data = self.reader.read_from_csv("data/Telcom_dataset.csv")
        mode_city = day_1_data.SITE_ID.mode()

        city_name = self.cities.get(mode_city[0])
        print(city_name)

        day_2_data = self.reader.read_from_csv("data/Telcom_dataset2.csv")
        mode_city = day_2_data.SITE_ID.mode()

        city_name = self.cities.get(mode_city[0])
        print(city_name)

        day_3_data = self.reader.read_from_csv("data/Telcom_dataset3.csv")
        mode_city = day_3_data.SIET_ID.mode()

        city_name = self.cities.get(mode_city[0])
        print(city_name)



"""
class MyClass():
    # my_analysed_variable = None
    def my_def(self):
       # analyses 1,000,000,000 rows
       self. = results
        pass
    
    def my_user_def(self):
        # use the analysis
        # I will use self.my_analysed_variable

class MyOtherClass:
    def main(self):
        my_class = MyClass() # creates an Instance
        my_class.my_def()
        my_class.my_user_def()
        
"""
