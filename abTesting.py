
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

url = "https://the-internet.herokuapp.com/"

chrome_options = Options()
# so the browser doesn't close
chrome_options.add_experimental_option("detach", True)

# setting up your chrome driver
driver = Chrome(service=Service(ChromeDriverManager().install()), 
                options=chrome_options)

driver.get(url)
driver.maximize_window()

action = ActionChains(driver)

def addRemoveElements():
    driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
    addElem = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    for i in range(5):
        addElem.click()
    
    delete = driver.find_element(By.CSS_SELECTOR, ".added-manually").is_displayed()
    print(delete)
    driver.find_element(By.CSS_SELECTOR, ".added-manually").click()


def basicAuth():
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.find_element(By.CSS_SELECTOR, ".example").is_displayed()
    

def brokenImage():
    driver.find_element(By.CSS_SELECTOR, "a[href='/broken_images']").click()
    image = driver.find_element(By.TAG_NAME, "img")


def checkBoxes():
    driver.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']").click()
    first = driver.find_element(By.XPATH, "//input[1]").click()
    ass = driver.find_element(By.XPATH, "//input[1]").is_selected()
    print(f"Ass is selected, True or False: {ass}")
    second = driver.find_element(By.XPATH, "//input[2]").click()
    ass1 = driver.find_element(By.XPATH, "//input[2]").is_selected()
    print(f"Ass is selected, True or False: {ass1}")


def contextMenu():
    driver.find_element(By.CSS_SELECTOR, "a[href='/context_menu']").click()
    spot = driver.find_element(By.CSS_SELECTOR, "#hot-spot")
    action.context_click(spot)
    action.perform()
    alert = wait(driver, 10).until(EC.alert_is_present())
    text = alert.text
    assert text == "You selected a context menu"
    alert.accept()
    

def digestAuthentication():
    driver.find_element(By.CSS_SELECTOR, "a[href='/digest_auth']").click()
    driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")
    driver.find_element(By.CSS_SELECTOR, "div[class='example'] p").is_displayed()


def disappearingElements():
    driver.find_element(By.CSS_SELECTOR, "a[href='/disappearing_elements']").click()
    home = driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()
    assert driver.current_url == url

    driver.find_element(By.CSS_SELECTOR, "a[href='/disappearing_elements']").click()
    about = driver.find_element(By.CSS_SELECTOR, "a[href='/about/']").click()
    assert driver.current_url == "https://the-internet.herokuapp.com/about/"
    result = driver.find_element(By.CSS_SELECTOR, "body h1").text
    assert result == "Not Found"

    driver.back()

    # driver.find_element(By.CSS_SELECTOR, "a[href='/disappearing_elements']").click()
    contact = driver.find_element(By.CSS_SELECTOR, "a[href='/contact-us/']").click()
    assert driver.current_url == "https://the-internet.herokuapp.com/contact-us/"
    result = driver.find_element(By.CSS_SELECTOR, "body h1").text
    assert result == "Not Found"

    driver.back()

    # driver.find_element(By.CSS_SELECTOR, "a[href='/disappearing_elements']").click()
    portfolio = driver.find_element(By.CSS_SELECTOR, "a[href='/portfolio/']").click()
    assert driver.current_url == "https://the-internet.herokuapp.com/portfolio/"
    result = driver.find_element(By.CSS_SELECTOR, "body h1").text
    assert result == "Not Found"
    

def dragNdrop():
    driver.find_element(By.CSS_SELECTOR, "a[href='/drag_and_drop']").click()
    draggable = driver.find_element(By.CSS_SELECTOR, "#column-a")
    droppable = driver.find_element(By.CSS_SELECTOR, "#column-b")
    action.drag_and_drop(draggable, droppable).perform()


def dropdown():
    driver.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown")
    dd = Select(dropdown)

    dd.select_by_visible_text("Option 1")


def dynamicControls():
    driver.find_element(By.CSS_SELECTOR, "a[href='/dynamic_controls']").click()
    # check the box
    checkBox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    checkIfElementIsSelected = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").is_selected()
    # print("Check box is selected. ", checkIfElementIsSelected)

    #remove checkBox
    removeBtn = driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.CSS_SELECTOR, "#loading").is_displayed() == True
    message = driver.find_element(By.CSS_SELECTOR, "#message").text
    assert message == "It's gone!"

    #Add Button
    driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']").click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.CSS_SELECTOR, "#loading").is_displayed() == True
    message = driver.find_element(By.CSS_SELECTOR, "#message").text
    assert message == "It's back!"

    # Click Check Button
    driver.find_element(By.CSS_SELECTOR, "#checkbox").click()
    driver.find_element(By.CSS_SELECTOR, "#checkbox").is_selected()

    # Enable
    driver.find_element(By.CSS_SELECTOR, "button[onclick='swapInput()']").click()
    driver.implicitly_wait(20)
    assert driver.find_element(By.XPATH, "//form[@id='input-example']//div[1]").is_displayed() == True
    message = driver.find_element(By.CSS_SELECTOR, "#message").text
    print(message)
    assert message == "It's enabled!"

    # Disable
    driver.find_element(By.XPATH, "(//button[normalize-space()='Disable'])[1]").click()
    driver.implicitly_wait(20)
    assert driver.find_element(By.XPATH, "//form[@id='input-example']//div[1]").is_displayed() == True
    message = driver.find_element(By.CSS_SELECTOR, "#message").text
    print(message)
    assert message == "It's disabled!"


