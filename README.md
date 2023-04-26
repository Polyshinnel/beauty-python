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
1. Лампочка
2. Розетка
3. Дверь
4. Пинпад
5. Локер


### Состояние устройства

Отображает физическое состояние устройства на текущий момент времени(зависит от контекста устройства и его роли)

Список устройств и их состояний:

1. **Лампочка** - включить(enabled), выключить(disabled)
2. **Розетка** - включить(enabled), выключить(disabled)
3. **Дверь** - открыт(open), закрыт(closed)
4. **Пин пад** - включить(enabled), выключить(disabled)
5. **Локер** - открыт(open), закрыт(closed)

### Методы устройства

В зависимости от роли и набора устройств для данной роли, список действий доступных для данного устройства:

##### Лампочка:
1. Метод Switch с аргументами: on, off

##### Розетка:
1. Метод Switch с аргументами: on, off

##### Дверь:
1. Метод Open с аргументами: time(в секундах), отвечает на сколько именно дверь будет открыта, при указании времени 0 - деверь будет открыта постоянно

##### Пин Пад:
1. Метод Beep с аргументами: count - количество звуковых сигналов
2. Метод Light с аргументами: count - количество вспышек встроенного светодиода
3. Метод Frequency с аргументами: Low, Hight - отвечает за частоту сигнала встроенного бипера

##### Локер:
1. Метод Open с аргументами: 0 для постоянного открытия локера(так как нам не требуется его закрывать)




# Разбор отправляемых запросов к серверу устройства:

### Запрос статуса устройства

**Запрос на сервер устройств**

```json
{
  "location_id": "1",
  "room_id": "1",
  "work_place": "1",
  "device_id": "1234-1234"
}
```

1. location_id - id локации
2. room_id - id комнаты
3. work_place - id рабочего места(если в комнате всего одно рабочее место, id = 1)
4. device_id - серийный номер устройства

**Ожидаемый ответ в контроллер /event-bus**

```json
{
  "type": "status",
  "location_id": "1",
  "room_id": "1",
  "work_place": "1",
  "device_id": "1234-1234",
  "status": "Offline"
}
```

Возможные статусы:
1. Online - устройство доступно для комманд и находится в сети
2. Offline - устройство не доступно или не отвечает
3. Reboot - Устройство перезагружается. После 30 секунд должно сменить статус на Online. Если не отвечает - Offilne
4. Flashed - Устройство прошивается. После 90 секунд должно сменить статус на Online. Если не отвечает - Offline



### Запрос на смену состояния устройства:

**Запрос на сервер устройств**

```json
{
  "location_id": "1",
  "room_id": "1",
  "work_place": "1",
  "device_id": [
    "1234-1234"
  ],
  "methods": {
    "switch": "on"
  }
}
```

1. location_id - id локации
2. room_id - id комнаты
3. work_place - id рабочего места(если в комнате всего одно рабочее место, id = 1)
4. device_id - массив из серийных номеров устройства. В случае если устройство отдно, передается массив из одного элемента
5. methods - набор методов для устройства


**Ожидаемый ответ в контроллер /event-bus**
```json
{
  "type": "state",
  "location_id": "1",
  "room_id": "1",
  "work_place": "1",
  "device_id": [
    "1234-1234"
  ],
  "state": "enabled"
}
```
state - передает параметры для смены статуса в дашборде


**ВНИМАНИЕ! ИСКЛЮЧЕНИЕ ДЛЯ СОБЫТИЯ РАБОТЫ С PIN PAD!**

При вводе данных на клавиатуру издет отправка JSON следующего вида:

```json
{
  "type": "pin-pad",
  "location_id": "1",
  "room_id": "1",
  "work_place": "1",
  "device_id": "1234-1234",
  "pin": "1234"
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
