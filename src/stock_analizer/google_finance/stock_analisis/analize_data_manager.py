
from src.tools.mongo_data_manager import MongoDataManager
from datetime import datetime

#TODO: Check this class under uses in terms of analizing the data.
class AnalizeDataManager(MongoDataManager):
    """
    Comunicates between application and database analisis collection.
    """

    ANALISIS_COLLECTION = "analisis"

    # Analisis types
    CORELATION_TYPE = "corelation"


    def __init__(self, database: str):
        MongoDataManager.__init__(self, database)
        self.collection = AnalizeDataManager.ANALISIS_COLLECTION

    def save_analisis(self, analisis_data):
        """
        Saves analisis data
        """
        self.save_items(self.collection, analisis_data)


    def load_analisis(self, type: str):
        """
        Loads analisis data
        """
        query = {"Type" : type}
        return self.load_items(self.collection, query)


    def load_best_correls_for(self, num_of_corels: int, comp_name: str, start_date: datetime, end_date: datetime) -> list:
        """
        Loads company names and correlations with the best correlations to specified comp_name between specified dates.
        """
        query = {}
        return self.load_items(self.collection, query)


    def load_worst_correls_for(self, num_of_correls: int, comp_name: str, start_date: datetime, end_date: datetime) -> list:
        """
        Loads company names and correlations with the best correlations to specified comp_name between specified dates.
        """
        query = {}
        return self.load_items(self.collection, query)

    def load_correls_for(self, comp_name: str):
        """
        Loads all companies correlations.
        """
        query = {}
        return self.load_items(self.collection, query)

    def load_best_correls(self, num_of_comps: int) -> list:
        """
        Loads companies with the best correlations.
        """
        return 0

    def load_comps_with_the_best_vols(self):
        """

        """


