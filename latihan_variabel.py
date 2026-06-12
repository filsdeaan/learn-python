# soal 1. Buat program sederhana untuk menghitung total belanja.

nama_makanan = "Kebab"
harga_satuan = 8000
jumlah_pembelian = int(input("Jumlah pembelian?: "))
total = jumlah_pembelian * harga_satuan

print("Pesananmu: ", nama_makanan)
print("Jumlah: ", jumlah_pembelian)
print("Totalnya adalah: ", total)

# soal 2. Buat variabel untuk menyimpan data siswa.

nama = "Abyan"
umur = 16
tinggi_badan = 166.6
status_pelajar = True

print(nama)
print(umur)
print(tinggi_badan)
print(status_pelajar)

# soal 3. Kalkulator penghitung sisa kuota.

total_kuota = 8 

pemakaian1 = int(input("Pemakaian (1) kuota berapa?: "))
pemakaian2 = int(input("Pemakaian (2) kuota berapa?: "))

sisa_kuota = total_kuota - (pemakaian1 + pemakaian2)

print(f"Sisa kuota kamu adalah: {sisa_kuota} GB")

# soal 4. Kalkulator pengelola pembagian uang.

# pakai metode 50/30/20

uang_jajan = float(input("Uang jajan kamu berapa:"))

untuk_kebutuhan = 50/100 * uang_jajan
untuk_keinginan = 30/100 * uang_jajan
untuk_tabungan = 20/100 * uang_jajan

print("Untuk kebutuhan: ", untuk_kebutuhan)
print("Untuk keinginan: ", untuk_keinginan)
print("Untuk tabungan: ", untuk_tabungan)

# soal 5. Buat program sederhana untuk mencatat perkembangan berat badan.

berat_awal = float(input("Berat badan kamu sekarang?: "))
berat_target = float(input("Target berat badan kamu?: "))
kenaikan_berat = float(input("Kenaikan berat badan kamu bulan ini?: "))

berat_progress = berat_awal + kenaikan_berat
sisa_target = berat_progress - berat_target

print(f"Berat kamu sekarang {berat_progress} Kg")
print(f"Sisa menuju target {sisa_target} Kg")