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