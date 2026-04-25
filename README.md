# IMDB ELT Pipeline using Python and PostgreSQL

The pipeline performs the following steps:
- downloads compressed dataset files from IMDB (tsv format / gz archive);
- saves files to a local directory;
- extracts .gz files;
- creates a PostgreSQL table;
- loads data into the PostgreSQL table;
- deletes temporary files after successful loading.

## How to run the script:
- first, launch your PostgreSQL server;
- create a database for the project;
- choose a link from which you want to extract data;
- create a directory where you want to save a file;
- specify all this information in the script.

## Important notes:
- the script protects private information using a .env file;
- to run the script you need to create your own .env file in your directory as shown in the example;
- in my case, I only needed 5 columns out of 6 from the source dataset;
- I chose the following approach: create a table that matches the source dataset and then drop it later.

## Tools:
- PostgreSQL;
- Python 3.14 (psycopg, requests, gzip, shutil, os, dotenv).






