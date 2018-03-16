class Erabiltzailea:
    
    def __init__(self,izena,abizena, tel,email):        
        self.b1=izena
        self.b2=abizena
        self.b3=tel
        self.b4=email        
    
erabil1 = Erabiltzailea ('Lucia', 'Berriz', 9876, 1)
print('NAN:', erabil1.b1,',Izena:',erabil1.b2,',Helbidea:',erabil1.b3,',Telefonoa:',erabil1.b4)