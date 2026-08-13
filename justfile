# https://just.systems

# Basic just declarations
set dotenv-load := true
ROOT := justfile_directory()

# Database variables
db-backup := env_var("DB_BACKUP")
db-user := env_var("POSTGRES_USER")
db-name := env_var("POSTGRES_DB")

# Exported HTML data
raw-export-data := env_var("DATA_DIR")


backup-db:
    docker exec postgres pg_dump -U {{db-user}} {{db-name}} > "{{db-backup}}"

restore-db:
    docker exec -i postgres psql -U {{db-user}} -d postgres -c "DROP DATABASE IF EXISTS {{db-name}};"
    docker exec -i postgres psql -U {{db-user}} -d postgres -c "CREATE DATABASE {{db-name}};"
    cat "{{db-backup}}" | docker exec -i postgres psql -U {{db-user}} -d {{db-name}}

restore-raw:
    cp -a {{raw-export-data}}/. {{ROOT}}/raw_export_data

users:
    docker exec -i postgres psql -U {{db-user}} -d {{db-name}} -c "SELECT * FROM users;"

tables:
    docker exec -i postgres psql -U {{db-user}} -d {{db-name}} -c "\d"
