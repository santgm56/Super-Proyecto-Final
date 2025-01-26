from src.base.web_data_extractor import WebDataExtractor
from selenium import webdriver
from bs4 import BeautifulSoup

class DynamicPageExtractor(WebDataExtractor):
    def __init__(self, url: str, driver_location: str, request_headers: dict = None):
        super().__init__(url, request_headers)
        self._driver_location = driver_location

    def get_data(self):
        """
        Lógica para obtener datos de una página dinámica
        """
        pass

    def extract_data(self, soup: BeautifulSoup, selector: str):
        """
        Lógica para extraer los datos usando BeautifulSoup
        """
        pass