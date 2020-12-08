from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.expedia.base_component import BaseComponent

class InputAutoCompletar(BaseComponent):

    __INPUT_AUTOCOMPLETAR_XPATH = "//input[@autocomplete]"
    __OPCIONES_AUTOCOMPLETAR_XPATH = "//li/button"

    def __init__(self, driver: webdriver, localizadorRaiz: str, timeout: int = 10):
        super().__init__(driver, localizadorRaiz, timeout)

    def __iniciarInput(self):
        self.get_elementoRaiz().click()

    def colocar_valor(self, valor):
        self.__iniciarInput()
        textbox_digita: WebElement = self.get_hijo(self.__INPUT_AUTOCOMPLETAR_XPATH)
        textbox_digita.send_keys(valor)
        opciones_autocompletar = self.get_hijos(self.__OPCIONES_AUTOCOMPLETAR_XPATH)
        if len(opciones_autocompletar) > 0:
            opciones_autocompletar[0].click()

