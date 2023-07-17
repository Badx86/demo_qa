# Используйте базовый образ Python
FROM python:3.9.13

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте зависимости проекта в контейнер
COPY requirements.txt .

# Установите зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Скачивание Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Установка Chrome
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Скопируйте файлы вашего проекта в контейнер
COPY . .

# Запустите команду для запуска вашего приложения
CMD [ "pytest", "-s", "-v", "--alluredir=allure-results" ]
