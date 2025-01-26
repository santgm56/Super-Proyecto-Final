from src.base.web_data_extractor import WebDataExtractor
from src.components.data_handler import DataHandler

class ScrapingCoordinator:
    def __init__(self, extractor: WebDataExtractor, data_handler: DataHandler):
        self._extractor = extractor
        self._data_handler = data_handler

    def begin_scraping(self, selector: str):
        """
        Inicia el proceso de scraping usando el extractor y maneja los datos extraídos.
        """
        pass