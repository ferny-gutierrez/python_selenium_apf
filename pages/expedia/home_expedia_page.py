from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomeExpediaPage(BasePage):
    __URL = 'https://www.expedia.mx'
    __HEADER_LOGO_LOCALIZADOR = (By.XPATH,"//*[contains(@class,'header-logo')]")
    __LISTAR_PROPIEDADES_LOCALIZADOR = (By.ID, 'listYourProperty')
    __AYUDA_LOCALIZADOR = (By.ID, 'support-cs')
    __VIAJES_LOCALIZADOR = (By.ID, 'itinerary')

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver,timeout,self.__URL)

    def esperar_hasta_que_se_cargue_elemento(self):
        """
        Método que verifica que se cumpla la condicion suministrada
        :return:
        """
        self._wait.until(EC.visibility_of_element_located(self.__HEADER_LOGO_LOCALIZADOR))

    def hacer_click_logo(self):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__HEADER_LOGO_LOCALIZADOR))
        elemento.click()

    def hacer_click_anunciar_una_propiedad(self):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__LISTAR_PROPIEDADES_LOCALIZADOR))
        elemento.click()

    def hacer_click_ayuda(self):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__AYUDA_LOCALIZADOR))
        elemento.click()

    def hacer_click_viajes(self):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__VIAJES_LOCALIZADOR))
        elemento.click()