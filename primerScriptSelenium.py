# importar librería unittest para traer todas las pruebas
import unittest
# desde el módulo de PyUnitReport se va a importar el HTMLTestRunner
# que ayudará a orquestar cada una de las pruebas que se estén ejecutando
# junto con los reportes
from pyunitreport import HTMLTestRunner
# después,desde el módulo de Selenium que ya está instalado vamos a
# vamos a importar el submódulo webdriver para poder así
# comunicarnos con el navegador.
from selenium import webdriver

# Crear una clase que estará haciendo referencia a unittest
# test case qeu serán todos lo casos de pruebas
class HelloWorld(unittest.TestCase):

#    def setUp(self):
    @classmethod
    def setUpClass(cls): # modificar cada self por cls en este método
        #return super().setUp()
        cls.driver = webdriver.Chrome(executable_path = './chromedriver') # r'C://Documents/selenium.exe'
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        #pass
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        #pass
        # con self directamente
        self.driver.get('https://www.wikipedia.org')

    # mismo procedimiento que en setUp
    @classmethod
    def tearDownClass(cls):
        #return super().tearDown()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = "Report", report_name = "hello-world-report"))
