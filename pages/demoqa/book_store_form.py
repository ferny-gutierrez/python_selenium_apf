from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BookStore(BasePage):
    __URL = "https://demoqa.com/books"
    __INPUT_LOCALIZADOR = (By.ID, 'searchBox')
    __FILAS_TABLA_LOCALIZADOR = (By.XPATH, "//*[@class='rt-tbody']//*[@class = 'rt-tr-group']")

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver,timeout,self.__URL)

    def buscar(self, valor: str):
        elemento: WebElement = self._wait.until(EC.visibility_of_element_located(self.__INPUT_LOCALIZADOR))
        elemento.clear()
        elemento.send_keys(valor)

    def obtener_info_table(self) -> dict:
        filas: WebElement = self._wait.until(EC.visibility_of_all_elements_located(self.__FILAS_TABLA_LOCALIZADOR))
        diccionario_tabla = {}
        for indice,fila in enumerate(filas) :
            celdas: WebElement = fila.find_elements_by_xpath(".//*[@role='gridcell']")
            print(fila.text)
            titulo = celdas[1].text
            autor = celdas[2].text
            editorial = celdas[3].text
            diccionario_tabla[indice] = { 'titulo': titulo, 'autor' : autor, 'editorial': editorial}
            for celda in celdas:
                print(celda.text)
        return diccionario_tabla

def wait_until_loaded(self):
    """
    Método que verifica que se cumpla la condicion suministrada
    :return:
    """
    self._wait.until(EC.visibility_of_element_located(self.__INPUT_LOCALIZADOR))
