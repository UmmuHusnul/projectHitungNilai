x = int(input("Banyaknya nilai : "))

#i = 1
jumlah = 0 #untuk menyimpan jumlah nilai saat ini
#while i <= x:
for i in range(1,x + 1):
    print("Masukkan nilai ke-",i) 
    y = int(input("> "))#untuk meminta nilai dari user disimpan di variabel
    #i = i+i
    jumlah = jumlah+y #untuk menjumlahkan nilai inputan dari user
    print("hasil jumlah : ", jumlah)
print("Total semua nya : ", jumlah)