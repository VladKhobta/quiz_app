# quiz_app

## Стек технологий
FastAPI, SQLAlchemy, PostgreSQL, Alembic

## Инструкции по запуску

1. Клонируем проект в любое удобное место.
   ```git clone https://github.com/VladKhobta/quiz_app.git```
2. Собираем образ и запускаем контейнеры с помощью следующей команды:
   ```docker-compose up -d --build```
3. Создаем таблицы внутри контейнера на основании миграций с помощью:
   ```docker-compose exec web alembic upgrade head```

## Взаимодействие

1. http://localhost:8888/docs -- интерактивная документация.
2. Для взаимодействия с PostgreSQL:
   1. Если есть pgAdmin, можно добавить сервер (Register > Server) с параметрами:
      - host: localhost
      - port: 5432
      - username: postgres
      - password: postgres
   2. Либо, для доступа из интерактивной оболочки:
      ```
      docker-compose exec -it db bash
      psql -U postgres
      ```
      Можно попробовать, например:
      ```
      SELECT * FROM questions;
      ```
