"""

ID (find_element(By.ID, "element_id"))
Name (find_element(By.NAME, "element_name"))
Class Name (find_element(By.CLASS_NAME, "class_name"))
Tag Name (find_element(By.TAG_NAME, "tag_name"))
Link Text / Partial Link Text (find_element(By.LINK_TEXT, "link text"))
CSS Selectors (find_element(By.CSS_SELECTOR, "css_selector"))
XPath (find_element(By.XPATH, "//tagname[@attribute='value']"))

xpath::

//{tag}[@attribute='']
eg: //div//input[@data-test='username']
//div//input[contains(@data-test,'username')]

"""