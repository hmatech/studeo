ruang_keluarga = ['TV', 'kipas Angin', 'lampu', 'dvd player']
ruang_makan = ['meja makan', 'kursi', 'piring', 'gelas']
kamar = ['kasur', 'bantal', 'guling']
ruang_tamu = ['sofa', 'meja', 'asbak']

print('-'*20)
print('Barang-barang di ruang keluarga: ')
for ke in ruang_keluarga:
    print(ke)
print('-'*20, '\n')
print('-'*20)
print('Barang-barang di ruang makan: ')
for ke in range(0, len(ruang_makan)):
    print(f'Terdapat {ruang_makan[ke]}')
print('-'*20, '\n')
print('-'*20)
print('Barang-barang di kamar: ')
for ke in range(0, len(ruang_makan)):
    print(f'{ke+1}. {ruang_makan[ke]}')
print('-'*20, '\n')
print('-'*20)
print('Barang-barang di ruang tamu: ')
for ke in range(0, len(ruang_tamu)):
    print('Ada {}'.format(ruang_tamu[ke]))
print('-'*20, '\n')
