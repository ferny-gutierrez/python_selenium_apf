from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.expedia.hospedaje import Hospedaje
from pages.base_page import BasePage

class HomeExpediaPage(BasePage):
    __URL = 'https://www.expedia.mx'
    __HEADER_LOGO_LOCALIZADOR = (By.XPATH,"//*[contains(@class,'header-logo')]")
    __LISTAR_PROPIEDADES_LOCALIZADOR = (By.ID, 'listYourProperty')
    __AYUDA_LOCALIZADOR = (By.ID, 'support-cs')
    __VIAJES_LOCALIZADOR = (By.ID, 'itinerary')
    __HOSPEDAJE_LOCALIZADOR_RAIZ = "//*[@id='wizard-hotel-pwa-v2']"
    __BUSQUEDA_TABS_LOCALIZADOR = (By.XPATH, "//*[@id='uitk-tabs-button-container']//li")

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver,timeout,self.__URL)
        self.hospedaje = Hospedaje(self._driver, self.__HOSPEDAJE_LOCALIZADOR_RAIZ, self._timeout)

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

    def seleccionar_tab (self, nombre_tab: str):
        tabs = self._wait.until(EC.visibility_of_all_elements_located(self.__BUSQUEDA_TABS_LOCALIZADOR))
        if nombre_tab.lower() == 'stays' and len(tabs) >= 1:
            tabs[0].click()
        elif nombre_tab.lower() == 'flights' and len(tabs) >= 2:
            tabs[1].click()
        elif nombre_tab.lower() == 'cars' and len(tabs) >= 3:
            tabs[2].click()
        elif nombre_tab.lower() == 'packages' and len(tabs) >= 4:
            tabs[3].click()
        elif nombre_tab.lower() == 'things_to_do' and len(tabs) >= 5:
            tabs[4].click()
        else:
            raise ValueError (f'opción no valida:{nombre_tab}')