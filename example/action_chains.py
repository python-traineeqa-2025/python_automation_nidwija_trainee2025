"""
move_to_element(element)-> Moves the mouse to the center of the given element.
click(element)->	Clicks on the specified element.
context_click(element)->	Performs a right-click on the element.
double_click(element)->	Performs a double-click on the element.
click_and_hold(element)->	Clicks and holds the mouse on the element.
release() ->	Releases the held mouse button.
drag_and_drop(source, target)->	Drags an element and drops it onto another.
perform()->	Executes all the actions in the chain.


actions.click(input_box).send_keys("Selenium Testing")
actions.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()

another_input_box = driver.find_element(By.ID, "another_input_id")
actions.click(another_input_box).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

"""

