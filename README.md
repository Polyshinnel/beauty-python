# Понятийный словарь

Термины используемые в рамках проекта

### Статус устройства

Статус устройства отвечает за его доступность в системе на текущий момент. 

Список статусов:
1. Online - устройство доступно для комманд и находится в сети
2. Offline - устройство не доступно или не отвечает
3. Reboot - Устройство перезагружается. После 30 секунд должно сменить статус на Online. Если не отвечает - Offilne
4. Flashed - Устройство прошивается. После 90 секунд должно сменить статус на Online. Если не отвечает - Offline

### Роль устройтва

Роль устройства - конечное представление устройства в физическом мире(розетка, лампочка, дверь, датчик света и т.д)

Текущие доступные роли устройств:
1. Лампочка(light)
2. Розетка(socket)
3. Дверь(door)
4. Пинпад(pin)
5. Локер(locker)
6. Датчик бинарного типа(digital_sensor)
7. Датчик передающий данные(analog_sensor)


### Состояние устройства

Отображает физическое состояние устройства на текущий момент времени(зависит от контекста устройства и его роли)

Список устройств и их состояний:

Общие состояния: on,off

### Методы устройства

В зависимости от роли и набора устройств для данной роли, список действий доступных для данного устройства, так же устройства деляться на устройства ввода и вывода. Все устройства вывода(управляемые), обладают методами, устройства ввода(датчики) не имеют методов управления

##### Лампочка:
1. Метод Switch

##### Розетка:
1. Метод Switch

##### Дверь:
1. Метод Open

##### Локер:
1. Метод Open


### Параметры устройств

Ввиду того, что к одному контроллеру может быть подключено несколько устройств - при работе с ними указывается параметр port к которому подключено данное устройство. 

##### Розетка:
1. Порт(port) - порт контроллера к которому подключено реле, по умолчанию 1
2. Состояние(state) - on,off

##### Лампочка:
1. Порт(port) - порт контроллера к которому подключено реле, по умолчанию 1
2. Состояние(state) - on,off

##### Дверь:
1. Состояние(state) - on,off
2. Задержка(delay) - количество секунд открытия двери
3. Звуковое оповещение(sound) - on,off
4. Световая индикация(light) - on,off

##### Локер:
1. Порт(port) - порт контроллера к которому подключен замок, по умолчанию 1

##### Пинпад:
1. Пин(pin) - пин код введенный на панели

##### Датчик бинарного типа(digital_sensor)
1. Состояние(state) - on,off
2. Порт(port) - порт контроллера к которому подключен датчик

##### Датчик передающий данные(analog_sensor)
1. Показания(value) - целое число типа int
2. Порт(port) - порт контроллера к которому подключен датчик

# Разбор отправляемых запросов к серверу устройства:

### Запрос статуса устройства

```json
{
  "device_id": "device_id",
  "port" : 1,
  "methods": [
    "status"
  ]
}
```

device_id - id устройства(обычно это серийный код)
port - не обязательный параметр, по умолчанию равен 1
status - метод запроса статуса устройства

### Перезагрузка устройства

```json
{
  "device_id": "device_id",
  "port" : 1,
  "methods": [
    "reset"
  ]
}
```


### Запрос на действие с устройством:

**Запрос на сервер устройств**

```json
{
  "role": "socket",
  "device_id": "device_id",
  "methods": [
    "switch"
  ],
  "params": {
    "port": 1,
    "state": "on"
  }
}
```

1. role - роль устройства
2. device_id - id устройства
3. methods - метод управления устройством
4. params - параметры устройства


**События получаемые в контроллер устройств /event-bus**

Открытие дверцы локера:

```json
{
  "device_id": "locker_id",
  "type": "state",
  "params": {
    "port": 1,
    "state": "open"
  }
}
```

Открытие двери:
```json
{
  "device_id": "room_controller_id",
  "type": "state",
  "params": {
    "state": "open"
  }
}
```

Ввод пинкода:
```json
{
  "device_id": "room_controller_id",
  "type": "pin",
  "params": {
    "pin": "pincode"
  }
}
```
Notice: в качестве данных с пинкода могут приниматься: 4 цифры - код для брони, 6 цифр - код для локера, цифробуквенное сочетание - карта доступа

Датчик бинарного типа(digital_sensor):
```json
{
  "device_id": "device_id",
  "type": "state",
  "role": "digital_sensor",
  "params": {
    "state": "on"
  }
}
```

