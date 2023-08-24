###
- flight app user buraya kopyalandi. 
- kopyaladiktan sonra installed apslere     
    'rest_framework.authtoken',
    'dj_rest_auth',

    #!My Apps
    'users',

- postmanda login logout kontrolu.
- car_app create
- "detail": "CSRF Failed: CSRF token missing."    postmande bu hatayi aldik. settings.py de TokenAuthentication ayari unuttuk user app den sonra

- car_app de cars ve reservation modelleri olsuturduk 
- serializers
- views.py olusturuyoruz. 
- postman de get post yaptik arabalari gördük..

### Kullaniciya göre islem yapma 
- views.py
- sadece admin olanlar car üretsin.
- permission_classes isimize yaramadi 
- create permissions.py
- artik sadece token i olan admin özelligi olan kullanici post yapiyor. 
- serializersda görmek istedigimiz alani secicez kisiye göre.
- 