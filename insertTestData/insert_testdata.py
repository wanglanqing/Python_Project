#--coding:utf8--
import pymysql

class InsertTestData(object):

    def __init__(self):
        self.connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            # passwd = ' ',
            charset = 'utf8'
        )
        self.student_file = 'Student.txt'
        self.course_file = 'Course.txt'
        self.teacher_file = 'Teacher.txt'
        self.score_file = 'Score.txt'
        self.student = 'student'
        pass

    def readlines(self,filename):
        self.file_name = filename.split('.')[0]
        with open(filename) as f:
            lines = f.readlines()
        return lines, self.file_name

    def connect_mysql(self):
        cursor = self.connect.cursor()
        return cursor

    def close_mysql(self):
        self.connect.close()

    def close_curser(self):
        self.connect_mysql().close()

    def add_student(self):
        lines = self.readlines(self.student_file)
        sql = "INSERT INTO  \
              `execersise_test`.`Student`  \
              (`ID`,`name`, `sex`,`birthday`,`class`)  \
              VALUES  \
              ('%s','%s','%s','%s','%s')"

        for line in lines[1:] :
            try:
                self.connect_mysql().execute(sql \
                                %(line.split(',')[0].strip(),\
                                  line.split(',')[1].strip(),\
                                  line.split(',')[2].strip(),\
                                  line.split(',')[3].strip(),\
                                  line.split(',')[4].strip()
                                ))
            except Exception as e:
                print('add_student error: ',e)
            self.connect.commit()
            self.close_curser()

    def add_teacher(self):
        lines = self.readlines(self.teacher_file)
        sql = "INSERT INTO  \
                      `execersise_test`.`teacher`  \
                      (`ID`, `name`, `sex`, `birthday`, `Prof`, `Depart`)  \
                      VALUES  \
                      ('%s','%s','%s','%s','%s','%s')"
        for line in lines[1:]:
            try:
                self.connect_mysql().execute(sql \
                            %(line.split(',')[0].strip(),\
                              line.split(',')[1].strip(),\
                              line.split(',')[2].strip(),\
                              line.split(',')[3].strip(),\
                              line.split(',')[4].strip(),\
                              line.split(',')[5].strip()
                        ))
            except Exception as e:
                print('add_teacher error: ',e)
            self.connect.commit()
            self.close_curser()

    def add_score(self):
        lines = self.readlines(self.score_file)
        sql = "INSERT INTO  \
                      `execersise_test`.`score`  \
                      (`SID`, `CID`, `Degree`)  \
                      VALUES  \
                      ('%s','%s','%s')"
        for line in lines[1:]:
            try:
                self.connect_mysql().execute(sql \
                             % (line.split(',')[0].strip(), \
                                line.split(',')[1].strip(), \
                                line.split(',')[2].strip()
                        ))
            except Exception as e:
                print('add_score error: ',e)
            self.connect.commit()
            self.close_curser()

    # def add_course(self):
    #     lines = self.readlines(self.course_file)
    #     sql = "INSERT INTO  \
    #                           `execersise_test`.`course`  \
    #                           (`ID`, `name`, `Tno`)  \
    #                           VALUES  \
    #                           ('%s','%s','%s')"
    #     for line in lines[1:]:
    #         try:
    #             self.connect_mysql().execute(sql \
    #                              % (line.split(',')[0].strip(), \
    #                                 line.split(',')[1].strip(), \
    #                                 line.split(',')[2].strip()
    #                                 ))
    #
    #         except Exception as e:
    #             print('add_course error: ',e)
    #         self.connect.commit()
    #         self.close_curser()

    def add_course(self):
        lines = self.readlines(self.course_file)
        sql = "INSERT INTO  \
                              `execersise_test`.`course`  \
                              (`ID`, `name`, `Tno`)  \
                              VALUES  \
                              ('%s','%s','%s')"
        for line in lines[1:]:
            try:
                self.connect_mysql().execute(sql \
                                 % (line.split(',')[0].strip(), \
                                    line.split(',')[1].strip(), \
                                    line.split(',')[2].strip()
                                    ))

            except Exception as e:
                print('add_course error: ',e)
            self.connect.commit()
            self.close_curser()

if __name__ == '__main__':
    testdata = InsertTestData()
    testdata.add_student()
    testdata.add_teacher()
    testdata.add_course()
    testdata.add_score()
    testdata.close_mysql()

