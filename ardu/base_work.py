import sqlite3


def base_update(form_number='test', avg_val=0, values='test'):
    try:
        insert_data = (form_number, avg_val, values,)
        conn = sqlite3.connect("ardu_base.db", )
        curs = conn.cursor()
        curs.execute("INSERT INTO ardu_data VALUES (?, ?, ?)", insert_data)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print("Вставка данных")
    base_update()
    print("Данные внесены")