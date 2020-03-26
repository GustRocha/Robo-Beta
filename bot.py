import time, smtplib, os, pyscreenshot, openpyxl, random
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait	
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Servicedesk_email = "dft.servicedesk@dafiti.com.br"
servicedesk_email_login = "servicedesk.robo6@gmail.com"
servicedesk_password = "Sd2019monitoracao"

links = ('https://www.dafiti.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html', 'https://www.dafiti.com.br/Bolsa-Santa-Lolla-Croco-Marrom-4474115.html', 
'https://www.dafiti.com.br/Bolsa-Colcci-Redonda-Preta-3797015.html')
itens = random.choice(links)
browser.get("https://secure.{}.com.br/customer/account/login/".format(site))
time.sleep(5)
browser.find_element_by_xpath("""//*[@id="wrapper"]""").click()
time.sleep(2)
#login e senha para entrar no site
#espera 10 segundos pelo elemento
browser.find_element_by_xpath("""//*[@id="LoginForm_email"]""").send_keys(servicedesk_email_login)
time.sleep(0.5)
browser.find_element_by_xpath("""//*[@id="LoginForm_password"]""").send_keys(servicedesk_password)
time.sleep(0.5)
browser.find_element_by_xpath("""//*[@id="customer-account-login"]""").click()
time.sleep(4)

def comprar(url, site):


	#abre um item
	browser.get(url)
	time.sleep(8)
	produto_esgotado = browser.find_element_by_xpath("""//*[@id="stock-available"]/div[2]""").text
	if produto_esgotado == 'Produto Esgotado':
		print('produto esgotado')
		def comprar(url, site):

		
	else:	
			browser.find_element_by_xpath("""//*[@id="add-to-cart"]/button""").click()
			time.sleep(4)
			browser.get('https://secure.dafiti.com.br/cart/')
			time.sleep(5)
			print('entrando na sacola')
			sacola_vazia = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="wrapper"]/div[4]/h3"""))).text

			if sacola_vazia == 'SUA SACOLA ESTÁ VAZIA...': 
				print('sacola vazia')
				browser.get(itens)
				browser.find_element_by_xpath("""/html/body/div[4]/div[5]/div[3]/div[2]/div[2]/div[2]/form/button""").click()
				time.sleep(4)
				#carrinho = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="wrapper"]/div[2]/div[3]/div/div/div[3]/div[4]/div[2]/a""")))
				#carrinho.click()
				browser.get('https://secure.dafiti.com.br/cart/')
				time.sleep(3)
				item_carrinho = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="cart_form"]/div[1]/div[2]/div/div[3]/div[3]/a/div"""))).text

				if item_carrinho > '1':

					print('ha {} item no carrinho'.format(item_carrinho))
					time.sleep(2)

					browser.find_element(By.CSS_SELECTOR,".cart-product:nth-child(2) .cart-product-options-item:nth-child(3) .selectbox-icon").click()
					time.sleep(2)

					print('botao encontrado')
					browser.find_element_by_xpath("""/html/body/div[5]/div[4]/div[4]/form/div[1]/div[2]/div/div[3]/div[3]/a/ul/li[1]""").click()
					time.sleep(2)

					browser.find_element_by_xpath("""//*[@id="button-finalize-order-1"]""").click()
					time.sleep(4)

					#selecionar o boleto
					browser.find_element(By.CSS_SELECTOR, ".is-disabled").click()
					time.sleep(1)

					#clicar em finalizar compra
					browser.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()

					#espera o numero do pedido
					numero_pedido = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"""//span[@class="sel-order-nr"]"""))).text

				else:
					itens_sacola = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"""//span[@class="sel-order-nr"]"""))).text
					if itens_sacola == 'VOCÊ POSSUI PRODUTOS GUARDADOS NA SACOLA (1)':
						print('ha itens no carrinho')
						browser.find_element_by_xpath("""//*[@id="wrapper"]/div[4]/div[7]/div/form/div[2]/div/div[2]/a""").click()
						time.sleep(5)
						browser.find_element(By.CSS_SELECTOR, ".is-disabled").click()
						time.sleep(1)
	
						browser.find_element_by_xpath("""//*[@id="paymentMethodForm"]/div[4]/div[1]/label""").click()
						time.sleep(1)

						#clicar em finalizar compra
						browser.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()

						#espera o numero do pedido
						numero_pedido = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"""//span[@class="sel-order-nr"]"""))).text
	
						hora = datetime.today()
						#mostra numero do pedido e hora
						pedidos.append((numero_pedido, hora))
						print(numero_pedido, hora, site)
					else:
					
						#ir para o carrinho
						time.sleep(8)
						
						#clicar em finalizar compra
						browser.find_element_by_xpath("""/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[3]/a[1]""").click()
						time.sleep(4)

						#selecionar o boleto
						browser.find_element(By.CSS_SELECTOR, ".is-disabled").click()
						time.sleep(1)
	

						browser.find_element_by_xpath("""//*[@id="paymentMethodForm"]/div[4]/div[1]/label""").click()
						time.sleep(1)

						#clicar em finalizar compra
						browser.find_element_by_xpath("""//*[@id="btn_finalize_order"]""").click()

						#espera o numero do pedido
						numero_pedido = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"""//span[@class="sel-order-nr"]"""))).text

	
						hora = datetime.today()
						#mostra numero do pedido e hora
						pedidos.append((numero_pedido, hora))
						print(numero_pedido, hora, site)

def enviar_email(erro, site):
	#login no email
	de = "servicedesk.robo6aaaaaa@gmail.com"
	para = ""
	senha = "Sd2019monitoracao"
	msg = MIMEMultipart()
	msg ['From'] = de
	msg['To'] = para
	msg['Subject'] = "Erro na compra"

	body = "Ocorreu um erro na compra do site [{1}]:\n({0})".format(erro, site)

	# anexa imagem
	image = MIMEImage(open('error.png','rb').read())
	msg.attach(image)
	# anexa o texto
	msg.attach(MIMEText(body, 'plain'))

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(de, senha)
	s.sendmail(de, para, msg.as_string())
	print('mensagem enviada')
	s.quit()


# AQUI COMECA RODAR O CODIGO
if __name__ == "__main__":

	chrome_options = webdriver.ChromeOptions()

	prefs = {
	"profile.default_content_setting_values.notifications": 2,
	#"deviceName": "Galaxy S5" 
	}

	#inicia maximizado
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("prefs", prefs)

	browser = webdriver.Chrome(options=chrome_options)
	
	
	browser.set_page_load_timeout(60)

	skus = []
	#Trocar as urls dos produtos abaixo
	urls = [
	'https://www.dafiti.com.br/Kit-3-pcs-Meia-Quiksilver-Ano-Todo-Preta%2FCinza%2FBranca-4111229.html'
	]

	sites = ['dafiti']

	pedidos = []

	# tente
	try:
		
		for url,site in zip(urls,sites):
			comprar(url, site)
		
		

	# exceto erro
	except Exception as erro:
		browser.save_screenshot('error.png')
		enviar_email(erro, site)
		browser.quit()

	browser.quit()
