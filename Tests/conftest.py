import pytest
from selenium import webdriver

driver = None  # to assgin global driver to screentshot



def pytest_addoption(parser):
    parser.addoption(
    "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver                                            # using to assign  for screnshot
    browser_name = request.config.getoption("browser_name")  #esay way to call all the browser
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firfox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver
    driver.quit()



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    """Captures a screenshot and saves it to the given path."""
    driver.save_screenshot(file_name)