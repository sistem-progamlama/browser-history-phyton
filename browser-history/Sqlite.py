import sqlite3 as sql



def chromiumGecmisGetir():
	vt = sql.connect('/home/celal/.config/chromium/Default/History')
	im = vt.cursor()
	im.execute("""select max(id) from visits """)
	for i in im:
		return i


