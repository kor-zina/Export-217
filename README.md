# Project structure

## 1. Root folder
Contents:
- gitignored `.env`, it has `LOG_LEVEL` variable set to `INFO`, `DATA_DIR` variable, pointing to a backup of raw initial data, `NOT_PLAYERS` variable, pointing to a json file, listing unneccessary players, `DB_URL` variable, pointing to a backup of a (yet inexistend) database with messages, users, campaigns, etc.
- published `.env.example`
- (yet empty) `docker-compose.yml`
- (yet empty) `justfile`
- `not_players_example.json`
- `pyproject.toml` listing members of the workspace (refiner, shared, and web-server)
- this `README.md`

## 2. Raw export data
Raw initial data, extracted from a Telegram chat, gitignored. Contents:
- 732 HTML files of dump
- media files, mentioned in those HTML files
- `script.js` for simplified browser view
- `styles.css`
Located in `${pwd}/raw_export_data`

## 3. Examples of export data
Public examples of messages.html, not gitignored.
Contents:
- `Dump analysis.md` describing the format of HTML files
- first two HTML files from the whole raw export data
Located in `${pwd}/export_example`

## 4. Refiner
A collection of batch ETL jobs for parsing and ML pipelines.
Contents:
- `pyproject.toml` listing dependencies for refiner solely
- `README.md` with more detailed description of its intended use 
Located in `${pwd}/refiner` 

## 5. Shared
A collection of SQLAlchemy models, shared enums, Pydantic DTOs, DB utilities, and shared constants
Contents:
- `pyproject.toml` listing dependencies for shared solely
- (yet) empty `README.md`
Located in `${pwd}/shared`

## 6. Web Server
FastAPI server for the future web part
- `pyproject.toml` listing dependencies for web-server solely
- (yet) empty `README.md`
Located in `${pwd}/web-server`