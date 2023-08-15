from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    url = "https://books.toscrape.com/"

    chrome_options = Options()
    # Keeping the browser open after script completion
    chrome_options.add_experimental_option("detach", True)

    # Setting up your chrome driver
    driver = Chrome(service=Service(ChromeDriverManager().install()), 
                    options=chrome_options)

    driver.get(url)
    driver.maximize_window()

    xpath_query = "//article[p[@class='star-rating One']]/h3/a | //article[p[@class='star-rating One']]//p[@class='price_color']"
    results = driver.find_elements(By.XPATH, xpath_query)

    for result in results:
        if result.tag_name == "a":
            print(result.get_attribute("title"))
        else:
            print(result.get_attribute("innerHTML"))

except Exception as e:
    print("An error occurred:", str(e))
finally:
    try:
        # Make sure the driver is properly closed if it's defined
        driver.quit()
    except NameError:
        pass  # If driver is not defined, don't attempt to quit it
