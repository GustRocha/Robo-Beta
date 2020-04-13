# -*- coding: utf-8 -*-
import smtplib, os, pyscreenshot
from datetime import datetime
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
url = ("https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html","https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html")
url2 = ("https://www.dafiti.com.br/Kit-10pcs-Cueca-Lupo-Boxer-Logo-Grafite%2FBranco%2FPreto-4594938.html","https://www.dafiti.com.br/Kit-10pcs-Cueca-Lupo-Boxer-Logo-Grafite%2FBranco%2FPreto-4594938.html")
rand = random.choice(url)
rand2 = random.choice(url2)

class TestDafit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)        
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dafit(self):
        driver = self.driver
        #Login
        driver.get("https://www.dafiti.com.br/")
        try:
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div/div[3]/div[1]/div[1]/a[1]').click()
            pass
        except NoSuchElementException:
            driver.get("https://secure.dafiti.com.br/customer/account/login/")
            pass
        try:
            driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div/button/i').click()
            print("Fechou o anuncio")
            pass
        except NoSuchElementException:
            print("Nao apareceu anuncio")
            pass

        driver.find_element_by_id("LoginForm_email").clear()
        driver.find_element_by_id("LoginForm_email").send_keys(email)
        driver.find_element_by_id("LoginForm_email").send_keys(Keys.RETURN)        
        driver.find_element_by_id("LoginForm_email").click()
        time.sleep(2)
        driver.find_element_by_id("LoginForm_password").send_keys(senha)
        driver.find_element_by_id("LoginForm_password").send_keys(Keys.RETURN)
        time.sleep(3)
        print("Login Realizado com sucesso...")
        #Entra no url
        driver.get(rand)#lista de url
        time.sleep(5)
        #Verifica se o produto esta disponivel
        disp = driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').text
        print(disp)
        while disp == "Avise-me":
            driver.get(rand2)
            time.sleep(5)
            disp = driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').text
            print(disp)
            pass

        print("Produto disponivel")

        tam = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div').text
        print(tam)
        time.sleep(3)
        try:
            driver.find_element_by_class_name("block-information-null-products").click()
            print("Fechou pop-up")
            pass
        except NoSuchElementException:
            pass

        if tam == "Selecione o tamanho...": 
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[1]').click()
            time.sleep(2)
            estoque = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
            print(estoque)
            time.sleep(3)
            #Apertar o botão do pop up de sem stock
            try:
                driver.find_element_by_class_name("modal-close icon-cross").click()
                print("Apertou acabou")
                time.sleep(3)
                pass
            except NoSuchElementException:
                pass
            pass            

        elif estoque == "Esgotado":
            driver.find_element_by_xpath("//form[@id='add-to-cart']/div[2]/i").click()
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[2]').click()
            est = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
            print(est)
            pass
        elif est == "Esgotado":
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
            driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[3]').click()
            esto = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
            print(est)
            print("Tamanhos indisponiveis, favor trocar")
            driver.quit()
        else:
            driver.find_element_by_xpath("(//button[@type='submit'])[4]").click()
            time.sleep(3)   
            print("Adicionado na sacola")
            pass

        time.sleep(3)
        driver.find_element_by_xpath("(//button[@type='submit'])[4]").click()
        print("Adicionado na sacola")

        #Tentar entrar na sacola pelo botão 
        try:
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div/div[3]/div[3]/a/i').click()
            time.sleep(3)
            print("Entrou pelo botão")
            pass
        except NoSuchElementException:
            driver.get("https://secure.dafiti.com.br/cart/")
            time.sleep(3)
            print("Entrou pelo link")
            pass
        try:
            driver.find_element_by_class_name("modal-close").click()
            print("Apertou")
            time.sleep(2)
            pass
        except NoSuchElementException:
            print("Nao Apertou")
            pass

        #vazio = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/h3').text
        
        itens_sacola = driver.find_element_by_xpath('//*[@id="cart_form"]/div[1]/div[1]/p').text
        if itens_sacola == '1 Item':
            print('ha itens no carrinho')
            #clicar em finalizar compra
            driver.find_element_by_xpath("""/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[3]/a[1]""").click()
            time.sleep(4)

            #selecionar o boleto
            driver.find_element(By.CSS_SELECTOR, ".is-disabled").click()
            time.sleep(1)


            driver.find_element_by_xpath("""//*[@id="paymentMethodForm"]/div[4]/div[1]/label""").click()
            time.sleep(1)

            #clicar em finalizar compra
            driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()

            #espera o numero do pedido
            numero_pedido = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,"""//*[@id="wrapper"]/div[4]/div/div[2]/div/div[6]/div/div[1]/h2/span"""))).text


            hora = datetime.today()
            #mostra numero do pedido e hora
            print(numero_pedido, hora)

        else:   
            print(itens_sacola)
            driver.find_element_by_xpath('//*[@id="cart_form"]/div[1]/div[2]/div/div[3]/div[3]/a/i').click()
            driver.find_element_by_xpath('//*[@id="cart_form"]/div[1]/div[2]/div/div[3]/div[3]/a/ul/li[1]').click()
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="button-finalize-order-1"]').click()
             #selecionar o boleto
            driver.find_element(By.CSS_SELECTOR, ".is-disabled").click()
            time.sleep(1)


            driver.find_element_by_xpath("""//*[@id="paymentMethodForm"]/div[4]/div[1]/label""").click()
            time.sleep(1)

            #clicar em finalizar compra
            driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()

            #espera o numero do pedido
            numero_pedido = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,"""//*[@id="wrapper"]/div[4]/div/div[2]/div/div[6]/div/div[1]/h2/span"""))).text

            hora = datetime.today()
            #mostra numero do pedido e hora
            print(numero_pedido, hora)


        
           

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
    unittest.main()

