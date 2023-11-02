from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class Chatbot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def openBrowser(self):
        self.driver.get("https://web.whatsapp.com")
        self.driver.maximize_window()

    def searchContact(self, name):
        try:
            person = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//span[@title='{name}']")))
            person.click()
            print("* Usuário encontrado!")
        except TimeoutException:
            print("* Usuário não encontrado!")

    def SendMessage(self, message, count):
        start_time = time.time()
        for i in range(count):
            input_chat = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3uMse')))
            input_chat.click()
            time.sleep(0.5)
            input_chat.send_keys(message + Keys.RETURN)
            time.sleep(0.8)
            print("* Mensagem enviada!")

        end_time = time.time()
        print("* Fim das mensagens")
        print("Tempo total:", round(end_time - start_time, 2), "segundos")