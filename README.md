# Project goal

There used to be a Telegram chat where just over 20 people played text-based tabletop role-playing games. Despite the vast distances between us, we were friends; we knew a lot about each other and shared many things, sent each other gifts on holidays, and wished each other happy birthdays. Some of us had the opportunity to meet in person, which they gladly took advantage of. Some of us were from Ukraine, and some were from Russia.

When the war began on February 22, 2022, some volunteered to go to the front, some joined a volunteer brigade, some became military medics, some went into hiding in the countryside, some fled their hometowns due to the bombings, some moved to another country to attend university -- and so on. In short, the shells scattered us, and many of us no longer had time for games -- it’s hard to type out your character’s actions while in a trench.

The chat was abandoned, and part of the games’ history was lost due to limits on the number of messages stored on the servers. I decided to save what remained of the games, clean out everything unrelated to them, break them down into campaigns, arcs, and sessions, create summaries for all of them, and build a tiny memorial website where each of us could revisit our games with nostalgia.

Contrary to the view promoted by culture and the state, war brings out only the worst in people and, bit by bit, strips them of their dignity.

In all countries the greater part of the people certainly detest war, and most devoutly wish for peace. A very few of them, indeed, whose unnatural happiness depends upon the public misery, may wish for war; but be it yours to decide, whether it is equitable or not, that the unprincipled selfishness of such wretches should have more weight than the anxious wishes of all good men united.

"War is sweet to them that know it not." Pindar of Boeotia

# Project structure

## 1. Root folder
Contents:
- gitignored `.env`, it has `LOG_LEVEL` variable set to `INFO`, `DATA_DIR` variable, pointing to a backup of raw initial data, `NOT_PLAYERS` variable, pointing to a json file, listing unneccessary players, `DB_URL` variable, pointing to a backup of a (yet inexistend) database with messages, users, campaigns, etc.
- published `.env.example`
- (not full yet) `docker-compose.yml`, describes a postgres container and a mount, takes in DB credentials 
- (yet empty) `justfile`
- `players_example.json`
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