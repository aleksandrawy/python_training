from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get("https://www.igame.com/eye-test/")

firefox.switch_to.frame(firefox.find_element_by_tag_name("iframe"))

for i in range (30):
    el = firefox.find_element_by_class_name("thechosenone")
    print(el)
    el.click()

    #el = firefox.find_element_by_partial_link_text('radziecki')
#el.click()