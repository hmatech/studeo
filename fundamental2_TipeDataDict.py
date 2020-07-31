data_kantor = {
    'tanggal': '2020-07-30',
    'barang_list': [
        {'nama': 'printer', 'jumlah': 10},
        {'nama': 'komputer', 'jumlah': 5},
        {'nama': 'kertas', 'jumlah': 20},
        {'nama': 'pulpen', 'jumlah': 50},
    ],
    'karyawan_list': [
        {'nama': 'Habibie', 'usia': 19},
        {'nama': 'Sidiq', 'usia': 18},
        {'nama': 'Arya', 'usia': 20},
    ]
}

print('---Data kantor---')
print(f"Pertanggal {data_kantor['tanggal']}")
print('Daftar barang:')
for i in data_kantor['barang_list']:
    satuan = ''
    if i['nama'] == 'printer':
        satuan = 'unit'
    elif i['nama'] == 'komputer':
        satuan = 'unit'
    elif i['nama'] == 'kertas':
        satuan = 'rim'
    elif i['nama'] == 'pulpen':
        satuan = 'buah'
    print(f"\t{i['nama']} berjumlah {i['jumlah']} {satuan}")
print("="*20)
print('Daftar karyawan:')
for i in data_kantor['karyawan_list']:
    print(f"\t{i['nama']} berusia {i['usia']} tahun")
