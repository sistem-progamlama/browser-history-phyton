import sqlite3 as sql

def mozillaMaxIdGetir():
	vt = sql.connect('/home/celal/.mozilla/firefox/3jd3s4wf.default/places.sqlite')
	im = vt.cursor()
	im.execute("""select max(id) from moz_historyvisits """)
	for i in im:
		return i[0]
def mozillaGetirById(i):
	vt = sql.connect('/home/celal/.mozilla/firefox/3jd3s4wf.default/places.sqlite')
	im = vt.cursor()
	im.execute('select m.url,h.visit_date from moz_historyvisits h inner join moz_places m on h.place_id=m.id WHERE h.id=?',(int(i),))
	liste = []
	liste.clear()
	for (url,visit_date) in im:
		liste.append(url)
		liste.append(visit_date)
	return liste