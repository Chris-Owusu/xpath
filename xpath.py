from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://books.toscrape.com/"

chrome_options = Options()
# so the browser doesn't close
chrome_options.add_experimental_option("detach", True)

# setting up your chrome driver
driver = Chrome(service=Service(ChromeDriverManager().install()), 
                options=chrome_options)

driver.get(url)
driver.maximize_window()

xpath_query = "//article[p[@class='star-rating One']]/h3/a | //article[p[@class='star-rating One']]//p[@class='price_color']"
# re = driver.find_elements("xpath", xpath_query)
results = driver.find_elements(By.XPATH, xpath_query)

for result in results:
    if result.tag_name == "a":
        print(result.get_attribute("title"))
    else:
        print(result.get_attribute("innerHTML"))

 
driver.quit()