# -*- coding: utf-8 -*-
from selenium import webdriver #para abrir o navegador e controlar 
from selenium.webdriver.common.keys import Keys # para controlar as teclas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time
import random
#Variaveis 
driver = webdriver.Chrome(executable_path=r'Z:\SERVICE-DESK\Robo Beta\chromedriver.exe')
email = "servicedesk.robo15@gmail.com"
senha = "Sd2019monitoracao"
#driver = webdriver.Chrome('')
disponivel = ""
listr = ["https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html", "https://www.dafiti.com.br/Jogo-de-Banho-5pcs-Buddemeyer-Oxford-Azul-4076766.html", "https://www.dafiti.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html", "https://www.dafiti.com.br/Kit-10pcs-Meia-Lupo-Cano-Medio-Liso-Preto-4599000.html"]
urlr = random.choice(listr)
conta = 0
while (conta != 3):
    # Repetir todo procedimento


#Login
    driver.get("https://secure.dafiti.com.br/customer/account/login/")
    time.sleep(2)
    driver.find_element_by_id("LoginForm_email").clear()
    driver.find_element_by_id("LoginForm_email").send_keys(email)
    driver.find_element_by_id("LoginForm_email").send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_id("LoginForm_password").send_keys(senha)
    driver.find_element_by_id("LoginForm_password").send_keys(Keys.RETURN)
    time.sleep(3)
    print("Login Realizado com sucesso...")
#Compra
    driver.get("https://www.dafiti.com.br/")
    driver.get(urlr)#Lista aleatoria
    print("Item selecionado ")

    resultado = driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').text
    #texto = resultado.text
    if resultado == "Comprar":
        print("Produto disponivel")
        #Seleciona o tamanho

        time.sleep(5)
        
            
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath(u"//img[@alt='Calçados, Sapatos, Roupas e Acessórios na Dafiti']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='wrapper']/div[2]/div[2]/div/div/div[3]/div[3]/a/span").click()
        try:
             sac = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')).text
        except NoSuchElementException:
           pass
        

        if sac == "Sua sacola está vazia...":
            print("funfo")

            pass

       #Carrinho
        try:
            driver.find_element_by_link_text(u"Não adicionar e ir para o Checkout").click()
            time.sleep(3)

        except NoSuchElementException:
            pass

        # Adiciona ao carrinho 
        #driver.get("https://secure.dafiti.com.br/cart/")
        time.sleep(5)  
        # Entra no carrinho      
        #driver.find_element(By.CSS_SELECTOR, ".cart-preview-icon").click()
        
        driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/i").click()
        driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/ul/li").click()
        print("Selecionado no carrinho")
        time.sleep(3)
        driver.find_element_by_id("button-finalize-order-1").click()

        
        #cards = driver.find_element_by_xpath('//*[@id="cart_form"]/div[2]/div[1]/p').text
        #print (cards)
        #Clica em ir para sacola
                
        
        time.sleep(5)

            

        try:                     

            #driver.find_element_by_xpath('//*[@id="paymentMethodForm"]/div[2]/div[1]/label').click()
            #driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()
            #time.sleep(5)
            #driver.get("https://checkout.dafiti.com.br/checkout/finish/")
            #time.sleep(5)
            driver.find_element_by_xpath('//*[@id="paymentMethodForm"]/div[4]/div[1]/label').click()
            time.sleep(4)
            driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()
            num = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div/div[6]/div/div[1]/h2/span')
            pedido = (num.text)
            print(pedido)
            print("Finalizado")
            time.sleep(7)
            driver.get("https://secure.dafiti.com.br/customer/account/login/")
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[2]/div[1]/ul/li[9]/a').click()
        



        except:
            print("Erro no checkout")
            driver.get("https://secure.dafiti.com.br/customer/account/login/")
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[2]/div[1]/ul/li[9]/a').click()
            time.sleep(4)
    else:

        driver.get("https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html") 
        


        print("Produto disponivel")
        #Seleciona o tamanho

        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath(u"//img[@alt='Calçados, Sapatos, Roupas e Acessórios na Dafiti']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='wrapper']/div[2]/div[2]/div/div/div[3]/div[3]/a/span").click()
        try:
            driver.find_element_by_link_text(u"Não adicionar e ir para o Checkout").click()
            time.sleep(3)

        except NoSuchElementException:
            pass

        # Adiciona ao carrinho 
        #driver.get("https://secure.dafiti.com.br/cart/")
        time.sleep(5)  
        # Entra no carrinho      
        #driver.find_element(By.CSS_SELECTOR, ".cart-preview-icon").click()
        
        driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/i").click()
        driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/ul/li").click()
        print("Selecionado no carrinho")
        time.sleep(3)
        driver.find_element_by_id("button-finalize-order-1").click()

        
        #cards = driver.find_element_by_xpath('//*[@id="cart_form"]/div[2]/div[1]/p').text
        #print (cards)
        #Clica em ir para sacola
                
        
        time.sleep(5)

        try:


            #driver.find_element_by_xpath('//*[@id="paymentMethodForm"]/div[2]/div[1]/label').click()
            #driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()
            #time.sleep(5)
            #driver.get("https://checkout.dafiti.com.br/checkout/finish/")
            #time.sleep(5)
            driver.find_element_by_xpath('//*[@id="paymentMethodForm"]/div[4]/div[1]/label').click()
            time.sleep(4)
            driver.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()
            num = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div/div[6]/div/div[1]/h2/span')
            pedido = (num.text)
            print(pedido)
            print("Finalizado")
            time.sleep(7)
            driver.get("https://secure.dafiti.com.br/customer/account/login/")
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[2]/div[1]/ul/li[9]/a').click()
        



        except:
            print("Erro no checkout")
            driver.get("https://secure.dafiti.com.br/customer/account/login/")
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[2]/div[1]/ul/li[9]/a').click()
            time.sleep(4)







        
        
        
       



        




        


    




    
    conta += 1
    print(conta)
    

driver.close()