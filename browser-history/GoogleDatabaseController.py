import sqlite3 as sql

from mysql.connector import OperationalError


def googleMaxIdGetir():
	try:
		vt = sql.connect('/home/celal/.config/google-chrome/Default/History-yedek',timeout=1)
		im = vt.cursor()
		im.execute("""select max(id) from visits """)
		for i in im:
			return i[0]
	except Exception:
		pass
def googleGetirById(i):
	vt = sql.connect('/home/celal/.config/google-chrome/Default/History-yedek',timeout=1)
	im = vt.cursor()
	im.execute('select m.url,h.visit_time from visits h inner join urls m on h.url=m.id WHERE h.id=?',(int(i),))
	liste = []
	liste.clear()
	for (url,visit_date) in im:
		liste.append(url)
		liste.append(visit_date)
	return liste