import requests
url_provinsi = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
url_kodepos = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
data_provinsi = requests.get(url_provinsi)
data_kodepos = requests.get(url_kodepos)

# Cari kode provinsi untuk banten dan jawa barat
# print(data_provinsi.json())
kodepos_banten = data_kodepos.json()["36"]
kodepos_jawabarat = data_kodepos.json()["32"]

# Cari index kode pos sampora dari data kode pos banten
for dictionary in kodepos_banten:
    if dictionary["urban"] == "SAMPORA":
        index_sampora = kodepos_banten.index(dictionary)

# Cari index kode pos citarum dari data kode pos jawa barat
for dictionary in kodepos_jawabarat:
    if dictionary["urban"] == "CITARUM":
        index_citarum = kodepos_jawabarat.index(dictionary)

# Kodepos
kodepos_sampora = kodepos_banten[index_sampora]["postal_code"]
kodepos_citarum = kodepos_jawabarat[index_citarum]["postal_code"]
print("Kode Pos lokasi Dilan adalah " + kodepos_sampora)
print("Kode Pos lokasi Milea adalah " + kodepos_citarum)

# Hitung jarak antara kode pos sampora dan citarum
api_key = '4so5q9zrJyhfJHCqYpmlZWVZBn5ocQTcQ9wMmtGPZk7nTiFTum5zyKb3JiLcEZPH'
url_zipcode = f'http://www.zipcodeapi.com/rest/{api_key}/distance.json/{kodepos_sampora}/{kodepos_citarum}/km'
data = requests.get(url_zipcode)
jarak = data.json()['distance']
print('Jarak Dilan & Milea adalah ' + str(jarak) + ' km')

