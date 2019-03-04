import time
from selenium import webdriver

URL = 'https://www.instagram.com/explore/tags/{}' #인스타그램 테그 기본 주소
DRIVER_DIR = "C:/Users/JIWOO/Desktop/Study/6.Git hub/2.Peckage/chromedriver" #크롬 드라이버 패키지 디렉토리

def instragram_scrapy(keyword) :
    try :
        driver = webdriver.Chrome(DRIVER_DIR)
        driver.implicitly_wait(10)
        driver.get(URL.format(keyword))

        new_links = driver.find_elements_by_css_selector('div.v1Nh3 > a') # 새로 연결할 주소, v1Nh3의 자식 'a' 불러오기
        links = [i.get_attribute('href') for i in new_links] # new_link의 자식 'a'의 'href' 속성 값만 가져오기

        for link in links :
            driver.get(link)
            for li in driver.find_elements_by_class_name('C4VMK'): #C4VMK(게시물 내 콘텐츠 위치) 클래스 찾기
                user = li.find_element_by_tag_name('a').text #작성자
                reply = li.find_element_by_tag_name('span').text #댓글, 해시태그
                print("({}) {}".format(user, reply))

    except Exception as e:
        print(e)
    finally:
        driver.close()

if __name__ == "__main__" :
    keyword = input('keyword(tag)') # 키워드
    instragram_scrapy(str(keyword))

# 20190305 최근 게시물 4줄(콘텐츠 12개) 내용 불러오기
# 최근 게시물 10줄 이상 불러오려면?
# Crawling 콘텐츠 엑셀파일로 정제해서 저장하려면?
