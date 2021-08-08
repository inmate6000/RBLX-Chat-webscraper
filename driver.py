#Built with selenium
#Launch this. "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
import time
class Messanger:
	def __init__(self):

		options = webdriver.ChromeOptions()
		print("HERE")
		options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
		print("DONE")
		options.add_argument('--ignore-certificate-errors')
		options.add_argument("--test-type")
		#addheadless  
		#options.add_argument('--headless')
		chrome_path = r"chromedriver\chromedriver92.exe"
		self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
		self.url = "https://www.roblox.com"
	def connect(self):
		self.driver.implicitly_wait(30)
		print("Connecting")
		self.driver.get(self.url)
		print("Connected".format(self.url))
		message = "Hi"
		friends = self.driver.execute_script('return document.getElementsByClassName("small text-title text-overflow font-caption-header chat-friend-name dynamic-ellipsis-item ng-binding read")')
		print(len(friends))
		self.chatAll("hi",["swag"],2)
	def chat(self,message):
		pass
	def chatAll(self,message,exclude=[],numFriends="x"):
		friends = self.driver.execute_script('return document.getElementsByClassName("small text-title text-overflow font-caption-header chat-friend-name dynamic-ellipsis-item ng-binding read")')
		if(numFriends == "x"):
			numFriends = len(friends)
		for i in range(numFriends):
			cur = time.time()
			try:
				#print(friends)
				if(friends[i].get_attribute("innerHTML") not in exclude):
					friends[i].click()
					inputArea = self.driver.execute_script('return document.getElementById("dialog-input")')
					inputArea.send_keys(message)
					inputArea.send_keys(Keys.ENTER)
					time.sleep(0.25)
					closeButton = self.driver.execute_script('return document.querySelector(".icon-chat-close-white")')
					closeButton.click()
				else:
					print("Excluded")
			except IndexError as e:
				print("IndexError:",e,"\nDid you forget to login? Make sure to login before running")
			print("DONE. Finished in {}ms".format(time.time()-cur))

driver = Messanger()
driver.connect()