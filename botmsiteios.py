# -- coding: utf-8 --
import time, smtplib, os, pyscreenshot
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



servicedesk_email = "servicedesk.robo16@gmail.com"
servicedesk_password = "Sd2019monitoracao"



def comprar(url, site):

	browser.get("https://secure.{}.com.br/customer/account/login/".format(site))

	#login e senha para entrar no site
	#espera pelo elemento
	WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH,"""//*[@id="LoginForm_email"]""")))

	browser.find_element_by_xpath("""//*[@id="LoginForm_email"]""").send_keys(servicedesk_email)
	time.sleep(0.5)
	browser.find_element_by_xpath("""//*[@id="LoginForm_password"]""").send_keys(servicedesk_password)
	time.sleep(0.5)
	browser.find_element_by_xpath("""//*//*[@id="send-2"]""").click()
	time.sleep(4)

	#abre um item
	browser.get(url)
	time.sleep(10)



	#ir para o carrinho
	#fechar popup compre o quanto antes

	try:
		browser.find_element_by_class_name("""hide-box-button""").click()
		time.sleep(5)
	except NoSuchElementException:
		pass
		
	#popup de pesquisa rapida
	browser.find_element_by_xpath("""//*[@id="add-to-cart"]/div/div[3]/button""").click()
	time.sleep(4)
	browser.get("https://secure.{}.com.br/cart/".format(site))
	time.sleep(5)

	#clicar em finalizar compra
	browser.find_element_by_xpath("""//*[@id="button-finalize-order-1"]""").click()
	time.sleep(3)

	#selecionar o boleto
	#browser.find_element_by_xpath("""//*[@id="boleto"]""").click()
	browser.find_element(By.CSS_SELECTOR, ".is-disabled").click()
	time.sleep(7)


	#clicar em finalizar compra
	browser.find_element(By.ID, "btn_finalize_order").click()
	time.sleep(5)
	
	#espera o numero do pedido
	
	numero_pedido = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"""//span[@class="sel-order-nr"]"""))).text

	#pega o horário
	hora = datetime.today()
	#mostra numero do pedido e hora
	pedidos.append((numero_pedido, hora))
	print(numero_pedido, hora, site)



def enviar_email(erro, site):
	#login no meail
	de = servicedesk_email
	para ="dft.servicedesk@dafiti.com.br"
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

	

	#lista de skus para buscar

	mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
	"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

	chrome_options = Options()

	chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

	browser = webdriver.Chrome(chrome_options = chrome_options)


	skus = []
	# Trocar url do produto abaixo
	urls = [
    'https://m.dafiti.com.br/Kit-3pcs-Meia-Trifil-Sport-Soquete-Lisa-Preto/Branco/Cinza-5081845.html',
	'https://www.kanui.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html',
	'https://www.tricae.com.br/Bolsa-Capodarte-Logo-Caramelo-4690776.html']

	sites = ['dafiti', 'kanui', 'tricae']

	pedidos = []

	# tente
	try:
		
		for url,site in zip(urls,sites):
			comprar(url, site)
		
		
		
	# exceto erro
	except Exception as erro:
		browser.save_screenshot('error.png')
		enviar_email(erro, site)
		# força o erro e interrupção do script
		raise
	browser.quit()
	
