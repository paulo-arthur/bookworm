import os, sys, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

#starting brownser
options = Options()
options.headless == False
driver = webdriver.Firefox(options=options)

def downloadPDF(title):
    print('Searching for links...')
    print()

    driver.get(f'https://www.google.com/search?q={title}+filetype%3Apdf')
    time.sleep(5)

    links = []

    #METHOD 1
    try:
        _ = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/a")
        links.append(_.get_attribute('href'))
    except Exception as e:
        pass
    
    #METHOD 2
    for i in range(1, 20):
        try:
            _ = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[{i}]/div/div/div[1]/div/a')
            links.append(_.get_attribute('href'))
        except Exception as e:
            pass

    for link in links:
        print(f'[{links.index(link)}] - ', link)
        print()
    
    return links

#getting arguments
args = sys.argv[1:]

if len(args) == 0:
    print("Please, specify a book title.")
    print("Error: no book title")

else:
    try:
        book_title = []
        number_of_pages = 0
        for arg in args:
            if arg != "-p":
                book_title.append(arg)
            else:
                number_of_pages = int(args[args.index(arg) + 1])
                break
    except:
        print('Error: please, check command ortography.')

book_title = "+".join(book_title)

pdfs = downloadPDF(book_title)
url = pdfs[int(input('Choose an URL: '))]

driver.get(url)