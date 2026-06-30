# https://just.systems

set dotenv-load := true
db-backup := env_var("DB_BACKUP")
db-user := env_var("POSTGRES_USER")
db-name := env_var("POSTGRES_DB")

ROOT := justfile_directory()


backup-db:
    docker exec postgres pg_dump -U {{db-user}} {{db-name}} > "{{db-backup}}"

restore-db:
    docker exec -i postgres psql -U {{db-user}} -d postgres -c "DROP DATABASE IF EXISTS {{db-name}};"
    docker exec -i postgres psql -U {{db-user}} -d postgres -c "CREATE DATABASE {{db-name}};"
    cat "{{db-backup}}" | docker exec -i postgres psql -U {{db-user}} -d {{db-name}}

users:
    docker exec -i postgres psql -U {{db-user}} -d {{db-name}} -c "SELECT * FROM users;"

tables:
    docker exec -i postgres psql -U {{db-user}} -d {{db-name}} -c "\d"
