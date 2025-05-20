# stackoverflow-playwright-tests
Tests for Stackoverflow website using Playwright/Python

## Описание
Проект предназначен для практиса навыков автоматизации UI/API тестирования, интеграции с CI/CD
Тесты покрывают сценарии работы с сайтом Stack Overflow: логин, навигация, работа с тегами, вопросы, комбинированные UI+API проверки

## Структура проекта
- pages/ — Page Object Model (POM) для основных страниц сайта
- tests/ — тесты (UI, API, комбинированные, мок-тест)
- requirements.txt — зависимости Python
- docker-compose.yml, Dockerfile — запуск тестов в контейнере
- .github/workflows/playwright-ci.yml — CI для автоматического запуска тестов
- .env — переменные окружения для тестовых пользователей

## Запуск тестов
### Клонирование, установка зависимостей
1. git clone https://github.com/yourusername/stackoverflow-playwright-tests.git
2. cd stackoverflow-playwright-tests
3. python -m venv .venv
4. .venv/bin/activate
5. pip install -r requirements.txt
6. playwright install --with-deps chromium

### Настройка .env
Создайте файл .env в корне проекта (*/stackoverflow-playwright-tests)
- EMAIL=your_email
- PASSWORD=your_password
- EMAIL2=your_email2
- PASSWORD2=your_password2

### Запуск тестов
- pytest -c tests/pytest.ini
- или в Docker:
docker compose up --build --exit-code-from tests

### Просмотр отчетов
allure serve tests/allure-results/

## CI/CD (github actions)
В проекте настроен GitHub Actions workflow (.github/workflows/playwright-ci.yml) для автоматического запуска тестов при каждом пуше или МР
