import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

driver.get("https://lansweeper.triumf.ca:82/AssetsImport.aspx")
driver.maximize_window()

username_field = driver.find_element(By.ID, "NameTextBox")
username_field.send_keys('yzeng')

load_dotenv(dotenv_path='password.env')
password = os.getenv('PASSWORD')
password_field = driver.find_element(By.ID, "PasswordTextBox")
password_field.send_keys(password)

login_button = driver.find_element(By.ID, "LoginButton")
login_button.click()

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ButtonBrowseOverlap")))
driver.execute_script("arguments[0].click();", button)

file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
file_path = os.path.join(os.path.dirname(__file__), 'test1.csv')
file_input.send_keys(file_path)

validate_button = driver.find_element(By.ID, "btnValidateImportAssets")
validate_button.click()

result_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "MainContent_assetImportResults")))

if "Everything checked out." in result_div.text:
    import_button = driver.find_element(By.ID, "btnImportAssets")
    import_button.click()
else:
    error_message = result_div.find_element(By.CSS_SELECTOR, "span").text
    print("Error message:", error_message)


