import json_reader
from PyQt5 import QtWidgets
import everytime
# lecture_name, prof, time_table, full_link, score, assign, team, grade, attendance, test_count
'''
prof = None
lect_name = None
score = None
assign = None
team = None
grade = None
attendance = None
test = None
'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = everytime.Everytime()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())