def entryAd():
    driver.find_element(By.CSS_SELECTOR, "a[href='/entry_ad']").click()
    driver.find_element(By.CSS_SELECTOR, "#modal").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".modal-title").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".modal-body").is_displayed()
    driver.find_element(By.CSS_SELECTOR, ".modal-footer").is_displayed()
    driver.find_element(By.CSS_SELECTOR, "div[class='modal-footer'] p").click()


def exitIntent():
    driver.find_element(By.CSS_SELECTOR, "a[href='/exit_intent']").click()
    htm = driver.find_element(By.CSS_SELECTOR, "html")
    action.move_to_element(htm).perform()
    driver.implicitly_wait(30)
    modal = driver.find_element(By.CLASS_NAME, "modal").is_displayed()
    print(modal)
    # driver.find_element(By.XPATH, "//p[normalize-space()='Close']").click()


def fileDownloader():
    driver.find_element(By.CSS_SELECTOR, "a[href='/download']").click()
    # links = driver.find_elements(By.XPATH, '//a[@class="hoverZoomLink"]')
    # print(links)
    driver.find_element(By.XPATH, "//a[normalize-space()='C722AABE-E537-46CF-BEE3-19D7891CF87E.png']").click()


def fileUpload():
    driver.find_element(By.CSS_SELECTOR, "a[href='/upload']").click()
    driver.find_element(By.CSS_SELECTOR, "#file-upload").send_keys('C:/Users/ChristopherOwusuAhen/Desktop/catman.png')
    driver.find_element(By.CSS_SELECTOR, "#file-submit").click()

    assert driver.find_element(By.CSS_SELECTOR, "#uploaded-files").is_displayed() == True


def formValidation():
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "(//i[@class='fa fa-2x fa-sign-in'])[1]").click()
    assert driver.find_element(By.CSS_SELECTOR, "#flash").is_displayed() == True


def frames():
    driver.find_element(By.CSS_SELECTOR, "a[href='/frames']").click()

    # Nested Frames
    driver.find_element(By.CSS_SELECTOR, "a[href='/nested_frames']").click()
    iframe = driver.find_element(By.XPATH, "//frame[@name='frame-right']")
    driver.switch_to.frame(iframe)


def horizontalSlider():
    driver.find_element(By.CSS_SELECTOR, "a[href='/horizontal_slider']").click()
    slider = driver.find_element(By.CSS_SELECTOR, "input[value='0']")
    action.double_click(slider).move_to_element_with_offset(slider, 8, 0).perform()


def hover():
    driver.find_element(By.CSS_SELECTOR, "a[href='/hovers']").click()
    hover1 = driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")
    action.move_to_element(hover1).perform()
    assert driver.find_element(By.XPATH, "(//div[@class='figcaption'])[1]").is_displayed() == True

    driver.refresh()
    hover2 = driver.find_element(By.XPATH, "(//div[@class='figure'])[2]")
    action.move_to_element(hover2).perform()
    assert driver.find_element(By.XPATH, "(//div[@class='figcaption'])[2]").is_displayed() == True

    driver.refresh()
    hover3 = driver.find_element(By.XPATH, "(//div[@class='figure'])[3]")
    action.move_to_element(hover3).perform()
    assert driver.find_element(By.XPATH, "(//div[@class='figcaption'])[3]").is_displayed() == True


def infiniteScroll():
    driver.find_element(By.CSS_SELECTOR, "a[href='/infinite_scroll']").click()
    elem = driver.find_element(By.CSS_SELECTOR, ".jscroll-added")
    scroll_origin = ScrollOrigin.from_element(elem)
    action.scroll_from_origin(scroll_origin, 0, 500).perform()







# addRemoveElements()
# basicAuth()
# brokenImage()
# checkBoxes()
# contextMenu()
# digestAuthentication()
# disappearingElements()
# dragNdrop()
# dropdown()
# dynamicControls()
# entryAd()
# exitIntent()
# fileDownloader()
# fileUpload()
# formValidation()
# frames()
# horizontalSlider()
# hover()
# infiniteScroll()

# driver.quit()