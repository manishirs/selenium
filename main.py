# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.common.keys import Keys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

Chrome_driver_path = 'C:\development\chromedriver.exe'

from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path=Chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name('fName')
fname.send_keys('Manish')
fname.send_keys(Keys.ENTER)

lname = driver.find_element_by_name('lName')
lname.send_keys('Mishra')
lname.send_keys(Keys.ENTER)

email = driver.find_element_by_name('email')
email.send_keys('manishirs@gmail.com')
email.send_keys(Keys.ENTER)

#button = driver.find_element_by_tag_name('Sign Up')
#button.click()

