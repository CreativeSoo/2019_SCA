import json # import json module

class Lecture_list:
    result_list = []
    def __init__(self, prof, lect_name, score, assign, team, grade, attendance, test):#리스트를 불러오기 전 각 변수들을 모두 None으로 받아둡니다
        self.prof = prof
        self.lect_name = lect_name
        self.score = score
        self.assign = assign
        self.team = team
        self.grade = grade
        self.attendance = attendance
        self.test = test

    def update(self):#Host가 만들어준 list.json 파일을 열어서 클래스멤버변수로 저장합니다.
        with open('list.json') as json_file:
            json_data = json.load(json_file)
        self.list = json_data
        print("Lecture Data Loaded")

    def search(self, prof, lect_name, score, assign, team, grade, attendance, test):#gui에서 입력받은 값으로 각 강의를 분류해냅니다.
        self.prof = prof
        self.lect_name = lect_name
        self.score = score
        self.assign = assign
        self.team = team
        self.grade = grade
        self.attendance = attendance
        self.test = test


        i = 0
        #검색 조건에 걸리지 않을 경우가 있으므로 초기화를 시켜줍니다.
        self.result_list = [{"prof":None, "lecture_name":None, "score":None, "assign":None, "team": None, "grade": None, "attendance":None, "time_table": None,"full_link":None, 'test_count':None}]

        while i<len(self.list)-1:
            item = self.list[i]
            if self.prof == None or self.prof == '' or item["prof"] == self.prof:
                if self.lect_name == None or self.lect_name == '' or item["lecture_name"] == self.lect_name:
                    if self.score == None or self.score == '' or item["score"] >= self.score:
                        if self.assign == None or self.assign == '' or item["assign"] == self.assign:
                            if self.team == None or self.team == '' or item["team"] == self.team:
                                if self.grade == None or self.grade == '' or item["grade"] == self.grade:
                                    if self.attendance == None or self.attendance == '' or item["attendance"] == self.attendance:
                                        if self.test == None or self.test == '' or item["test_count"] == self.test:
                                            self.result_list.append(item)#조건을 모두 부합하는 결과 리스트를 작성합니다.
            i = i+1



'''

(Lecture_list.result_list[i][]"lecture_name")
len(Lecture_list.result_list)
'''