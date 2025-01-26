# 🌐 Sistema WebScrapping

## 🗒️ Colaboradores

```
├── Santiago Gamboa Martínez
├── Samuel Eduardo Fajardo Quintero
└── Manuel Felipe Torres Gamboa
```

# 🏆 Introducción

El volumen de información que se encuentra disponible en internet crece de manera exponencial, haciendo indispensable el uso de herramientas tecnológicas que permitan extraer y analizar datos relevantes de forma automática y eficiente. Por esta razón, como equipo, hemos elegido desarrollar la `alternativa 2`: **_Sistema de WebScrapping_**, este proyecto consiste en desarrollar e implementar un sistema de web scraping que no solo cumpla con los objetivos de extracción de datos, sino que también esté estructurado bajo los principios fundamentales de la Programación Orientada a Objetos (POO).

Este proyecto, titulado: "Super_Proyecto_Final", tiene como objetivo diseñar un sistema de web scraping estructurado bajo principios de modularidad y escalabilidad. Para ello, se emplearán herramientas como Python junto a librerías especializadas como Requests, BeautifulSoup, Selenium y Pandas. Además, se garantizará un desarrollo robusto mediante buenas prácticas, como el manejo adecuado de excepciones y una organización eficiente del código estructurado bajo el paradigma de Programación Orientada a Objetos (POO).

# ➕ Definición de Alternativa

La alternativa para este proyecto consiste en el desarrollo de un sistema de web scraping que emplee como pilar principal la Programación Orientada a Objetos (POO). El sistema, como ya se mencionó anteriormente, será desarrollado en Python, un lenguaje ampliamente reconocido por su versatilidad y su extenso ecosistema de librerías diseñadas para la extracción y manipulación de datos desde la web, ademas, se contará con la implementación de un entorno virtual en el cual se instalarán las dependencias necesarias para desarrollar y ejecutar este sistema de web scraping.


### Ventajas de esta alternativa:

- Facilita la organización y escalabilidad del sistema gracias a la implementación de Programación Orientada a Objetos (POO).
- Aprovecha el amplio ecosistema y la versatilidad de Python, que incluye librerías robustas que a su vez estan bien documentadas.
- Brinda flexibilidad para adaptarse a diversas necesidades, como la extracción de datos estáticos o dinámicos dependiendo el caso.
- Fomenta la adquisición de habilidades de diseño y codificación para su aplicación en escenarios reales.

# 🗂️ Requerimientos Técnicos:
 
### 1. **Lenguaje y Librerías**:

- Python como lenguaje principal.

 ### **Librerías**:
- **`Requests`** para realizar solicitudes HTTP.
- **`BeautifulSoup`** para parsear y extraer datos de HTML.

- **`Selenium`** para interactuar con páginas dinámicas.
- **`Pandas`** para almacenar y procesar datos en estructuras organizadas.

### 2. **Estructura del Código**:

Implementación bajo los principios de la Programación Orientada a Objetos (POO) para garantizar modularidad y escalabilidad.

### **Clases principales**:
- **`WebDataExtractor`** (base).
- **`StaticPageExtractor`** y **`DynamicPageExtractor`** (derivadas).
- **`DataHandler`** para gestionar los datos.
- **`ScrapingCoordinator`** para coordinar el flujo del sistema.

### 3. **Entorno de Desarrollo**:

- Uso de entornos virtuales para aislamiento de dependencias (venv).
- Gestión de versiones con Git para colaboración y control del progreso.
- Archivo **`requirements.txt`** para especificar las dependencias del proyecto.

### 4. **Salida de Datos**:

Soporte para formatos CSV, JSON o almacenamiento en bases de datos SQLite.

### 5. **Otros Requerimientos**:
Capacidad de manejar excepciones para evitar interrupciones en la ejecución.
Compatibilidad con sitios web tanto estáticos como dinámicos.

# 🛠️ Configuración del Entorno de Trabajo  

### **1. Clonar el repositorio**:
Descargar el código fuente con los siguientes comandos:  
```bash
git clone https://github.com/santgm56/Super-Proyecto-Final.git 
cd Super-Proyecto-Final
```
### **2. Crear y activar un entorno virtual**:
El uso de un entorno virtual ayuda a instalar las dependencias del proyecto sin interferir con otras aplicaciones de Python.

