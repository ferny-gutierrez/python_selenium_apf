"""Clase base que representa una pagina web mediante el uso de un PageObject"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    __BODY_LOCATOR = (By.TAG_NAME,'body')

    def __init__(self, driver: WebDriver, timeout: int = 10, url: str = None):
        """
        Crea una nueva instancia de BasePage
        :param driver: El driver para controlar el navegador desde el script de automatizacion
        :param timeout: El tiempo de espera global de la pagina
        :param url: La URL a la que se desea ingresar
        """
        self._driver = driver
        self._timeout = timeout
        self._url = url
        self._wait = WebDriverWait(driver, timeout)
        self._tab_navegador_actual = None

    def abrir_pagina_web(self):
        """
        Abre la pagina web indicada en el parametro de entrada
        :return:
        """
        self._driver.get(self._url)
        self._tab_navegador_actual = self._driver.current_window_handle

    def cerrar_navegador(self):
        """
        Cierra el navegador a traves del webdriver
        :return:
        """
        self._driver.close()

    def get_default_timeout(self) -> int:
        """
        Retorna el timeout parametrizado por defecto
        :return: Timeout en segundos
        """
        return self._timeout;

    def set_default_timeout(self, newTimeout: int):
        """
        Establece el valor para esperas explicitas
        :param newTimeout: valor en segundos de la expera explicita
        :return:
        """
        if type(newTimeout) == int:
            self._timeout = newTimeout
            self._wait = WebDriverWait(self._driver, self._timeout)
        else:
            raise ValueError(f"Valor invalido para timeout {newTimeout}")

    def refrescar_pagina(self):
        """
        Método que refresca la pagina actual
        :return:
        """
        self._driver.refresh()

    def esperar_hasta_que_se_cargue_elemento(self):
        """
        Método que verifica que el tag body se carge antes de continuar
        :return:
        """
        self._wait.until(EC.visibility_of_element_located(self.__BODY_LOCATOR))

    def set_value_attribute(self, element, value):
        self._driver.execute_script("arguments[0].value = '{value}'", element)

    def moverse_a_tab_principal(self):
        self._driver.switch_to.window(self._tab_navegador_actual)
