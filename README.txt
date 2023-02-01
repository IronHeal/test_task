установить python 3.11 на ПК(если используется windows)
установить git bash на ПК
скачать ветку main
открыть консоль, переместиться в main ветку

команды в консоли:
python -m pip install --upgrade pip #установщик пакетов для python
source .venv/Scripts/activate активация виртуального окружения
pip install coverage установка пакета для запуска юнитестов и их отчетам

python ./main.py запуск смоук теста
python -m coverage run -m unittest -v запуск самих юнитестов
python -m coverage report команда просмотра отчета по запущенным юнитестам