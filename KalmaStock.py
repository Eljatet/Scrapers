'''
Created on 28 de mar. de 2016

@author: Javier Ebrero
'''
# -*- coding: utf-8 -*-
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from datetime import datetime
import codecs
import unicodecsv as csv
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from pywin.tools import browseProjects
contError=0
def consumo(URL):
	global browser,f2,f3,contError
	browser.get(URL)
	start2=time.clock()
	sumReal=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/p[2]').text
	sumReal=sumReal.split(" ")
	sumReal=int(sumReal[0])
	sumReal=(sumReal-31)/10
	sumReal+=1
	print(sumReal)
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	try:
		element = WebDriverWait(browser, 30).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
	finally:
		time.sleep(2)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	try:
		element = WebDriverWait(browser, 30).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
	finally:
		time.sleep(2)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
	if(sumReal<1):
		obtenerDatos(URL,start2)
	else:
		try:
			for i in range(sumReal):
				time.sleep(0.3)
				try:
					element = WebDriverWait(browser, 20).until(
					EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div[2]/a')))
					element.click()
				finally:
					try:
						element = WebDriverWait(browser, 20).until(
						EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
					finally:
						time.sleep(1.4)
						browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			print("Correcto")
			obtenerDatos(URL,start2)
		except NoSuchElementException:
			if(contError<=4):
				print("Intento n: "+str(contError))
				contError+=1
				consumo(URL)
			else:
				contError=0
				print(i)
				obtenerDatos(URL,start2)
		except WebDriverException:
			if(contError<=4):
				print("Intento n: "+str(contError))
				contError+=1
				consumo(URL)
			else:
				contError=0
				print(i)
				obtenerDatos(URL,start2)
def obtenerDatos(URL,start3):
	global browser,f2,f3
	suma=0
	sumReal=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/p[2]').text
	sumReal=sumReal.split(" ")
	for r in range(1,10000):
		try:
			for k in range(1,11):
				url=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[1]/h2/a'% (r,k))
				try:
					try:
						element=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[1]/div[2]/p[1]'% (r,k)).text
						element=element[12:]
					except NoSuchElementException:
						element=""
					try:
						Name=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[1]/h2/a'% (r,k)).text
					except NoSuchElementException:
						Name=""
					try:
						Ref_Fabricante=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[1]/div[2]/p[2]'% (r,k)).text
						Ref_Fabricante=Ref_Fabricante[17:]
					except:
						Ref_Fabricante=""
					try:
						Stock=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[4]/div'% (r,k)).text
					except NoSuchElementException:
						Stock=""
					try:
						Precio=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[3]/p[2]'% (r,k)).text
					except NoSuchElementException:
						try:
							Precio=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/ol[%d]/li[%d]/div/div[3]'% (r,k)).text
							Precio=Precio.split(" ")
							Precio=Precio[0]
						except NoSuchElementException:
							Precio=""
					suma+=1
					f3.write(Name+';'+element+';'+Ref_Fabricante+';'+Stock+';'+Precio+';'+'\n')
				except WebDriverException,UnexpectedAlertPresentException:
					f2.write(str(datetime.utcnow())+"  ERROR CLICK PRODUCTO"+'\r\n')
					break;
		except NoSuchElementException:
			print(str(suma)+ "  "+str(sumReal[0]))
			end2=time.clock()
			print(str(int((end2 - start3)/60))+ " minutos")
			print(str(suma)+ " productos")
			f2.write(str(URL)+"  Tiempo en esta URL: "+str(int((end2 - start3)/60))+"  Minutos"+'\r\n')
			f2.write(str(URL)+"  Suma total de productos obtenidos:  "+str(suma)+'\r\n')
			break
		except WebDriverException:
			break
def main():
	global browser,f2,f3
	reload(sys)
	sys.setdefaultencoding('utf-8')
	f2=codecs.open('loggKalma.txt','w','utf-8')
	f3=codecs.open('KalmaStock.txt','wb','utf-8')
	f3.write('Name'+';'+'Referencia'+';'+'Ref_Fabricante'+';'+'Stock'+';'+'Precio'+';'+'\n')
	print(str(datetime.utcnow()))
	#chromedriver = 'C:\chromedriver.exe'
	#browser= webdriver.Chrome(chromedriver)
	start = time.clock()
	browser = webdriver.PhantomJS('C:\phantomjs.exe',service_args=["--webdriver-loglevel=ERROR"])
	browser.set_window_size(1280,1024)
	browser.get("https://kalma.es/index.php/customer/account/login/")
	username = browser.find_element_by_id("email")
	password = browser.find_element_by_id("pass")
	username.clear()
	username.send_keys("pedidos@dentaltix.com")
	password.send_keys("B86142809")
	browser.find_element_by_xpath('//*[@id="send2"]').click()
	time.sleep(0.5)
	for i in range(1,25):
		try:
			try:
				if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
					browser.get('https://kalma.es/index.php')
					element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[1]/div/div/div/a[%d]'% (i))
					href = element.get_attribute('href')
					print(href)
					consumo(href)
			except NoSuchElementException:
					browser.get("https://kalma.es/index.php/customer/account/login/")
					username = browser.find_element_by_id("email")
					password = browser.find_element_by_id("pass")
					username.clear()
					username.send_keys("pedidos@dentaltix.com")
					password.send_keys("B86142809")
					browser.find_element_by_xpath('//*[@id="send2"]').click()
					time.sleep(0.5)
					print("RELOGGEADO")
					browser.get('https://kalma.es/index.php')
					element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[1]/div/div/div/a[%d]'% (i))
					href = element.get_attribute('href')
					print(href)
					consumo(href)
			except WebDriverException:
					browser.get("https://kalma.es/index.php/customer/account/login/")
					username = browser.find_element_by_id("email")
					password = browser.find_element_by_id("pass")
					username.clear()
					username.send_keys("pedidos@dentaltix.com")
					password.send_keys("B86142809")
					browser.find_element_by_xpath('//*[@id="send2"]').click()
					time.sleep(0.5)
					print("RELOGGEADO")
					browser.get('https://kalma.es/index.php')
					element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[1]/div/div/div/a[%d]'% (i))
					href = element.get_attribute('href')
					print(href)
					consumo(href)
		except NoSuchElementException:
			continue
		except WebDriverException:
			continue
	time.sleep(1)
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				print("APARATALOGIA")
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[1]/div/a[1]')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[1]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[1]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				print("INSTRUMENTAL")
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[1]')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[2]')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[2]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[2]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	for t in range(1,20):
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[1]/div/div/div/a[%d]'% (t))
				href2 = element.get_attribute('href')
				print(href2)
				consumo(href2)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[1]/div/div/div/a[%d]'% (t))
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[1]/div/div/div/a[%d]'% (t))
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				print("APARATALOGIA LABORATORIO")
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[2]/div/a')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[2]/div/a')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[2]/div/a')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				print("INSTRUMENTAL LABORATORIO")
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[1]')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[1]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	try:
		try:
			if(browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/ul/li[3]/a/span').is_enabled()):
				browser.get('https://kalma.es/index.php')
				element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[2]')
				href = element.get_attribute('href')
				print(href)
				consumo(href)
		except NoSuchElementException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[2]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
		except WebDriverException:
			browser.get("https://kalma.es/index.php/customer/account/login/")
			username = browser.find_element_by_id("email")
			password = browser.find_element_by_id("pass")
			username.clear()
			username.send_keys("pedidos@dentaltix.com")
			password.send_keys("B86142809")
			browser.find_element_by_xpath('//*[@id="send2"]').click()
			time.sleep(0.5)
			print("RELOGGEADO")
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[2]')
			href = element.get_attribute('href')
			print(href)
			consumo(href)
	except NoSuchElementException:
		pass
	except WebDriverException:
		pass
	end = time.clock()
	tiempoEjec= (end - start)/3600
	print("PROGRAMA SCRAPY DE KALMA FINALIZADO")
	f2.write("TIEMPO TOTAL DE EJECUCION: "+str(int(tiempoEjec))+"horas")
	f2.close()
	f3.close()
	browser.close()

main()