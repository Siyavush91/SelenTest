from selenium.webdriver.common.action_chains import ActionChains


def test_before(driver):
    draggeble = driver.find_element_by_css_selector("body > div > img:nth-child(3)")
    droppable = driver.find_element_by_xpath("//div[@class='trash']")
    ActionChains(driver).drag_and_drop(draggeble, droppable).pause(3).perform()

def test_after(driver):
    draggeble = driver.find_elements_by_css_selector("body > div > img")
    droppable = driver.find_element_by_xpath("//div[@class='trash full']")
    for draggeble in draggeble:
        ActionChains(driver).drag_and_drop(draggeble, droppable).pause(3).perform()
