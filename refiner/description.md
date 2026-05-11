The parser/ML pipeline is a **batch ETL job** - run once (or on new dump drops); it is CPU-bound, has no HTTP surface, and produces a DB artefact

The web server **writes** for a web server to **read**

How it should work:

1. Docker builds a container, dependent on `postgresql`, with a mount `DATA_DIR`, taken from `.env`. It is dependend on `beautifulsoup4` and ML-libs;

2. ETL job #1 (parser) parses HTML files from `DATA_DIR` to a database. It ensures that tables `USERS`, `MESSAGES`, `CAMPAIGNS`, `ARCHS`, `SESSIONS`, and `CHARACTERS` exist with appropriate normalized structure;

3. ETL job #2 (dropper) drops messages from specific users, as well as messages which are replies to them;

4. ML job #1 (rp-decision-maker) decides further which messages are related to game sessions. Those can be GM/DM/storyteller's messages, player's messages, and under-the-table comments, typically started with `/` sign

5. Then, ML job #2 (campaign-manager) decides which messages belong to which campaigns, and who is the main GM of the campaign. It updates 

6. Then, ML job #3 (plot-arch-manager) decides which messages belong to which plot arch within each campaign, and who is the main GM of the plot arch

7. Then, ML job #4 (game-session-manager) decides which messages belong to which game session within each plot arch, and who is the GM of this exact game session

8. Then, ML job #5 (session-summarizer) summarizes each session

9. Then, ML job #6 (plot-arch-summarizer) summarizes each plot arch

10. Then, ML job #7 (campaign-summarizer) summarizes each campaign