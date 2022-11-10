import unittest
from discourse import HomePage
from selenium import webdriver

class DiscourseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\chromedriver.exe')
        self.driver.get('https://www.discourse.org/')
    
    def test1_closed_topics(self):
        # Access home page
        homePage = HomePage(self.driver)

        #Access demo page
        demoPage = homePage.clickDemoLink()
        logoText = demoPage.getLogoText()

        # check demo page loaded
        self.assertTrue(logoText,'Demo')

        # scroll down to end of page
        demoPage.scrollDownEndPage()
        footerText = demoPage.getFooterText() 

        # check end page
        self.assertTrue(footerText,'There are no more latest topics.')

        # print titles of closed topics
        closedTitlesList = demoPage.getClosedTopicsTitlesList()
        print('\na. List of closed topics:')

        for title in closedTitlesList:
            print(title)
                

    def test2_categories_list(self):
        # Access home page
        homePage = HomePage(self.driver)

        #Access demo page
        demoPage = homePage.clickDemoLink()
        logoText = demoPage.getLogoText()

        # check demo page loaded
        self.assertTrue(logoText,'Demo')

        # scroll down to end of page
        demoPage.scrollDownEndPage()
        footerText = demoPage.getFooterText()

        # check end page
        self.assertTrue(footerText,'There are no more latest topics.')

        # print topic categories list
        categoryList = demoPage.getTopicsCategoryList()
        categorySet = set(categoryList)
        print('\nb. List of topics categories:')

        for category in categorySet:
            print(category+":",categoryList.count(category),'topics')


    def test3_most_viewed_topic(self):
         # Access home page
        homePage = HomePage(self.driver)

        #Access demo page
        demoPage = homePage.clickDemoLink()
        logoText = demoPage.getLogoText()

        # check demo page loaded
        self.assertTrue(logoText,'Demo')

        # scroll down to end of page
        demoPage.scrollDownEndPage()
        footerText = demoPage.getFooterText()

        # check end page
        self.assertTrue(footerText,'There are no more latest topics.')
                
        # print most viewed topic
        viewsList = demoPage.getTopicsViewsList()
        topicsList = demoPage.getTopicsList()
        maxViews = max(viewsList)
        idxMaxViews = viewsList.index(maxViews)
        print('\nc. Most viewed topic:')
        print(topicsList[idxMaxViews]+":",maxViews,'views')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()