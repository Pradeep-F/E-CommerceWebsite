class BaseClass:

    def __init__(self,driver):
        self.driver = driver

    def getTitel(self):
        return self.driver.title
