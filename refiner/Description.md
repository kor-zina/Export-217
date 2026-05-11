The parser/ML pipeline is a **batch ETL job** - run once (or on new dump drops); it is CPU-bound, has no HTTP surface, and produces a DB artefact

The web server **writes** for a web server to **read**

How it should work:

1. Docker builds a container, dependent on `postgresql`, with a mount `DATA_DIR`, taken from `.env`. It is dependend on `beautifulsoup4` and ML-libs;

2. ETL job #1 (parser) parses HTML files from `DATA_DIR` to a database. It ensures that tables `USERS`, `MESSAGES`, `USERS_MESSAGES`,  `CAMPAIGNS`, `CAMPAIGN_MESSAGES`, `ARCHS`, `ARCH_MESSAGES`, `SESSIONS`, `SESSION_MESSAGES`, `CHARACTERS`, `USER_CHARACTERS`, and `CHARACTER_CAMPAIGNS` exist with appropriate normalized structure. It updates tables `MESSAGES`, `USERS`, and `USERS_MESSAGES`;

3. ETL job #2 (dropper) drops messages from specific users, as well as messages which are replies to them. The list of usernames is stored in a file, specified in `NOT_PLAYERS` environment variable;

4. ML job #1 (rp-decision-maker) decides further which messages are related to game sessions and drops all unrelated ones from `MESSAGES` table. It also drops users from `USERS` table if nessessary. RP-related messages can be GM/DM/storyteller's messages, player's messages, under-the-table comments, typically started with `/` sign, commands to different roll-bots (Telegram bots used to roll the dices). The rest is not needed;

5. ML job #2 (session-splitter) decides which messages belong to which game session, and who is the GM of this exact game session. As a general rule (and there are likely no exceptions), gaming sessions can be divided by time, as they take place continuously. They never last longer than 24 hours, but often extend into the night, starting before midnight and ending after midnight on the following day. Each session, users play one character (sometimes they also play their character's companion), and GM plays multiple characters. The job extracts characters' names and maps them to users. It also decides which user is a GM, and so, which characters are PCs and which are NPCs. It updates tables `MESSAGES`, `SESSIONS`, `SESSION_MESSAGES`, `CHARACTERS`, and `USER_CHARACTERS`;

6. ML job #3 (campaign-manager) decides which messages belong to which campaigns, and who is the main GM of the campaign. Campaigns differ by game rules (stats, how dices are rolled, etc.), game setting, locations. Usually, by characters too, but some characters have taken part in multiple campaigns. Some users have always created a new PC for a new campaign and can act like beacons in that regard. The main GM is that user who was the GM of the most of the sessions within a campaign. The job updates tables `CAMPAIGNS` and `CAMPAIGN_MESSAGES`;

7. ML job #4 (plot-arch-manager) decides which messages belong to which plot arch within each campaign, and who is the main GM of the plot arch. It is the most intricate and complicated part, as it relies heavily on major plot events, such as PCs moving to another city, change of antagonists, change of GMs, etc. For example, in one of the campaigns, three users mainly were players, but had led their own plot arch in which they acted like GMs. The job updates tables `MESSAGES` and `ARCHS`;

8. ML job #5 (session-summarizer) summarizes each session. It updates only `SESSIONS` table;

9. ML job #6 (plot-arch-summarizer) summarizes each plot arch. It updates only `ARCHS` table;

10. ML job #7 (campaign-summarizer) summarizes each campaign. It updates only `CAMPAIGNS` table;

11. ML job #8 (character-descriptor) summarizes characters' personalities and their biography.