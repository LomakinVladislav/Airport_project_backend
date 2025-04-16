# Файл запускает скрипт для создания актуальных моделей из текущей версии БД.
# Необходима библиотека sqlacodegen

import subprocess
from urllib.parse import quote
from config import settings 

# Формируется URL подключения
db_url = f"postgresql+psycopg://postgres:postgressallica@localhost:5432/region_airport"

subprocess.run([
    "python", 
    "-m", 
    "sqlacodegen", 
    db_url,
    "--outfile", 
    "actual_models.py"
])