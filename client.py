import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:1233")

x = input("Masukan angka pertama : ")
y = input("Masukan angka kedua : ")

print("Pilihan Operasi\n1.tambah\n2.kurang\n3.kali\n4.bagi")

op = input("Operasi : ")

print(c.func(x,y,op))