**En Windows**:
```bash
python -m venv venv  
.\venv\Scripts\activate 
```

**En macOS/Linux**:
```bash
python -m venv venv  
source venv/bin/activate  
```

### **3. Instalar las dependencias**:
Una vez dentro del entorno virtual, ejecutar:

```bash
pip install -r requirements.txt 
```

### **5. Salir del entorno virtual**:
Al terminar de trabajar o hacer modificaciones, se puede salir del entorno virtual escribiendo:
```bash
deativate
```
### **Nota adicional**: 
Si se usa Windows y existe algún problema al activar el entorno virtual, es posible que se necesite habilitar la ejecución de scripts por políticas de resticción en powershell. Para corregirlo, basta con ejecutar estos comandos en el CMD como terminal predeterminada ya que esta no cuenta con dichas condiciones. 

# 📈 Diagrama de Clases
````mermaid
classDiagram
    %% Clase base: WebDataExtractor
    class WebDataExtractor {
        - url: str
        - request_headers: dict
        + __init__(url: str, request_headers: dict)
        + get_data(): None
        + handle_exception(error: Exception): str
    }

    %% Clase derivada: StaticPageExtractor
    class StaticPageExtractor {
        + __init__(url: str, request_headers: dict)
        + get_data(): BeautifulSoup
        + extract_data(soup: BeautifulSoup, selector: str): list
    }

    %% Clase derivada: DynamicPageExtractor
    class DynamicPageExtractor {
        - driver_location: str
        + __init__(url: str, driver_location: str, request_headers: dict)
        + get_data(): BeautifulSoup
        + extract_data(soup: BeautifulSoup, selector: str): list
    }

    %% Clase para gestión de datos: DataHandler
    class DataHandler {
        - collected_data: list
        + __init__()
        + add_extracted_data(extracted_data: list): int
        + save_to_file(file_name: str): str
    }

    %% Clase controladora: ScrapingCoordinator
    class ScrapingCoordinator {
        - extractor: WebDataExtractor
        - data_handler: DataHandler
        + __init__(extractor: WebDataExtractor, data_handler: DataHandler)
        + begin_scraping(selector: str): bool
    }

    %% Relaciones
    WebDataExtractor <|-- StaticPageExtractor : herencia
    WebDataExtractor <|-- DynamicPageExtractor : herencia
    ScrapingCoordinator o-- WebDataExtractor : composición
    ScrapingCoordinator o-- DataHandler : composición
````
## **Implementación de los Pilares de POO**
### 1. **Abstracción**:

- **Aplicación**: La clase `WebDataExtractor` define métodos abstractos como `get_data()` y `handle_exception()`, lo que permite a las clases derivadas hacer sus propias implementaciones (`StaticPageExtractor` y `DynamicPageExtractor`).
- **Importancia**: se centra en lo que hace un objeto en lugar de cómo lo hace, proporcionando una interfaz clara y simplificada; ideal para adaptar su implementación en distintas situaciones.

### 2. **Encapsulamiento**:

- **Aplicación**: Los atributos `url`, `request_headers` y `driver_location` son privados (indicados por el guion `-`), lo que significa que no pueden ser accedidos directamente desde fuera de la clase. Por lo tanto, existen métodos públicos (`+`) que proporcionan acceso controlado a estos atributos.
- **Importancia**: Protege los datos de acceso no autorizado y modificaciones accidentales.

### 3. **Herencia**:

- **Aplicación**: `StaticPageExtractor` y `DynamicPageExtractor` heredan de `WebDataExtractor`, lo que significa que comparten la interfaz definida por `WebDataExtractor` y pueden proporcionar implementaciones específicas de `get_data()` y `extract_data()`.
- **Importancia**: Promueve la reutilización del código y permite crear una jerarquía de clases, lo que facilita la extensión y el mantenimiento del código.

### 4. **Polimorfismo**:

- **Aplicación**: La clase `ScrapingCoordinator` puede trabajar con cualquier objeto que sea una instancia de `WebDataExtractor` (ya sea `StaticPageExtractor` o `DynamicPageExtractor`), lo que permite que `begin_scraping()` funcione con diferentes tipos de extractores sin cambiar su implementación.
- **Importancia**: Permite que una función o un método opere sobre objetos de diferentes clases de manera uniforme sin ningún problema, facilitando la extensión del código y la integración de nuevas clases sin modificar el código existente.

