from Pms.src.common.driverCommon import drivercommon
from selenium.webdriver.common.by import By
import time
url='http://192.168.2.54:8080/Achievements-admin/longin'
class departmentM:
    def test_departmentM(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[4]/a').click()
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'//*[@id="treeName"]').click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.XPATH, '//*[@id="tree_4_check"]').click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/a[1]').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'/html/body/div/form/div[2]/div/input').send_keys('YYDS_deoartment')
        self.driver.find_element(By.XPATH,'/html/body/div/form/div[3]/div/input').send_keys(9)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/a[2]').click()
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False
    drivercommon().driver.close()