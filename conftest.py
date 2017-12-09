# coding: utf-8
__author__ = 'jiabin5'


import pytest
import os
from utils.browserCli import browserClient, br

driver = br.driver
@pytest.fixture(scope="session", autouse=True)
def browser_client(request):
    br.setup(driver)
    print "================ started ================"
    def tear_down():
        br.close(driver)
        print "================ finished ================"
    request.addfinalizer(tear_down)


@pytest.mark.hookwrapper
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
            file_name = report.nodeid.replace("::", "_")+".png"
            print file_name
            base_name = os.path.basename(file_name)
            file_name = 'result/'+base_name
            print file_name
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % base_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)








