import pandas

class Reader:
    def __init__(self):
        pass

    def read_from_csv(self, file_name, delimeter=","):
        """
        Reads the raw data from the CSV files.
        Returns a list of dictionaries
        """

        return pandas.read_csv(file_name, sep=delimeter)
