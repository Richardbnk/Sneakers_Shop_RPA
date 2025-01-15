"""
Descontinued since the new firewall from nike is more extreme today.

Before Running, for the login to work, change the text "cdc" to any other text with 3 digits, as shown in the code below:

perl -pi -e 's/cdc/bct/g' /Users/richardb/Repositories/files/chromedriver

"https://www.zoominfo.com" for test security anti bot
https://www.zenrows.com/blog/undetected-chromedriver#denied-access
"""

from rbspec.rpa import web_scraper as ws

from selenium.webdriver.common.by import By
from selenium import webdriver
import params

import time

sneaker_url = "https://www.nike.com.br/snkrs/dunk-low-retro-bttys-025979.html?cor=NX"

login1 = params.LOGINS[0]
email = login1["email"]
password = login1["password"]

product_sizes = ("40", "40,5")

size = product_sizes[0]


chrome_path = ws.get_driver_path()


driver = ws.startSelenium(driver_path=chrome_path, window_size=[140, 90])
# Changing the property of the navigator value for webdriver to undefined

ws.maximize_window(driver=driver)

ws.open_url(driver=driver, url="https://www.nike.com.br/")


# Entrar Login
driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]").click()

# insert login info
ws.wait_element(
    driver=driver,
    element_type=By.CSS_SELECTOR,
    element_path="input[type^='email']",
    timeout=60,
)
ws.do_action(
    driver=driver,
    action="click",
    element_type=By.CSS_SELECTOR,
    element_path="input[type^='email']",
    timeout=2,
    wait_before_action=1.1,
)
ws.do_action(
    driver=driver,
    action="send_keys",
    element_type=By.CSS_SELECTOR,
    element_path="input[type^='email']",
    timeout=2,
    text=email,
)
ws.do_action(
    driver=driver,
    action="click",
    element_type=By.CSS_SELECTOR,
    element_path="input[type^='password']",
    timeout=2,
    wait_before_action=1.2,
)
ws.do_action(
    driver=driver,
    action="send_keys",
    element_type=By.CSS_SELECTOR,
    element_path="input[type^='password']",
    timeout=2,
    text=password,
)
ws.do_action(
    driver=driver,
    action="click",
    element_type=By.CSS_SELECTOR,
    element_path="div[class^='nike-unite-submit-button']",
    timeout=2,
    wait_before_action=1.4,
)

# open URL
ws.open_url(driver=driver, url=sneaker_url)

# delete coockies element
# element = driver.find_element(
#    By.CSS_SELECTOR, "div[data-testid='banner-cookies-terms']"
# )
driver.execute_script(
    """
var element = arguments[0];
element.parentNode.removeChild(element);
""",
    element,
)

# Click at Size
driver.find_elements(
    By.CSS_SELECTOR, "input[data-testid^='product-size-{size}']".format(size=size)
)[0].click()
