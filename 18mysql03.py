import pymysql

conn = pymysql.connect(host='localhost', user='kosmo_user', 
    password='1234', db='kosmo_db', charset='utf8')

curs = conn.cursor()

sql = """update board set title='{1}', content='{2}'
    where num = {0}""".format(input('수정할 일련번호:'), input('제목:'),
                        input('내용:'))

try:
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 수정됨")
except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)

conn.close()