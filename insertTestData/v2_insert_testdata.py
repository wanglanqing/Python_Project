#--coding:utf8--
import pymysql


class InsertTestData(object):
    STUDENT_FILE = 'Student.txt'
    COURSE_FILE = 'Course.txt'
    TEACHER_FILE = 'Teacher.txt'
    SCORE_FILE = 'Score.txt'

    def __init__(self):
        self.connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            # passwd = ' ',
            charset = 'utf8'
        )
        self.database = 'execersise_test'

    def read_lines(self, filename):
        dict = {}
        file_name = filename.split('.')[0]
        dict['file_name'] = file_name
        with open(filename) as f:
            lines = f.readlines()
        dict['file_content'] = lines
        return dict

    def connect_mysql(self):
        cursor = self.connect.cursor()
        return cursor

    def close_mysql(self):
        self.connect.close()

    def close_curser(self):
        self.connect_mysql().close()

    def add_test_datas(self, file_obj):
        file = file_obj
        file_name = file['file_name']
        title = file['file_content'][0].strip()
        datas = file['file_content'][1:]
        content_len = len(datas)
        data = ''
        counter = 1
        for tmpdata in datas:
            if counter == content_len:
                data += '(' + tmpdata.strip() + ');'
            else:
                data += '(' + tmpdata.strip() + '),'
            counter += 1
        sql = 'insert into ' + self.database + '.' + file_name + ' (' + title + ') values '+ data
        try:
            # self.connect_mysql().executemany(sql)
            self.connect_mysql().execute(sql)
        except Exception as e:
            print('add_' + file_name + ' error: ', e)
        self.connect.commit()
        self.close_curser()

if __name__ == '__main__':
    testdata = InsertTestData()
    testdata.add_test_datas(testdata.read_lines(InsertTestData.STUDENT_FILE))
    testdata.add_test_datas(testdata.read_lines(InsertTestData.TEACHER_FILE))
    testdata.add_test_datas(testdata.read_lines(InsertTestData.COURSE_FILE))
    testdata.add_test_datas(testdata.read_lines(InsertTestData.SCORE_FILE))