Датчик передающий данные(analog_sensor):
```json
{
  "device_id": "device_id",
  "type": "state",
  "role": "analog_sensor",
  "params": {
    "value": "1234"
  }
}
```

# Настройка сервера:

Инструкция написана для операционной системы Ubuntu 22.04

### Установка Apache
1.  sudo apt update
2.  sudo apt upgrade
3.  sudo apt install apache2
4.  sudo systemctl enable apache2


### Установка MySQL
1. sudo apt install mysql-server mysql-client

### Создание пользователя для phpmyadmin
1. sudo mysql -u root -p - пароль по умолчанию пустой
2. CREATE USER 'admin' IDENTIFIED BY 'пароль'; - создаем пользователя
3. GRANT ALL PRIVILEGES ON *.* TO 'admin'; - даем все привелегии
4. FLUSH PRIVILEGES; - применяем привелегии

### Установка php для работы phpMyAdmin
1. sudo apt install php - по умолчанию УЖЕ стоит версия 8.1
2. sudo apt install libapache2-mod-php - модуль apache для работы с php
3. sudo apt install php-curl php-memcached php-mysql php-pgsql php-gd php-imagick php-intl php-mcrypt php-xml php-zip php-mbstring - ставим все необходимые модули для php

### Установка phpmyadmin - оболочка для работы с базами данных
1. sudo apt -y install phpmyadmin
2. sudo nano /etc/apache2/apache2.conf
3. В конец конфиг файла добавить Include /etc/phpmyadmin/apache.conf
4. sudo systemctl restart apache2

### Комманды для работы с Apache:
1. sudo systemctl status apache2 - посмотреть статус службы
2. sudo systemctl restart apache2 - перезапустить апач
3. sudo systemctl start apache2 - запустить апач
4. Логи по ошибкам можно посмотреть тут: cat /var/log/apache2/error.log

### Установка оснастки для WSGI
1. sudo apt install libapache2-mod-wsgi-py3 - модуль apache для работы с WSGI
2. sudo apt-get install python3-pip
3. sudo pip3 install flask, flask_sqlalchemy, mysqlclient

### Настройка WSGI для проекта:
1. В корне проекта создаем app.wsgi
2. В нем прописываем путь до папки с приложением: sys.path.insert(0, '/var/www/beauty-python')
3. Импортируем app из файла точки входа(в моем случае это runner.py) - from runner import app as application
4. Создаем виртуальный хост по адресу: /etc/apache2/sites-enabled/sitename.conf
5. В конфиге после DocumentRoot прописать:
```
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/путь до wsgi файла
WSGIApplicationGroup %{GLOBAL}
<Directory flaskapp>
     WSGIProcessGroup flaskapp
     WSGIApplicationGroup %{GLOBAL}
     Order deny,allow
     Allow from all 
</Directory>
```
6. Перезагружаем сервер: sudo service apache2 restart


# Развертывание проекта
1. Переименовать файл config-init.py в config.py
2. Настроить подключение к БД - где mysql://username:password@localhost/db_name

```python
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
                              'mysql://beauty_dev:test123@localhost/beauty_dev'

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
                              'mysql://beauty_dev:test123@localhost/beauty_dev'
```

3. Зайти в консоль Python и произвести следующие комманды:

```python
from runner import app,db
app.app_context().push()
db.create_all()
```
Тут мы делаем следующее - создаем контекст приложения: app_context и запускаем создание базы данных


# Описание методов API

Универсальное api для работы с приложением. 

### Авторизация - метод POST

**Адрес:** /authorize

**Описание:** запрашивает логин и пароль, в случае успешной авторизации отдает токен

**Параметры:**
1. user - имя пользователя
2. pass - пароль

**Ответ:** 

```json
{
  "token": "66c277d84d0066facb1ad91ea505d119",
  "err": "none"
}
```

### Добавление бронирования - метод POST

**Адрес:** /add-booking

**Описание:** интерфейс для добавления бронирования

**Параметры:**
1. token - токен для авторизации
2. pin - пин код для двери
3. location_id - id локации
4. room_id - id комнаты
5. work_place - id рабочего места(чтобы включить электроприборы именно в выделенном месте)
6. date_start - дата начала бронирования
7. date_end - дата окончания бронирования

**Ответ:** 

```json
{
  "booking_res": true,
  "err": "none"
}
```
