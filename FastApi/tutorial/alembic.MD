# Alembic
1. Create alembic conf ```alembic init -t async alembic```
    * alembic init - create new config
    * -t async -> template async (create file with support async)
    * alembic -> name of folder that will be created config
2. alembic revision --autogenerate -m "create items table"
   * alembic revision - create new migration
   * --autogenerate - generate migration by models (need to set metadata in env.py)
   * -m "Smth" - message for generate(name)
3. alembic upgrade head 
   * upgrade all migrations to the last migration
4. alembic downgrade -1 
   * alembic downgrade - return migration 
   * -1 -> return to 1 migration
5. alembic current -> show current migration
6. alembic history -> show all migrations
7. alembic downgrade base -> downgrade all migrations