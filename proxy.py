import zerorpc

c1 = zerorpc.Client()
c1.connect("tcp://127.0.0.1:1234")

c2 = zerorpc.Client()
c2.connect("tcp://127.0.0.1:1235")

class Hitung(object):
    def func(self, x, y, op):
        if (op == 1): #tambah
            return c1.tambah(x,y)
        elif (op == 2): #kurang
            return c1.kurang(x,y)
        elif (op == 3): #kali
            return c2.kali(x,y)
        elif (op == 4): #bagi
            return c2.bagi(x,y)
        else:
            return 0


s = zerorpc.Server(Hitung())
s.bind("tcp://0.0.0.0:1233")
s.run()