# Poetry

## Для контроля зависимостями есть 2 основных пакета (pip-env и poetry).

### Основные команды:

1. poetry new <path> - инициализация проекта с поетру файлом (обычно не используется)
2. poetry init - инициализация poetry файлов (нужно ввести настройки)
3. poetry install - установка зависимостей с pyproject.toml
    1. poetry install --sync - синхронизировать зависимости (текущие с venv poetry) с pyproject.toml
4. poetry add <"package"> - добавление библиотеки в зависимости
5. poetry lock --no-update - перезаморозка версий
6. poetry show --tree - показ существующих зависимостей в удобном типе
7. poetry install --sync синхронизировать текущее окружение с тем, что у нас в poetry.lock
8. poetry update <package> - обновление зависимостей
pyproject.toml можно менять в ручную, но нельзя трогать poetry.lock

