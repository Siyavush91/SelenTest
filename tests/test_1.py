def test_ex(driver, url_param):
    driver.get(url_param)
    assert driver.title == "Your Store"

