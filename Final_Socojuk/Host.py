from selenium import webdriver
import time
import pyautogui
import json
from bs4 import BeautifulSoup


# chrome 실행
class Update:
    def update(self):

        print("update 버튼이 눌렸어요")
        driver = webdriver.Chrome('C:\chromedriver.exe')

        # url에 접근한다.
        driver.get('https://everytime.kr/login')

        # 아이디/비밀번호를 입력해준다.
        user_id = "jjs301203"
        password = "wltjr5108"
        driver.find_element_by_name('userid').send_keys(user_id)
        driver.find_element_by_name('password').send_keys(password)

        # 로그인 버튼을 눌러주자.

        driver.find_element_by_xpath("//input[@type='submit']").click()

        # else:#새로운 시간표의 데이터를 추출합니다.

        print('시간표 데이터의 추출을 시작합니다')
        # 시간표로 접속
        driver.find_element_by_xpath("//a[@href='/timetable']").click()

        # 새로고침
        driver.refresh()
        driver.implicitly_wait(300)

        # 학기 시간표 띄우기
        driver.find_element_by_xpath("//li[@class='button search']").click()
        driver.implicitly_wait(300)

        # 스크롤 위치로 이동
        pyautogui.moveTo(1305, 988)
        time.sleep(5)

        # 스크롤 내리기 오랜 시간이 걸리고 다수의 마우스 클릭을 사용하므로 시연 시에는 주석을 안풉니다.
        
        b = 0
        while b <= 25:
            pyautogui.click()
            time.sleep(0.01)
            b = b + 1
        

            # 강의시간표 준비
        time.sleep(0.2)

        html = driver.page_source
        outbs = BeautifulSoup(html, 'html.parser')

        trs = outbs.find('div', id='subjects').find('div', class_='list').find('tbody').findAll('tr')


        list = []


        for tr in trs:
            tds = tr.find_all('td')

            # 강의의 기본적인 정보를 추출
            lecture_name = tds[3].string
            prof = tds[4].string
            time_table = tds[7].string
            rink_path = tds[8].find('a')
            rink = rink_path.get('href')
            full_link = 'https://everytime.kr' + rink
            score = rink_path.get('title')

            # 각 강의별 평가 항목 페이지로 접속해 세부 평가 항목의 정보를 추출

            try:
                driver.get(full_link)
                time.sleep(0.5)

                s_html = driver.page_source
                inner_bs = BeautifulSoup(s_html, "html.parser")

                det = inner_bs.find('div', class_='details').findAll('span')

            except: #하지만 오랜 시간 크롤링이 진행되면 정보를 받아오는데 시간이 오래 걸릴 수 있으므로 접속 오류시 재접속 후 1.5초 대기
                try:
                    driver.get(full_link)
                    time.sleep(1.5)

                    s_html = driver.page_source
                    inner_bs = BeautifulSoup(s_html, "html.parser")

                    det = inner_bs.find('div', class_='details').findAll('span')
                except:#그래도 접속 오류 발생 시 새 창 생성
                    try:
                        driver.close();# 본래의 창 닫기
                        driver = webdriver.Chrome('C:\chromedriver.exe') #새 창 켜기

                        driver.get('https://everytime.kr/login') #로그인 창 접속

                        # 아이디/비밀번호를 입력해준다.
                        driver.find_element_by_name('userid').send_keys(user_id)
                        driver.find_element_by_name('password').send_keys(password)

                        # 로그인 버튼을 눌러주자.
                        driver.find_element_by_xpath("//input[@type='submit']").click()

                        driver.get(full_link)#강의별 평가 페이지 접속
                        time.sleep(1.5)

                        s_html = driver.page_source
                        inner_bs = BeautifulSoup(s_html, "html.parser")

                        det = inner_bs.find('div', class_='details').findAll('span')

                    except: #접속할 수 없는 평가 페이지이므로 리스트에서 제외합니다.
                        print("pass")
                        continue

            if det != []:
                # 각 평가 항목 추출
                assign = det[0].string
                team = det[1].string
                grade = det[2].string
                attendance = det[3].string
                test_count = det[4].string

                #입력되는 강의의 정보를 하나씩 띄워줍니다.
                print(lecture_name, prof, time_table, score, assign, team, grade, attendance, test_count)

                list.append(
                    {"lecture_name": lecture_name, "prof": prof, "time_table": time_table, "full_link": full_link,
                     "score": score, "assign": assign, "team": team, "grade": grade, "attendance": attendance,
                     "test_count": test_count})

        print(list)
        with open('list.json', 'w') as writer:#모든 강의의 리스트를 각 강의별로 Dictionary로 저장하고 list의 하나의 요소로써 담아둡니다.
            writer.write(json.dumps(list))
        driver.close();



if __name__ == "__main__":
    Update().update()
