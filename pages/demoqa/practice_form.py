""" logica para controlar el formulario de control de practicas"""
from selenium.webdriver.common.keys import Keys

from test_base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PracticeForm(BasePage):
    """ formulario de practicas"""

    __URL = "https://demoqa.com/automation-practice-form"
    __SUBMIT_LOCATOR = (By.ID, 'submit')
    __FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    __LAST_NAME_LOCATOR = (By.ID, 'lastName')
    __EMAIL_LOCATOR = (By.ID, 'userEmail')
    __MOBILE_LOCATOR = (By.ID, 'userNumber')
    __CURRENT_ADRESS_LOCATOR = (By.ID, 'currentAddress')
    __SUBJECTS_LOCATOR =  (By.ID, 'subjectsInput')
    __SUBJECTS_SELECTED_LOCATOR = (By.XPATH,"//*[contains(@class, 'subjects-auto-complete__multi-value__label')]")
    __GENDER_LOCATOR_XPATH = "//*[@name='gender' and @value='{0}']/following-sibling::label"
    __HOBBIES_LOCATOR_XPATH = "//label[contains(@for, 'hobbies') and text()='{0}']"
    __DATE_LOCATOR = (By.ID,'dateOfBirthInput')
    __FILE_LOCATOR = (By.ID, 'uploadPicture')

    __STATE_ITEM_LOCATOR_XPATH = "//*[@id='state']//*[contains(@class,'-option') and text()='{0}']"
    __STATE_LOCATOR = (By.ID, 'state')

    __CITY_ITEM_LOCATOR_XPATH = "//*[@id='city']//*[contains(@class,'-option') and text()='{0}']"
    __CITY_LOCATOR = (By.ID, 'city')

    __STATE_VALUE_LOCATOR = (By.XPATH, "//*[@id='state']//*contains(@class,'-singleValue')")
    __CITY_VALUE_LOCATOR = (By.XPATH, "//*[@id='city']//*contains(@class,'-singleValue')")

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver,timeout,self.__URL)

    def wait_until_loaded(self):
        """
        Método que verifica que se cumpla la condicion suministrada
        :return:
        """
        self._wait.until(EC.element_to_be_clickable(self.__SUBMIT_LOCATOR))

    def get_first_name(self):
        return self.__get_input_value(self.__FIRST_NAME_LOCATOR)

    def set_first_name(self, value: str):
        self.__set_input_value(self.__FIRST_NAME_LOCATOR, value)

    def get_last_name(self):
        return self.__get_input_value(self.__LAST_NAME_LOCATOR)

    def set_last_name(self, value: str):
        self.__set_input_value(self.__LAST_NAME_LOCATOR,value)

    def set_email(self, value: str):
        self.__set_input_value(self.__EMAIL_LOCATOR,value)

    def set_mobile(self, value: str):
        self.__set_input_value(self.__MOBILE_LOCATOR,value)

    def get_subjects(self) -> list:
        elements = self._driver.find_elements(*self.__SUBJECTS_SELECTED_LOCATOR)
        values = []
        for element in elements:
            values.append(element.text)
        return values

    def set_subjects(self, value: str):
        self.__set_input_autocomplete_value(self.__SUBJECTS_LOCATOR, value)

    def set_current_address(self, value: str):
        self.__set_input_value(self.__CURRENT_ADRESS_LOCATOR,value)

    def set_gender(self, value:str):
        tmp_xpath = self.__GENDER_LOCATOR_XPATH.format(value)
        tmp_locator = (By.XPATH, tmp_xpath)
        element = self._wait.until(EC.element_to_be_clickable(tmp_locator))
        element.click()

    def set_hobbies(self, value:str):
        tmp_xpath = self.__HOBBIES_LOCATOR_XPATH.format(value)
        print (tmp_xpath)
        tmp_locator = (By.CSS_SELECTOR, tmp_xpath)
        element = self._wait.until(EC.element_to_be_clickable(tmp_locator))
        element.click()

    def get_date_of_birth(self):
        return self.__get_input_value(self.__DATE_LOCATOR)

    def set_date_of_birth(self, value):
        element = self._wait.until(EC.element_to_be_clickable(self.__DATE_LOCATOR))
        self.set_value_attribute(element, value)

    def get_file(self):
        return self.__get_input_value(self.__FILE_LOCATOR)

    def set_file(self, value):
        element = self._wait.until(EC.element_to_be_clickable(self.__FILE_LOCATOR))
        self.__set_input_value(element,value)

    def set_state(self, value: str):
        """
        Metodo para expandir el dropdown
        :param value:
        :return:
        """
        # Paso 1: Expandir el dropdown
        element = self._wait.until(EC.element_to_be_clickable(self.__STATE_LOCATOR))
        element.click()
        # Paso 2: Seleccionar el valor del dropdown

        tmp_itemLocator = (By.XPATH, self.__STATE_ITEM_LOCATOR_XPATH.format(value))
        item = self._wait.until(EC.element_to_be_clickable(tmp_itemLocator))

        # Paso 3: Hacer click en el item
        item.click()

    def get_state(self):
        element = self._wait.until(EC.element_to_be_clickable(self.__STATE_VALUE_LOCATOR))
        return element.text

    def set_city(self, value: str):
        """
        Metodo para expandir el dropdown
        :param value:
        :return:
        """
        # Paso 1: Expandir el dropdown
        element = self._wait.until(EC.element_to_be_clickable(self.__CITY_LOCATOR))
        element.click()
        # Paso 2: Seleccionar el valor del dropdown

        tmp_itemLocator = (By.XPATH, self.__CITY_ITEM_LOCATOR_XPATH)
        item = self._wait.until(EC.element_to_be_clickable(tmp_itemLocator))
        item.click()

    def get_city(self):
        element = self._wait.until(EC.element_to_be_clickable(self.__CITY_VALUE_LOCATOR))
        return element.text
# ------------------------- Genericos -----------------------------------------------

    def __get_input_value(self, locator):
        element = self._wait.until(locator)
        return element.get_attribute('value')

    def __set_input_value(self, locator, value):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)

    def __set_input_autocomplete_value(self,locator, value):
        # Se espera hasta que se cargue el input text que hace parte del control
        element = self._wait.until(EC.element_to_be_clickable(locator))
        # Se limpia lo que haya dentro del input text
        element.clear()
        # Se envia el valor que se desee cargar en el input text
        element.send_keys(value)
        # Se busca el div que se carga en el autocompletar una vez se digita el valor (las sugerencias que se visualizan en el control)
        tmp_xpath = (By.XPATH, f"//*[contains(@class, 'subjects-auto-complete__menu-list')]//*[text()='{value}']")
        # Se espera hasta que el div anterior se cargue en la pagina
        self._wait.until(EC.element_to_be_clickable(tmp_xpath))
        # Se envia la tecla TAB para confirmar el valor digitado en el input text
        element.send_keys(Keys.TAB)

