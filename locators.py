from selenium.webdriver.common.by import By

# locators for web elements from homepage
class HomePageElements:
    demoLink = (By.LINK_TEXT,'Demo')

# locators for web elements from demo page
class DemoPageElements:
    htmlTag = (By.TAG_NAME,'html')
    logoText = (By.ID, 'site-text-logo')
    footerText = (By.CSS_SELECTOR,"div.footer-message>h3")
    closedTopicLink = (By.CSS_SELECTOR,"tr.closed a.title")
    topicRow = (By.CSS_SELECTOR,"tr.topic-list-item")
    topicView = (By.CSS_SELECTOR,"[title*='been viewed']")
    topicLink = (By.CSS_SELECTOR,"a.title")