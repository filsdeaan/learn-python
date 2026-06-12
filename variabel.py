# 2 variabel berbeda, tapi nilainya sama
a = b = 1
print(a)
print(b)

angka_saya = 7
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)

# variabel itu sensitif dengan huruf besar/kecil
nama_saya = "abyan"
Nama_saya = "filsdeaan"
print(nama_saya)
print(Nama_saya)

pesan = "abyan ngoding"

print(pesan) # print isi seluruh variabel
print(pesan[0]) # print karakter pertama di data dalam variabel, dimulai dari 0, spasi juga kehitung
print(pesan[2:7]) # print dari karakter ke 2 sampai 6, aturannya memang gitu
print(pesan[6:]) # print dari karakter ke 6 sampai habis
print(pesan * 2) # print isi variabel sebanyak 2x

# bisa juga gabungkan isi variabel + nilai baru
print(pesan + "di kamar")
print(pesan, "di kamar")