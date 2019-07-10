from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
starttime=time.time()


def run_vote():
    driver = webdriver.Chrome()
    options = webdriver.IeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")

    driver.get("https://pearsbaby.ng/pears-baby-of-the-year-2019/?contest=photo-detail&photo_id=18105")
    button = '//*[@id="main-container"]/div[2]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div[1]'

    buttunpath = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(button))

    buttunpath.click()


while True:
  run_vote()
  print("voted")
  time.sleep(30.0 - ((time.time() - starttime) % 30.0))
