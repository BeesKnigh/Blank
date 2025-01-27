# Модуль Б. Документация

## Установка и запуск
1. Убедитесь, что Docker установлен.
2. Запустите команду для сборки контейнера:
   ```bash
   docker build -t article-annotator .
   ```
4. Запустите контейнер:
   ```bash
   docker run -p 8000:8000 -p 8501:8501 article-annotator
   ```
5. Откройте браузер и перейдите по адресу `http://localhost:8501` для доступа к пользовательскому интерфейсу.

## Использование
- Вставьте текст научной статьи в текстовое поле и нажмите "Создать аннотацию".
- Аннотация будет сгенерирована моделью и показана ниже.

## Структура
- `model/summarizer.py` - нейросетевая модель для создания аннотаций.
- `api/main.py` - API для взаимодействия с моделью.
- `ui/app.py` - пользовательский интерфейс для работы с моделью.



## Если не хочется запускать через докер (или по какой-то причине не получается)
1. Установи все зависимости (pip install -r requirements.txt)
2. Открой 1 терминал и пропиши это:
   ```
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
3. Открой 2 терминал и пропиши это:
   ```
   streamlit run .\ui\app.py
   ```
4. В открывшемся окне бразуера вводи промпт.