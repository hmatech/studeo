
print('Eksekusi Sequential alias berurut')
print('#1 Halo')
print('#2 Saya Python')
print('#3 ini adalah eksekusi perintah print secara berurutan')
print('-'*20)

print('Ini adalah eksekusi terpilih dengan if')
tes = input('Apa jenis kelamin anda?(LK/PR): ')
if tes == 'LK' or tes == 'lk':
    print('Anda memiliki suara yang lantang dan mengandalkan logika!')
elif tes == 'PR' or tes == 'pr':
    print('Anda memiliki suara yang lemah lembut dan mengandalkan perasaan!')
else:
    print('Pilihan tidak ada!')
print('Selesai eksekusi terpilih')
print('-'*20)

print('Ini eksekusi menggunakan perulangan')
try:
    jumlah_teman = int(input('Masukkan jumlah teman: '))
    for i in range(0, jumlah_teman):
        print(f'Teman ke-{i + 1}')
except ValueError:
    print('Harap masukkan angka!')
