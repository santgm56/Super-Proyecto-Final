class WebDataExtractor:
    def __init__(self, url: str, request_headers: dict = None):
        self._url = url
        self._request_headers = request_headers if request_headers else {}

    def get_data(self):
        """
        Método principal para obtener los datos.
        Este método debe ser implementado en las clases derivadas.
        """
        pass

    def handle_exception(self, error: Exception):
        """
        Método para manejar excepciones durante el scraping.
        """
        pass