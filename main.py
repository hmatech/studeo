import requests

print("Hello Friend!")

try:
    r = requests.get('https://google.co.id')
    print(r.status_code)
    if r.status_code == 200:
        print("Halaman sukses dimuat!")
except Exception as e:
    print("Ada error!", e)