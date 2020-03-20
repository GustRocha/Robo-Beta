# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
import unittest, time, re
import random
email = "dftgustavorocha@gmail.com"
senha = "guri1997"
url2 = ("https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html","https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html")
#url = ["https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html","https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html", "https://www.dafiti.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html", "https://www.dafiti.com.br/Kit-10pcs-Meia-Lupo-Cano-Medio-Liso-Preto-4599000.html"]
#urlr = random.choice(url)
urlr2 = random.choice(url2)
class Teste(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'Z:\SERVICE-DESK\Robo Beta\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_e(self):
        driver = self.driver
        driver.get("https://secure.dafiti.com.br/customer/account/login/")
        driver.find_element_by_id("LoginForm_email").clear()
        driver.find_element_by_id("LoginForm_email").send_keys(email)
        driver.find_element_by_id("LoginForm_email").send_keys(Keys.RETURN)        
        driver.find_element_by_id("LoginForm_email").click()
        time.sleep(2)
        driver.find_element_by_id("LoginForm_password").send_keys(senha)
        driver.find_element_by_id("LoginForm_password").send_keys(Keys.RETURN)
        time.sleep(3)
        print("Login Realizado com sucesso...")
        driver.find_element_by_xpath("//img[@alt='Calçados, Sapatos, Roupas e Acessórios na Dafiti']").click()
        driver.get(urlr)#Lista aleatoria
        time.sleep(5)
        disp = driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').text
        print(disp)
        while disp == "Avise-me":
            driver.get(urlr2)
            print(disp)
            disp = driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').text
            time.sleep(3)
            pass
    
        print("Item escolhido ")

        #Altera o tamanho 
        driver.find_element_by_xpath("//form[@id='add-to-cart']/div[2]/i").click()
        driver.find_element_by_xpath("//form[@id='add-to-cart']/div[2]/ul/li").click()
        try:
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            pass
        except NoSuchElementException:
            pass
        
        resultado = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
        print(resultado)

        if resultado == "" :
            print("Produto Disponivel")
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div/div[3]/div[3]/a/i').click
            time.sleep(3)
            pass
        
        elif resultado == "Esgotado":
            print("Tamanho 2 indisponivel")
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[2]').click()
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            resultado = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
            print(resultado)
            pass
        elif resultado == "" :
            print("Tamanho 3 disponivel")
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[3]').click()
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
            pass
        else:
            print("3 tamanhos indisponiveis, troca de produto")
            driver.get(urlr)
            time.sleep(3)
            print("Trocado")
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
            time.sleep(2)
            pass
        try:
            driver.find_element_by_xpath("//div[@id='wrapper']/div[2]/div[2]/div/div/div[3]/div[3]/a/span").click()
        
        except NoSuchElementException:
            driver.get("https://secure.dafiti.com.br/cart/")
            pass
        pass
        try:
            driver.find_element_by_link_text(u"Não adicionar e ir para o Checkout").click()
            print("Popup fechado")
            pass               

        except NoSuchElementException:
            print("Adicionado na sacola.")
                          
            pass
        
    def check(self):
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[4]/h3'))).text
            time.sleep(5)
            while element != "SUA SACOLA ESTÁ VAZIA..." :
                test_e(self)              
                pass
        except:
            print("Checkout")
            pass          
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    url = ("https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html","https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html", "https://www.dafiti.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html", "https://www.dafiti.com.br/Kit-10pcs-Meia-Lupo-Cano-Medio-Liso-Preto-4599000.html")
    urlr = random.choice(url2)      
    unittest.main()

