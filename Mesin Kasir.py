
#======Nama Warung======
print ("                 | WARUNG KOPI KONEKSI - PAK BUDI |                         ")
print ()

#======Sambutan======
print ("============================================================================")
print ("            Selamat datang di Warung kopi KONEKSI - Pak Budi                ")
print ("            Silahkan pilih menu yang Tersedia di daftar menu                ")
print()
print ("                        = SELAMAT MENIKMATI =                               ")
print ()

#======Daftar Menu======
print ("============================= DAFTAR MENU ==================================")
print ()
print (" -----------------------------------------------")
print (" | NO |       Drink            |    HARGA      |")
print (" -----------------------------------------------")
print (" | 1. | Americano              | Rp.19.000     |")
print (" | 2. | Cafe Latte             | Rp.21.000     |")
print (" | 3. | caramel Macchiato      | Rp.25.000     |")
print (" | 4. | Matcha Latte           | Rp.26.000     |")
print (" | 5. | Chocolate Latte        | Rp.21.000     |")
print (" | 6. | ice Tea                | Rp.15.000     |")
print (" | 7. | Lemon Tea              | Rp.17.000     |")
print (" -----------------------------------------------")

print ()
print (" -----------------------------------------------")
print (" | NO |       Food             |    HARGA      |")
print (" -----------------------------------------------")
print (" | 8. | Koneksi Mix Platter    | Rp.30.000     |")
print (" | 9. | Cranberry Cream Cheese | Rp.26.000     |")
print (" | 10.| Chocolate Croissant    | Rp.18.000     |")
print (" | 11.| Almond Croissant       | Rp.20.000     |")
print (" | 12.| Sourdough Egg Toast    | Rp.23.000     |")
print (" -----------------------------------------------")
print ()

#======Pemesanan======
print ("============================ PEMESANAN =====================================")
print ()
Nama = input( "Masukan Nama Anda : ") # input nama user

pilihan = int(input("Masukan No Menu : ")) #input pilihan menu
QTY  = int(input("Masukan Jumlah pesanan : ")) #input banyaknya menu yang di pesan
Bayar = int (input("Bayar: ")) #input uang yang di bayar user

# Menentukan nama produk dan harga berdasarkan nomor menu yang dipilih
if pilihan == 1 :
  Harga = 19000
  nama_produk= "Americano"
elif pilihan == 2 :
  Harga = 21000
  nama_produk= "cafe_Latte"
elif pilihan == 3 :
  Harga = 25000
  nama_produk= "caramel_Macchiato"
elif pilihan == 4 :
  Harga = 26000
  nama_produk= "Matcha_Latte"
elif pilihan == 5 :
  Harga = 21000
  nama_produk= "Chocolate_Latte"
elif pilihan == 6 :
  Harga = 15000
  nama_produk= "ice_Tea"
elif pilihan == 7 :
  Harga = 17000
  nama_produk= "lemon_Tea"
elif pilihan == 8 :
  Harga = 30000
  nama_produk= "Mix_Platter"
elif pilihan == 9 :
  Harga = 26000
  nama_produk = "Cranberry_Cream_Cheese"
elif pilihan == 10 :
  Harga = 18000
  nama_produk =   "Chocolate_Croissant"
elif pilihan == 11 :
  Harga = 20000
  nama_produk = "Chocolate_Almond"
elif pilihan == 12 :
  Harga = 23000
  nama_produk = "Sourdough_Egg_Toast"
else :
  print ("Menu dengan Nomor tersebut tidak ada , masukan Nomor pesanan yang benar !")

Sub_Total = Harga * QTY # menghitung subtotal per produk
Diskon = float (0.10) # menentukan jumlah diskon sebesar 10%
Total_Diskon = Sub_Total * Diskon # menghitung jumlah diskon yang di dapat user
kembali = Bayar - Sub_Total # menghitung uang Kembalian user

print ()
print ()

# Menampilkan struk pesanan
print ("=========================================================")

print ("                    STRUK PESANAN                        ")

print ("=========================================================")

print ()

print ("          Nama      : ",Nama)

print ("          pesanan   : ", nama_produk)

print ("          Harga          = ", Harga )
print ("         ",QTY, "x", Harga,"     = ", Sub_Total,)

print ()

print ("---------------------------------------------------------")

print ("          Sub_Total : ",Sub_Total)
print ("          Diskon    : ",int (Total_Diskon))
print ()
print ("          Total     : ",int (Sub_Total - Total_Diskon)) #menampilkan Total yang harga setelah di diskon
print ("          Bayar     : ", Bayar)
print ("          Kembali   : ",kembali)
print ()
print ("=========================================================")

# Menampilkan ucapan terimakaasih pada struck
print ("             Terimakasih Telah Berbelanja")

print ("          | WARUNG KOPI KONEKSI - PAK BUDI |")

print ("=========================================================")

# ==================== SOAL REFLEKSI ====================

# 1. Tipe data apa saja yang kamu gunakan dan kenapa?
# Saya menggunakan tipe data String, Integer, dan Float.
# String digunakan untuk menyimpan data berupa teks seperti nama pelanggan dan nama produk.
# Integer digunakan untuk data angka bulat seperti jumlah pesanan dan pembayaran.
# Float digunakan untuk nilai yang memiliki angka desimal, seperti diskon.

# 2. Bagian mana yang paling sulit kamu pahami saat mengerjakan?
# Bagian yang paling sulit saya pahami adalah penggunaan while dan boolean, awalnya saya mau membuat pelanggan dapat memesan lebih dari satu kali, tapi tidak jadi

# 3. Jelaskan dengan kata-katamu sendiri: apa perbedaan int(), float(), dan str() pada saat menerima input?
# int() digunakan untuk mengubah input menjadi angka bulat, sedangkan float() digunakan untuk mengubah input menjadi angka yang dapat memiliki nilai desimal. Sementara itu, str() digunakan untuk mengubah input menjadi teks atau String. Jadi, perbedaannya adalah jenis data yang dihasilkan dari input tersebut.












