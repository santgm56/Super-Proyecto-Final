from src.base.web_data_extractor import WebDataExtractor
from bs4 import BeautifulSoup

class StaticPageExtractor(WebDataExtractor):
    def __init__(self, url: str, request_headers: dict = None):
        super().__init__(url, request_headers)

    def get_data(self):
        """
        Lógica para obtener datos de una página estática
        """
        pass

    def extract_data(self, soup: BeautifulSoup, selector: str):
        """
        Lógica para extraer los datos usando BeautifulSoup
        """
        pass