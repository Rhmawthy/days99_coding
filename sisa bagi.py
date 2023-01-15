'''Buatlah program yang dapat menerima inputan berupa angka 
dengan ketentuan sebagai berikut:
1. Jika angka yang diinput habis dibagi 3, maka program akan 
mencetak pesan “Pride of 3”
2. Jika angka yang diinput habis dibagi 5, maka program akan 
mencetak pesan “Pride of 5”
3. Jika angka yang diinput habis dibagi 3 dan 5, maka program 
akan mencetak pesan “Master Class”'''

angka = int (input("masukkan angka : "))

if  angka % 5 :
	print("pride of 3 ")
	
elif angka % 3 :
	print (" pride of 5 ")

elif angka % 5 and angka % 3 :
	print("master class")