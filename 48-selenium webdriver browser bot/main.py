from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Raj/devel/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?crid=1TQ48FSGZ06E6&keywords=instant+pot&qid=1675514558&sprefix=insta%2Caps%2C110&sr=8-4&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc")
price_element = driver.find_element(By.ID, "attach-base-product-price")
# price = driver.find_element("price")
print(price_element)
print(price_element.get_attribute("value"))

price_straightup = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
print(price_straightup.text)

# driver.close()
driver.quit()