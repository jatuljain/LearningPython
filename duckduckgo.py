from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import webbrowser
# opts = Options()
# opts.set_headless()
# assert opts.headless  # operating in headless mode
# binary = Firefox("E:\\Automation\\geckodriver\\geckodriver.exe")
#
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')

webbrowser.open('https://duckduckgo.com')