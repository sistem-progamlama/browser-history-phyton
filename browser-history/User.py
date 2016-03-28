class User:

    adi=''
    sifre=''
    mail=''
    uid=''
    def __init__(self):
        print("User")
    def __init__(self,ad,sif):
        self.adi=ad
        self.sifre=sif
    def __init__(self,ad,sif,email):
        self.adi=ad
        self.sifre=sif
        self.mail=email

