#-*- coding: utf-8 -*-
#!python3

from retry import retry
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.common import proxy
# from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))
# display.start()
#############################################
#########	Selenium Setup	#############
#############################################

def load_browser(browser='chrome', use_proxy=""):
	# use_proxy = "IP:PORT" or "HOST:PORT"
	#######FIREFOX############
	if browser=='firefox':
		myProxy=use_proxy
		#With from selenium.webdriver.common.proxy import *
		#Bad form
		proxy = Proxy({
			'proxyType': ProxyType.MANUAL,
			'httpProxy': myProxy,
			'ftpProxy': myProxy,
			'sslProxy': myProxy,
			'noProxy': '' # set this value as desired
			})
		#With from selenium import webdriver
		#Gets long
		# proxy = webdriver.common.proxy.Proxy({
		# 	'proxyType': webdriver.common.proxy.ProxyType.MANUAL,
		# 	'httpProxy': myProxy,
		# 	'ftpProxy': myProxy,
		# 	'sslProxy': myProxy,
		# 	'noProxy': '' # set this value as desired
		# 	})
		#With from selenium.webdriver.common import proxy
		# proxy = proxy.Proxy({
		# 	'proxyType': proxy.ProxyType.MANUAL,
		# 	'httpProxy': myProxy,
		# 	'ftpProxy': myProxy,
		# 	'sslProxy': myProxy,
		# 	'noProxy': '' # set this value as desired
		# 	})
		driver = webdriver.Firefox(proxy=proxy)
	elif browser=='chrome':
		#######CHROME##########
		PROXY = use_proxy
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
		driver = webdriver.Chrome(chrome_options=chrome_options)
	return driver

#########################################
#########################################
#########################################

if __name__ == "__main__":
    pass
