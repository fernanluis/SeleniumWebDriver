import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class homePageTests(unittest.TestCase):

    def setUp(self):
        #pass
        # ejecutable path que se encuentra justo en la misma carpeta en el archivo chromedriver
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        # después le decimos que driver es igual a self.driver para no estar repitiendo el código
        driver = self.driver
        # para dirigirnos a nuestro sitio web donde se ejecutarán las pruebas
        driver.get("http://demo.onestepcheckout.com/")
        # después le pedimos al navegador que maximize la ventana ya que puede haber elementos responsivos que cambien su ubicación u orden dependiendo del tamaño de la vista
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_search_text_field(self):
        #pass
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        #pass
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        #pass
        search_field = self.driver.find_element_by_class_name("input-text")#input-text required-entry solo se copia la primera parte

    def test_search_button_enabled(self): # verificar que botón esté disponible
        # pass
        button = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        #pass
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
    	vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img[1]')

    def test_shopping_cart(self):
        #pass
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        #pass
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = "Report", report_name = "home-page-report"))
