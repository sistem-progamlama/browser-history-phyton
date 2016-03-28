import datetime

import mysql.connector
from User import User as de
def getir(User):
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
		host='185.86.12.173',
		database='history')
	cursor = cnx.cursor()
	query = 'SELECT `id`, `adi`, `sifre`, `email` FROM `User` WHERE `adi`=\'%s\' and  `sifre`=\'%s\'' % (User.adi,User.sifre)
	cursor.execute(query)
	u=de
	for (id,adi,sifre,email) in cursor:
		de.adi=adi
		de.mail=email
		de.sifre=sifre
		de.uid=id
		print(u.adi+" girildi")
		return True
	cnx.close
	return False
def üyeOl(User):
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
                              host='185.86.12.173',
                              database='history')

	cursor = cnx.cursor()
	query = 'INSERT INTO `User`(`adi`, `sifre`, `email`) VALUES (\'%s\',\'%s\',\'%s\')' % (User.adi,User.sifre,User.mail)
	cursor.execute(query)
	cnx.commit()

def placesIdGetir(place):
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
                              host='185.86.12.173',
                              database='history')
	cursor = cnx.cursor()
	query = 'SELECT id from places where url=\"%s\"' % (place)
	print(query)
	cursor.execute(query)

	for i in cursor:
		return i[0]
	cnx.close
	return False
def placesEkle(place):
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
                              host='185.86.12.173',
                              database='history')
	cursor = cnx.cursor()
	query = 'INSERT INTO `places`( `url`) VALUES (\"%s\")' % (place)
	cursor.execute(query)
	cnx.commit()

def kayıtEkle(kayıt,browser_id,tarih):
	if(placesIdGetir(kayıt)==False):
		placesEkle(kayıt)
	id=placesIdGetir(kayıt)
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
                              host='185.86.12.173',
                              database='history')
	cursor = cnx.cursor()
	query = 'INSERT INTO `history`( `user`, `url`, `b_id`, `tarih`) ' \
	        'VALUES (%s,%s,%s,\"%s\")' % (de.uid,id,browser_id,milltoDate(tarih,browser_id))
	print(query)
	cursor.execute(query)

	cnx.commit()

def gecmisGetir():
	cnx = mysql.connector.connect(user='baydar1', password='celacelal94',
                              host='185.86.12.173',
                              database='history')
	cursor = cnx.cursor()
	query = 'SELECT p.url,h.tarih,b_adi FROM places p INNER JOIN history h on p.id=h.url ' \
	        'inner join browser b on b.b_id=h.b_id WHERE user=\'%s\'' % (de.uid)
	cursor.execute(query)
	liste = []
	liste.clear()
	for (url,tarih,b_adi) in cursor:
		liste.append([url,tarih,b_adi])
	return liste

def milltoDate(i,tarayıcı):
	base_datetime=None
	if tarayıcı==1:
		bölüm=1000000
		base_datetime = datetime.datetime( 1970, 1, 1 )
	elif tarayıcı==2:
		bölüm=1000000
		base_datetime = datetime.datetime(1601,1,1)

	target_date_time_ms = int(i/bölüm)*1000
	print(target_date_time_ms)

	delta = datetime.timedelta( 0, 3, 0, target_date_time_ms )
	target_date = base_datetime + delta
	print(target_date)
	return target_date
