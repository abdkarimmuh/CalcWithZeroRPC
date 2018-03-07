import func1
import zerorpc

class Server1(object):
    def tambah(self, x,y):
        print("Tambah")
        return x + y

    def kurang(self, x,y):
        print("Kurang")
        return x - y

s = zerorpc.Server(Server1())
s.bind("tcp://0.0.0.0:1234")
s.run()