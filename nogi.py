from selenium import webdriver
import pandas


browser = webdriver.Chrome(executable_path='c:/chromedriver/chromedriver.exe')
df = pandas.read_csv('default.csv', index_col=0) #1行目にname, furiganaを入れる
url = "http://www.nogizaka46.com/member/"


POSTS = "div.unit"
MEMBER_NAME = ".main"
MEMBER_SUBNAME = ".sub"

browser.get(url)

while True:
    print("Starting to get posts...")
    posts = browser.find_elements_by_css_selector(POSTS)
    print (len(posts))

    for post in posts:
        try:
            name = post.find_element_by_css_selector(MEMBER_NAME).text
            print(name)
            sub = post.find_element_by_css_selector(MEMBER_SUBNAME).text
            print(sub)
            se = pandas.Series([name,sub],["name", "furigana"])
            df = df.append(se, ignore_index=True)
        except Exception as e:
            print(e)
    break

print("Finished Scraping. Writing CSV.......")
df.to_csv("outnogi.csv",encoding="shift_jis")
print("DONE")
