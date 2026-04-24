import functions
import psycopg
import os
from dotenv import load_dotenv

# IMPORT AND UNPACK FROM IMDB_old:

url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
path = 'c:/FOREIGN/test/name.basics.tsv.gz'
new_path = 'c:/FOREIGN/test/name.basics.tsv'

functions.import_gz_file(url, path)
functions.unpack_gz(path, new_path)

# IMPORT TO POSTGRESQL:

load_dotenv()

try:
    connection = psycopg.connect(
        dbname=os.getenv('dbname'),
        user="postgres",
        password=os.getenv('password'),
        host="localhost",
        port="5432",
    )

    cursor = connection.cursor()

    cursor.execute("""

    DROP TABLE IF EXISTS name_basics;

    CREATE TABLE IF NOT EXISTS name_basics ( 
    nconst TEXT PRIMARY KEY,
    name TEXT,
    year_of_birth INTEGER,
    year_of_death INTEGER,
    professions TEXT,
    knownForTitles TEXT)
    """)

    with open(new_path, "rb") as f:
        with cursor.copy("COPY name_basics FROM STDIN WITH (DELIMITER E'\\t', HEADER, NULL '\\N')") as copy:
            data = f.read(128 * 1024)
            while data:
                copy.write(data)
                data = f.read(128 * 1024)

    cursor.execute("""
    ALTER TABLE name_basics DROP COLUMN knownForTitles;
    """)

    connection.commit()
    cursor.close()
    connection.close()

    print("Data imported")

except Exception as e:
    print(f"Ooops: {e}")


#DELETE PACKED AND UNPACKED FILES FROM DIRECTORY:

files_to_remove = [path, new_path]

for file in files_to_remove:
    os.remove(file)

print ("Packed and unpacked files deleted")



