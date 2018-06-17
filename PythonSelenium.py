from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AmazonLogIn:
    def __init__(self, URL):
        self.URL = URL
        self.driver = webdriver.Chrome(r"C:\Users\SAI_A\Downloads\Selenium\chromedriver_win32\chromedriver.exe")

    def invokeBrowser(self):
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.set_page_load_timeout(60)
        self.driver.get(self.URL)
        self.amazonLogin()

    def amazonLogin(self):

        self.driver.find_element_by_xpath("//span[contains(text(), 'Hello. Sign in')]").click()
        self.driver.find_element_by_id("ap_email").send_keys("xxxxxx@gmail.com")
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("ap_password").send_keys("xxxxxxxx")
        self.driver.find_element_by_id("signInSubmit").click()
        print("Amazon Logged in was successful.")
        self.placeOrder()

    def placeOrder(self):
        self.driver.find_element_by_id("twotabsearchtextbox").click()
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys("Oneplus 6")
        self.driver.find_element_by_xpath("//input[@class='nav-input']").click()
        self.driver.find_element_by_xpath("//span[@id='pdagDesktopSparkleDescription1']").click()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element_by_id("buy-now-button").click()

    def closeDriver(self):
        self.driver.close()
        print("Driver closed successfully.")


def main():
    obj = AmazonLogIn(URL=r'https://www.amazon.in/')
    obj.invokeBrowser()
    obj.closeDriver()

if __name__ == "__main__":
    main()


