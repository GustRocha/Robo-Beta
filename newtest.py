
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
email = "dftgustavorocha@gmail.com"
senha = "guri1997"
url = ["https://www.dafiti.com.br/Top-Lupo-Sport-Raschel-Preto-5130788.html"]
urlr = random.choice(url)
conta = 0


	


def Login(email, senha):
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
		


		


	#Abrir o produto
def Selecionar(urlr):
		driver.get("https://www.dafiti.com.br/")
		driver.get(urlr)#Lista aleatoria
		time.sleep(5)
		
		print("Item escolhido ")        
		resultado = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
		print(resultado)
		if resultado != "Esgotado":
			print("Produto disponivel")
			#Altera o tamanho            
			time.sleep(5)
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[1]').click()
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
			time.sleep(5)
			estoque = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
			print(estoque)

			if estoque == "":
				print("Produto Disponivel")
		
				if estoque == "Esgotado":
					print("Tamanho 2 indisponivel")
					driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
					driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[2]').click()
					driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
					estoque = driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/div/span[2]').text
					print(estoque)
					if estoque == "":
						print("Tamanho 3 disponivel")
						driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
						driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[3]').click()
						driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
					else:

						print("3 tamanhos indisponiveis, troca de produto")
						driver.get(urlr)
						time.sleep(3)
						print("Trocado")
						driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
						time.sleep(2)
			try:
				driver.find_element_by_xpath("//div[@id='wrapper']/div[2]/div[2]/div/div/div[3]/div[3]/a/span").click()
			except NoSuchElementException:
				driver.get("https://secure.dafiti.com.br/cart/")
				pass        
		else:
			print("Passou")

			#Altera o tamanho
			time.sleep(5)
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/i').click()
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/div[2]/ul/li[1]').click()
			driver.find_element_by_xpath('//*[@id="add-to-cart"]/button').click()
			time.sleep(5)
			#Volta para pagina inicial e clicka na sacola
			driver.find_element_by_xpath(u"//img[@alt='Calçados, Sapatos, Roupas e Acessórios na Dafiti']").click()
			time.sleep(5)
			try:
				driver.find_element_by_xpath("//div[@id='wrapper']/div[2]/div[2]/div/div/div[3]/div[3]/a/span").click()
			
			except NoSuchElementException:

				driver.get("https://secure.dafiti.com.br/cart/")
				pass
			pass


		
def sacola():


	try:
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[4]/h3'))).text
		time.sleep(5)
		while element =="SUA SACOLA ESTÁ VAZIA..." :
			Selecionar()              
		pass
	except:
		pass 
			
def carrinho():	
	
   
	try:

		driver.find_element_by_link_text(u"Não adicionar e ir para o Checkout").click()
		time.sleep(3)
	except NoSuchElementException:
		driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/i").click()
		driver.find_element_by_xpath("//form[@id='cart_form']/div/div[2]/div/div[3]/div[3]/a/ul/li").click()
		print("Selecionado no carrinho")
		time.sleep(3)
		driver.find_element_by_id("button-finalize-order-1").click()  
		time.sleep(5)
		pass   
	try:
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

					
while (conta <= 3):

	Login(email, senha)
	time.sleep(4)
	Selecionar(urlr)
	time.sleep(5)
	sacola()
	time.sleep(5)
	carrinho()
	pass
	conta += 1
	print(conta)

driver.close()

