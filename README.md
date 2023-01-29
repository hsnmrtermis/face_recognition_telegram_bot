# Face Recognition Telegram App
Telegram üzerinden attığımız fotoğrafta kimlerin olduğunu bize yazan bot uygulaması.

![Ekran Görüntüsü](./output.gif "Ekran görüntüsü")

# Kurulum
## Docker
- [ ] docker -t face_recognition_postgres .

- [ ] docker run -d -p face_recognition_postgres

## Virtual Environment
- [ ] source venv/bin/activate
- [ ] pip3 install -r requirements.txt

## Postgresql
- [ ] init.sql dosyasındaki veriler eklenmeli.


# Uygulamayı Çalıştırma

## Telegram Client
```
python3 main.py
```

## Api
```
python3 api.py
```
> http://127.0.0.1:8000/docs ile swagger arayüzünden tanımasını istediğimiz kişilerin fotoğrafını ve ismini  /person endpointine atabiliriz.

