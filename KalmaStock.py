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



def consumo(URL):
	browser.get(URL)
	start2=time.clock()
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
	for i in range(1,10000):
		try:
			time.sleep(0.5)
			cargar=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div[2]/a').click()
			time.sleep(0.5)
			try:
				element = WebDriverWait(browser, 20).until(
				EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
			finally:
				time.sleep(1)
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		except NoSuchElementException:
			obtenerDatos(URL,start2)
			break;
def obtenerDatos(URL,start3):
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
			if(suma==int(sumReal[0])):
				end2=time.clock()
				print(str(int((end2 - start3)/60))+ " minutos")
				print(str(suma)+ " productos")
				f2.write(str(URL)+"  Tiempo en esta URL: "+str(int((end2 - start3)/60))+"  Minutos"+'\r\n')
				f2.write(str(URL)+"  Suma total de productos obtenidos:  "+str(suma)+'\r\n')
			else:
				n=int(suma/10)
				obtenerDatosError(URL,start3,n)
			break;
		except WebDriverException:
			break;
def obtenerDatosError(URL,start3,n):
	sum=0
	print(str(n))
	browser.get(URL)
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	try:
		element = WebDriverWait(browser, 20).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
	finally:
		time.sleep(1.5)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	try:
		element = WebDriverWait(browser, 20).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
	finally:
		time.sleep(1.5)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(0.5)
	for i in range(1,5000):
		try:
			cargar=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div[2]/a').click()
			time.sleep(1)
			try:
				element = WebDriverWait(browser, 20).until(
				EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/div/div[2]/script')))
			finally:
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		except NoSuchElementException:
			for r in range(n,1000):
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
								except NoSuchElementException:
									Precio=""
							f3.write(Name+';'+element+';'+Ref_Fabricante+';'+Stock+';'+Precio+';'+'\n')
							sum+=1
						except WebDriverException,UnexpectedAlertPresentException:
							f2.write(str(datetime.utcnow())+"  ERROR CLICK PRODUCTO"+'\r\n')
							break;
				except NoSuchElementException:
					print("Productos Segunda Vuelta: " + str(sum))
					end2=time.clock()
					print(str(int((end2 - start3)/60))+ " minutos")
					f2.write(str(URL)+"  Tiempo en esta URL: "+str(int((end2 - start3)/60))+"  Minutos"+'\r\n')
					break;
				except WebDriverException:
					break;
			break;

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	f2=codecs.open('loggKalma.txt','w','utf-8')
	f3=codecs.open('KalmaStock.txt','wb','utf-8')
	f3.write('Name'+';'+'Referencia'+';'+'Ref_Fabricante'+';'+'Stock'+';'+'Precio'+';'+'\n')
	print(str(datetime.utcnow()))
	chromedriver = 'C:\chromedriver.exe'
	browser= webdriver.Chrome(chromedriver)
	start = time.clock()
	#browser = webdriver.PhantomJS('C:\phantomjs.exe',service_args=["--webdriver-loglevel=ERROR"])
	#browser.set_window_size(1280,1024)
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

	print("APARATALOGIA")
	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[1]/div/a[1]')
	href = element.get_attribute('href')
	print(href)
	consumo(href)
	print("INSTRUMENTAL")
	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[1]')
	href = element.get_attribute('href')
	print(href)
	consumo(href)

	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14567"]/div/div[2]/div/div[2]/div/a[2]')
	href = element.get_attribute('href')
	print(href)
	consumo(href)

	for t in range(1,20):
		try:
			browser.get('https://kalma.es/index.php')
			element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[1]/div/div/div/a[%d]'% (t))
			href2 = element.get_attribute('href')
			print(href2)
			consumo(href2)
		except NoSuchElementException:
			continue
			print("-----------")
		except WebDriverException:
			continue
			print("-----------")

	print("APARATALOGIA LABORATORIO")
	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[2]/div/a')
	href = element.get_attribute('href')
	print(href)
	consumo(href)


	print("INSTRUMENTAL LABORATORIO")
	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[1]')
	href = element.get_attribute('href')
	print(href)
	consumo(href)

	browser.get('https://kalma.es/index.php')
	element= browser.find_element_by_xpath('//*[@id="popup14568"]/div/div[2]/div/div[1]/div/a[2]')
	href = element.get_attribute('href')
	print(href)
	consumo(href)


	end = time.clock()
	tiempoEjec= (end - start)/3600
	print("PROGRAMA SCRAPY DE KALMA FINALIZADO")
	f2.write("TIEMPO TOTAL DE EJECUCION: "+str(int(tiempoEjec))+"horas")
	f2.close()
	f3.close()
	browser.close()