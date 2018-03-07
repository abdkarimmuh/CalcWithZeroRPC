import func2
import zerorpc

class Server2(object):
    def kali(self, x,y):
        print("Kali")
        return x * y

    def bagi(self, x,y):
        print("Bagi")
        return x / y

s = zerorpc.Server(Server2())
s.bind("tcp://0.0.0.0:1235")
s.run()