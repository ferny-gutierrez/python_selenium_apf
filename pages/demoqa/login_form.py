from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginForm(BasePage):

    __URL = "https://demoqa.com/login"
    __USERNAME_LOCALIZADOR = (By.ID, 'userName')
    __PASSWORD_LOCALIZADOR = (By.ID, 'password')
    __BOTON_LOGIN_LOCALIZADOR = (By.ID, 'login')
    __BOTON_NEWUSER_LOCALIZADOR = (By.ID, 'newUser')

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver,timeout,self.__URL)

    def esperar_hasta_que_se_cargue_elemento(self):
        """
        Método que verifica que se cumpla la condicion suministrada
        :return:
        """
        self._wait.until(EC.element_to_be_clickable(self.__BOTON_LOGIN_LOCALIZADOR))

    def set_user_name(self, valor: str):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__USERNAME_LOCALIZADOR))
        elemento.clear()
        elemento.send_keys(valor)

    def set_password(self, valor: str):
        elemento: WebElement = self._wait.until(EC.element_to_be_clickable(self.__PASSWORD_LOCALIZADOR))
        elemento.clear()
        elemento.send_keys(valor)

    def boton_login_click(self):
        elemento = self._wait.until(EC.element_to_be_clickable(self.__BOTON_LOGIN_LOCALIZADOR))
        elemento.click()

# ------------------------- Genericos -----------------------------------------------

    def __get_input_value(self, locator):
        elemento = self._wait.until(locator)
        return elemento.get_attribute('value')

    def __set_input_value(self, locator, valor):
        elemento = self._wait.until(EC.element_to_be_clickable(locator))
        elemento.clear()
        elemento.send_keys(valor)

