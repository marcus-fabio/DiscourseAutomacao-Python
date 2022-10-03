import time
from selenium.webdriver.common.keys import Keys
from locators import HomePageElements
from locators import DemoPageElements

# Class of home page
class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    
    # Maximize browser window
    def maximizeWindow(self):
        self.driver.maximize_window()
    
    # Click link menu to access demo page
    def clickDemoLink(self):
        self.driver.find_element(*HomePageElements.demoLink).click()
        return DemoPage(self.driver)


class DemoPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.switch_to.window(self.driver.window_handles[1])

    # Get logo text of demo page
    def getLogoText(self):
        return self.driver.find_element(*DemoPageElements.logoText).text
    
    # Get footer text in demo page
    def getFooterText(self):
        return self.driver.find_element(*DemoPageElements.footerText).text
    
    # Scroll down to end of demo page
    def scrollDownEndPage(self):
        for i in range(0,2):
            self.driver.find_element(*DemoPageElements.htmlTag).send_keys(Keys.END)
            time.sleep(1)
    
    # Get list of closed topics in demo page
    def getClosedTopicsTitlesList(self):
        return [title.text for title in self.driver.find_elements(*DemoPageElements.closedTopicLink)]
    
    # Get list of topics categories in demo page
    def getTopicsCategoryList(self):
        return [category.get_attribute('class').split()[1][9:].upper() for category in self.driver.find_elements(*DemoPageElements.topicRow)]

    # Get list of topics in demo page
    def getTopicsList(self):
        return [topic.text for topic in self.driver.find_elements(*DemoPageElements.topicLink)]

    # Convert number of views string to int
    def convertInt(str):
        if str:
            if 'k' in str:
                return int(float(str.replace('k',''))*1000)
            elif 'M' in str:
                return int(float(str.replace('M',''))*1000000)
            else:
                return int(str)

    # Get list of number of views in demo page
    def getTopicsViewsList(self):
        return [DemoPage.convertInt(views.text) for views in self.driver.find_elements(*DemoPageElements.topicView)]