# 💿 Solución Preliminar

### **Objetivo General**

Desarrollar un sistema de web scraping basado en la Programación Orientada a Objetos (POO) que permita extraer, procesar y almacenar información de manera eficiente, utilizando Python y sus herramientas especializadas.

---
## Clases principales

### 1. **Clase WebDataExtractor**:
- `__init__(url: str, request_headers: dict = None)`:  Constructor que inicializa los atributos url (URL de la página web a scrapear) y request_headers (Encabezados HTTP para la solicitud). 
- `get_data()`: Método abstracto para obtener los datos de la página web.
- `handle_exception(error: Exception)`: Método para manejar excepciones.

````python
#### src/base/web_data_extractor.py

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
````

### 2. **Clase StaticPageExtractor**:
- `__init__(url: str, request_headers: dict = None)`: Constructor que inicializa los atributos url y request_headers llamando al constructor de la clase base.
- `get_data()`: Implementación específica para obtener datos de una página estática.
- `extract_data(soup: BeautifulSoup, selector: str)`: Método para extraer los datos obtenidos.

````python 
#### src/components/static_page_extractor.py

from src.base.web_data_extractor import WebDataExtractor
from bs4 import BeautifulSoup

class StaticPageExtractor(WebDataExtractor):
    def __init__(self, url: str, request_headers: dict = None):
        super().__init__(url, request_headers)

    def get_data(self):
         """
         Método para obtener datos de una página estática
         """
        pass

    def extract_data(self, soup: BeautifulSoup, selector: str):
        """
        Método para extraer los datos usando BeautifulSoup
        """
        pass
````

### 3. **Clase DynamicPageExtractor**:
- `__init__(url: str, driver_location: str, request_headers: dict = None)`: Constructor que inicializa los atributos url, driver_location (Ruta del controlador del navegador para Selenium) y request_headers llamando al constructor de la clase base. 
- `get_data()`: Implementación específica para obtener datos de una página dinámica.
- `extract_data(soup: BeautifulSoup, selector: str)`: Método para parsear los datos obtenidos.

````python 
#### src/components/dynamic_page_extractor.py

from src.base.web_data_extractor import WebDataExtractor
from selenium import webdriver
from bs4 import BeautifulSoup

class DynamicPageExtractor(WebDataExtractor):
    def __init__(self, url: str, driver_location: str, request_headers: dict = None):
        super().__init__(url, request_headers)
        self._driver_location = driver_location

    def get_data(self):
        """
        Método para obtener datos de una página dinámica
        """
        pass

    def extract_data(self, soup: BeautifulSoup, selector: str):
        """
        Método para extraer los datos usando BeautifulSoup
        """
        pass

````
### 4. **Clase DataHandler:**
- `__init__()`: Constructor que inicializa el atributo collected_data (Datos extraídos) como una lista vacía. 
- `add_extracted_data(new_data)`: Método para añadir datos a la lista collected_data.
- `Método para guardar los datos en un archivo.`: Método para guardar los datos en un archivo.

````python 
#### src/components/data_handler.py

import pandas as pd

class DataHandler:
    def __init__(self):
        self._collected_data = []

    def add_extracted_data(self, new_data):
        """
        Método para añadir los nuevos datos extraídos al almacenamiento.
        """
        pass 

    def save_to_file(self, file_name: str):
        """
        Método para guardar los datos extraídos a un archivo.
        """
        pass
````

### 5. **Clase ScrapingCoordinator**:
- `__init__(extractor: WebDataExtractor, data_handler: DataHandler`: Constructor que inicializa los atributos extractor (Objeto extractor para realizar el scraping.) y data_handler (Objeto manejador de datos para gestionar los datos extraídos). 
- `begin_scraping(selector: str)`: Método para iniciar el proceso de scraping.

````python 
#### src/coordinator/scraping_coordinator.py

from src.base.web_data_extractor import WebDataExtractor
from src.components.data_handler import DataHandler

class ScrapingCoordinator:
    def __init__(self, extractor: WebDataExtractor, data_handler: DataHandler):
        self._extractor = extractor
        self._data_handler = data_handler

    def begin_scraping(self, selector: str):
        """
        Método para inicia el proceso de scraping usando el extractor y maneja los datos extraídos.
        """
        pass
````

# ✨ Estructura del proyecto 

