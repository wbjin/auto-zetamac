import time
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class ParseError(Exception):
    def __init__(self, message="Not found"):
        self.message = message

# browser = Firefox()
browser = Chrome()
def func():
    browser.get('https://arithmetic.zetamac.com/')
    browser.find_element("xpath", "//input[@value='Start']").click()
    t_end = time.time() + 60 * 2
    time_left = browser.find_element(By.CLASS_NAME, "left").text
    score = 0
    while(True):
        time.sleep(0.5)
        if (time_left == "0"): break
        problem = browser.find_element(By.CLASS_NAME, "problem").text
        elements = problem.split(" ")
        if elements[1] == "+":
            output = int(elements[0])+int(elements[2])
        elif elements[1] == "–":
            output = int(elements[0])-int(elements[2])
        elif elements[1] == "×":
            output = int(elements[0])*int(elements[2])
        elif elements[1] == "÷":
            output = int(int(elements[0])/int(elements[2]))
        else:
            raise ParseError(elements[1] + " not found")

        print(elements[0], elements[1], elements[2], "=", output)
        submit_button = browser.find_element(By.CLASS_NAME, "answer")
        submit_button.send_keys(str(output))
        submit_button.clear()
        score+=1
        time_left = browser.find_element(By.CLASS_NAME, "left").text
    
    print(score)
    time.sleep(15)
    browser.close()
    quit()


if __name__ == "__main__":
    try:
        func()
    except Exception as e:
        print(e)
        time.sleep(15)
        browser.close()
        quit()
