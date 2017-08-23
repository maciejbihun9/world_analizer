
from src.tools.mongo_data_manager import MongoDataManager

class AnalizeDataManager(MongoDataManager):
    """
    Comunicates between application and database analisis collection.
    """

    ANALISIS_COLLECTION = "analisis"


    def __init__(self, database: str):
        MongoDataManager.__init__(self, database)
        self.collection = AnalizeDataManager.ANALISIS_COLLECTION



