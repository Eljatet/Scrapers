# -*- coding: utf-8 -*-
from selenium import *
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import codecs
import sys
from sys import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
contProductos=0

def productos():
	global contProductos
	sum=0
	for i in range(1,31):
		try:
			browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/a'%(i))
			try:
				element=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[1]/p[1]/a'%(i)).text
				element=element.split("\n")
				Fabricante=element[0]
				Fabricante=Fabricante[11:]
				Referencia=element[1].replace(" ","")
				Referencia=Referencia[11:]
			except NoSuchElementException:
				element=""
				Referencia=""
				Fabricante=""
			try:
				Name=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[1]/h3/a'%(i)).text
			except NoSuchElementException:
				Name=""
			try:
				Stock=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[1]/h2/a/b'%(i)).text
			except NoSuchElementException:
				Stock=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[1]/h2/a'%(i)).text
				Stock=Stock.replace("\n","")
				if(Stock.isdigit()==False):
					Stock="0"
			try:
				Precio=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[2]/table/tbody/tr[2]/td/span'%(i)).text
				Precio=Precio.split(" ")
				if (len(Precio)==2):
					Precio=Precio[0]
				elif (len(Precio)==3):
					Precio=Precio[0]+Precio[1]
			except NoSuchElementException:
				try:
					Precio=browser.find_element_by_xpath('//*[@id="product_list"]/li[%d]/div[2]/table/tbody/tr/td/span'%(i)).text
					Precio=Precio.split(" ")
					if (len(Precio)==2):
						Precio=Precio[0]
					elif (len(Precio)==3):
						Precio=Precio[0]+Precio[1]
				except NoSuchElementException:
					Precio=""
			f3.write(Name+';'+Referencia+';'+Fabricante+';'+Stock+';'+Precio+';'+'\n')
			contProductos+=1
			sum+=1
		except WebDriverException,UnexpectedAlertPresentException:
			print(contProductos)
			contProductos=0
			return sum
			break;
		except NoSuchElementException:
			print(contProductos)
			contProductos=0
			return sum
			break;
	print(contProductos)
	contProductos=0
	return sum

def buscaproductos():
	try:
		sumaProductos=0
		browser.find_element_by_id('subcategories')
		urlS=browser.current_url
		for sub in range(1,1000):
			try:
				browser.get(urlS)
				browser.find_element_by_xpath('//*[@id="subcategories"]/ul/li[%d]/a[2]'%(sub)).click()
				try:
					browser.find_element_by_class_name('pagination')
					for x in range(1,1000):
						try:
							sumaProductos=(productos()+sumaProductos)
							if(browser.find_element_by_xpath('//*[@id="pagination_next"]/a').is_enabled()):
								browser.find_element_by_xpath('//*[@id="pagination_next"]/a').click()
							else:
								print(sumaProductos)
								break;
						except NoSuchElementException:
							break;
				except NoSuchElementException:
					sumaProductos=(productos()+sumaProductos)
			except NoSuchElementException:
				break;
	except NoSuchElementException:
		try:
			browser.find_element_by_class_name('pagination')
			for x in range(1,1000):
				try:
					sumaProductos=(productos()+sumaProductos)
					if(browser.find_element_by_xpath('//*[@id="pagination_next"]/a').is_enabled()):
						browser.find_element_by_xpath('//*[@id="pagination_next"]/a').click()
					else:
						print(sumaProductos)
						break;
				except NoSuchElementException:
					break;
		except NoSuchElementException:
			sumaProductos=(productos()+sumaProductos)


reload(sys)
sys.setdefaultencoding('utf-8')
f2=codecs.open('loggVentur.txt','w','utf-8')
f3=codecs.open('VenturScrapy.txt','wb','utf-8')
f3.write('Name'+';'+'Referencia'+';'+'Fabricante'+';'+'Stock'+';'+'Precio'+';'+'\n')
#chromedriver = 'C:\chromedriver.exe'
#browser= webdriver.Chrome(chromedriver)
browser = webdriver.PhantomJS('C:\phantomjs.exe')
browser.set_window_size(1280,1024)
start = time.clock()
browser.get('http://www.portalodontologico.es/authentication.php?back=index.php')
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("passwd")
username.clear()
password.clear()
username.send_keys("pedidos@dentaltix.com")
password.send_keys("8UCoq37D")
browser.find_element_by_xpath('//*[@id="SubmitLogin"]').click()
urls=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div')
ListlinkerHref = urls.find_elements_by_xpath("//*[@href]")
for ini in range(1,6):
	if(ini==2):
		url=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[2]/a')
		href = url.get_attribute('href')
		print(href)
		browser.get(href)
		print(href)
		buscaproductos()
	else:				
		for pag in range(1,100):
			try:
				if(ini==3 and (pag!=3 or pag!=4 or pag!=5)):
					url=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[%d]/ul/li[%d]/a'% (ini,pag))
					href = url.get_attribute('href')
					print(href)
					browser.get(href)
					buscaproductos()
				elif(ini==4 and (pag!=2 or pag!=3 or pag!=4)):
					url=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[%d]/ul/li[%d]/a'% (ini,pag))
					href = url.get_attribute('href')
					print(href)
					browser.get(href)
					buscaproductos()
				elif(ini==5):
					url=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[%d]/ul/li[%d]/a'% (ini,pag))
					href = url.get_attribute('href')
					print(href)
					browser.get(href)
					buscaproductos()
				for pag2 in range(1,100):
					try:
						url=browser.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[%d]/ul/li[%d]/ul/li[%d]/a'% (ini,pag,pag2))
						href = url.get_attribute('href')
						print(href)
						browser.get(href)
						buscaproductos()
					except WebDriverException,UnexpectedAlertPresentException:
						pass
					except NoSuchElementException:
						print("----------------------------------------")
						break;
			except NoSuchElementException:
				break;
end = time.clock()
tiempoEjec= (end - start)/3600
f2.write("TIEMPO TOTAL DE EJECUCION: "+str(int(tiempoEjec))+"horas")
print("PROGRAMA SCRAPY DE VENTUR FINALIZADO")
f2.close()
f3.close()
browser.close()