```plaintext
SUPER_PROYECTO_FINAL/
├── README.md
├── requirements.txt
├── .gitignore
├── setup.py
├── main.py
├── src/
│   ├── _init_.py
│   ├── base/
│   │   ├── _init_.py
│   │   └── web_data_extractor.py     # Clase base WebDataExtractor
│   ├── components/
│   │   ├── _init_.py
│   │   ├── static_page_extractor.py  # Clase derivada StaticPageExtractor
│   │   ├── dynamic_page_extractor.py # Clase derivada DynamicPageExtractor
│   │   └── data_handler.py           # Clase DataHandler
│   ├── coordinator/
│   │   ├── _init_.py
│   │   └── scraping_coordinator.py   # Clase ScrapingCoordinator
│   └── utils/
│       ├── _init_.py
│       └── helpers.py                # Funciones auxiliares
├── tests/
│   ├── _init_.py
│   ├── test_static_page_extractor.py  # Pruebas unitarias de StaticPageExtractor
│   ├── test_dynamic_page_extractor.py # Pruebas unitarias de DynamicPageExtractor
│   ├── test_web_data_extractor.       # Pruebas unitarias de WebDataExtractor
│   ├── test_data_handler.py           # Pruebas unitarias de DataHandler
│   └──test_scraping_coordinator       # Pruebas unitarias de ScrapingCoordinator
├── logs/
│      error.log                      # Para errores críticos.
│      activiti.log                   # Para registrar eventos generales del scraping. 
└── outputs/
```

 A continuación, se describe cada sección de la estructura organiza los componentes del proyecto de scraping web

### Archivos principales:
- **`README.md`**: Documento que detalla el propósito del proyecto, su configuración, cómo utilizarlo y demás aspectos importantes del mismo.
- **`requirements.txt`**: Archivo que lista las dependencias necesarias para ejecutar el proyecto.
- **`setup.py`**: Archivo para empaquetar e instalar el proyecto como módulo.
- **`main.py`**: Punto de entrada principal del programa.
- **`gitinignore`**: Indica archivos y directorios que no deben ser incluidos en el repositorio.

### `src/` - Código Fuente Principal
El núcleo principal del proyecto está dividido en módulos organizados por funcionalidad:

### `base/`
- **`web_data_extractor.py`**: Clase base `WebDataExtractor`, que contiene funcionalidades generales para la extracción de datos.

### `components/`
- **`static_page_extractor.py`**: Clase derivada `StaticPageExtractor`, diseñada para manejar la extracción de datos en páginas estáticas.
- **`dynamic_page_extractor.py`**: Clase derivada `DynamicPageExtractor`, diseñada para la extracción de datos en páginas dinámicas con contenido generado por JavaScript.
- **`data_handler.py`**: Clase `DataHandler` para procesar, limpiar y almacenar los datos extraídos.

### `coordinator/`
- **`scraping_coordinator.py`**: Clase `ScrapingCoordinator` que coordina y administra el flujo del scraping en el proyecto.

### `utils/`
- **`helpers.py`**: Funciones auxiliares y herramientas de apoyo para el proyecto.

### `tests/` - Pruebas Unitarias
Contiene las pruebas para validar los componentes principales del proyecto:
- **`test_static_page_extractor.py`**: Pruebas para `StaticPageExtractor`.
- **`test_dynamic_page_extractor.py`**: Pruebas para `DynamicPageExtractor`.
- **`test_web_data_extractor.py`**: Pruebas para `WebDataExtractor`.
- **`test_data_handler.py`**: Pruebas para `DataHandler`.
- **`test_scraping_coordinator.py`**: Pruebas para el flujo coordinado de scraping.

### `logs/` - Registro de Eventos y Errores
- **`error.log`**: Archivo para registrar errores críticos que ocurran durante la ejecución.
- **`activity.log`**: Archivo para registrar eventos y actividades generales del scraping.

### `outputs/` - Resultados Generados
Carpeta dedicada a almacenar los datos procesados y extraídos en formatos como CSV, JSON, etc.

---

# 💎 **Resultados Esperados**

- Sistema funcional capaz de extraer datos de sitios web tanto estáticos y como dinámicos.
- Almacenamiento organizado de los datos en formatos accesibles.
- Código modular, reutilizable y escalable, que cumpla con los principios de Programcación Orientada a Objetos (POO).
