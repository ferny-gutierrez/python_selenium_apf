from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    def __init__(self, driver: WebDriver, xpathLocalizadorRaiz: str, timeout: int = 10):
        self._driver = driver
        self._timeout = timeout
        self._xpathLocalizadorRaiz = xpathLocalizadorRaiz
        self._esperar = WebDriverWait(self._driver, self._timeout)

    def esperar_hastaque_secargue(self):
        localizadorRaiz = (By.XPATH, self._xpathLocalizadorRaiz)
        self._esperar.until(EC.presence_of_element_located(localizadorRaiz))

    def set_default_timeout(self, timeout: int):
        if type(timeout) == int:
            self._timeout = timeout
            self._esperar = WebDriverWait(self._driver, self._timeout)
        else:
            raise ValueError(f'Valor invalido para timeout {timeout}')

    def get_default_timeout(self) -> int:
        return self._timeout
    
    def get_elementoRaiz(self) -> WebElement:
        localizadorRaiz = (By.XPATH, self._xpathLocalizadorRaiz)
        return self._esperar.until(EC.presence_of_element_located(localizadorRaiz))

    def get_hijo(self, xpath):
        xpathHijo = self.concatenarXpathHijo_conXpathRaiz(xpath)
        localizadorHijo = (By.XPATH, xpathHijo)
        return self._esperar.until(EC.visibility_of_element_located(localizadorHijo))

    def get_hijos(self, xpath):
        xpathHijos = self.concatenarXpathHijo_conXpathRaiz(xpath)
        localizadorHijos = (By.XPATH, xpathHijos)
        return self._esperar.until(EC.visibility_of_all_elements_located(localizadorHijos))

    def concatenarXpathHijo_conXpathRaiz(self, xpathHijo) -> str:
        return self._xpathLocalizadorRaiz + xpathHijo