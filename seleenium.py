from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get("http://wykop.pl")

r = firefox.find_element_by_partial_link_text('radziecki')
r.click()

firefox.close()
#firefox.find_element_by_tag_name('a') #element - jeden element, elements - wiecej



#element = firefox.find_element_by_id("login")
#element.click()