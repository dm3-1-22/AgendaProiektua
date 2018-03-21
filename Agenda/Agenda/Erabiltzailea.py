class Erabiltzailea:
    
    def __init__(self,izena,abizena, tel,email):        
        self.b1=izena
        self.b2=abizena
        self.b3=tel
        self.b4=email        
    
erabil1 = Erabiltzailea ('Lucia', 'Berriz', 9876, 1)
print('NAN:', erabil1.b1,',Izena:',erabil1.b2,',Helbidea:',erabil1.b3,',Telefonoa:',erabil1.b4)

class Eventos:
    
    def __init__(self, izena , kodea, inportantzia, lekua, hasiera_data, bukaera_data):        
        self.i1=izena
        self.i2=kodea
        self.i3=inportantzia
        self.i4=lekua
        self.i5=hasiera_data
        self.i6=bukaera_data     
    
eventos1 = Eventos ('Lucia', 9876, 1 , 'berriz', '1', '2')
print('Izena:', eventos1.i1,',Izena:',eventos1.i2,',Helbidea:',eventos1.i3,',Telefonoa:',eventos1.i4)