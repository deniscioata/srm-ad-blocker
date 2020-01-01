#!/usr/bin/python

from shutil import copy2
import sqlite3
import urllib
import re
import os


def backup_database(db_file, db_backup_file):
    copy2(db_file, db_backup_file)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def upgrade_database_if_needed(conn):
    inserted = is_column_inserted(conn)
    if inserted:
        print("Is already upgraded")
    else:
        print("Not upgraded -> should upgrade")
        upgrade_database(conn)
        print("upgraded")


def upgrade_database(conn):
    try:
        cur = conn.cursor()
        cur.execute("ALTER TABLE category_domain ADD COLUMN inserted_by_me BIT default 0")
        cur.execute("CREATE TABLE 'temp' ('domain' TEXT UNIQUE, 'category_id' INTEGER, 'inserted_by_me' INTEGER )")
    except sqlite3.OperationalError as error:
        print("Failed to upgrade the database: ", error)


def is_column_inserted(conn):
    cur = conn.cursor()
    try:
        cur.execute("SELECT inserted_by_me from category_domain limit 0")
        return True
    except sqlite3.OperationalError as error:
        print("Error: ", error)
    return False


def download_files():
    print("Download files")
    clean_ad_file()
    for url in re.sub(r"#(.+)", "", file('urls.txt', 'r').read()).split("\n"):
        if url is "":
            continue
        print("Downloading:", url)
        html_values = download_file(url)
        print("Finished downloading:", url)
        if html_values is not None:
            parsed_string = parse_string(html_values)
            f = open("adBlockList.txt", "a+")
            f.write(parsed_string)
            f.close()


def download_file(url):
    sock = urllib.urlopen(url)
    html_source = sock.read()
    sock.close()
    if html_source.__contains__("<!DOCTYPE html>"):
        print("Invalid document", url)
        return None
    return html_source


def parse_string(string):
    string = re.sub("\r\n", "\n", string)
    string = re.sub("\t", "", string)
    string = re.sub("127.0.0.1", "", string)
    string = re.sub("0.0.0.0", "", string)
    string = re.sub(r"#(.+)", "", string)
    string = re.sub("\n", ",3,1\n", string)
    string = re.sub("\n,3,1\n", ",3,1\n", string)
    string = re.sub("\n ", "\n", string)
    return string


def remove_current_ads(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM category_domain WHERE inserted_by_me = 1")
    cur.execute("DELETE FROM 'temp' where 1 = 1;")
    conn.commit()


def import_processed_file(conn):
    cur = conn.cursor()
    data = []
    for line in file('adBlockList.txt', 'r').readlines():
        values = line.split(",")
        if values.__len__() == 3:
            data.append(values)
    cur.executemany("INSERT OR ignore INTO temp (domain, category_id, inserted_by_me) VALUES (?, ?, ?);", data)
    conn.commit()


def apply_exceptions(conn):
    exceptions = re.sub(r"#(.+)", "", file('exceptions.txt', 'r').read()).split("\n")
    cur = conn.cursor()
    for exception in exceptions:
        cur.execute("DELETE FROM temp WHERE domain like '%" + exception + "%'")
    conn.commit()


def apply_filters(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO category_domain(domain, category_id, inserted_by_me) SELECT domain, category_id, inserted_by_me FROM temp WHERE domain not like '%#%' AND inserted_by_me = 1;")
    conn.commit()

def clean_data(conn):
    clean_ad_file()
    cur = conn.cursor()
    cur.execute("DELETE FROM 'temp' where 1 = 1;")
    conn.commit()

def clean_ad_file():
    f = open("adBlockList.txt", "w+")
    f.write("")
    f.close()

def main():
	database_path = "/var/db/syno-domain-lists/category_database.db"
	database_processing_path = "/var/db/syno-domain-lists/category_database.backup"
	print("0. Creating a backup_database")
	backup_database(database_path, database_processing_path)

	print("1. Download ad block lits:")
	download_files()

    # create a database connection
	conn = create_connection(database_processing_path)
	with conn:
		print("2. Upgrade database if needed:")
		upgrade_database_if_needed(conn)
		print("3. Cleaning current database")
		remove_current_ads(conn)
		print("4. Import processed file")
		import_processed_file(conn)
		print("5. Apply exceptions")
		apply_exceptions(conn)
		print("6. Apply filters")
		apply_filters(conn)
		print("7. Cleaning temporary data")
		clean_data(conn)
	conn.close()

	print("8. Replacing old database with new database")
	backup_database(database_processing_path, database_path)
	print("9. Cleaning temporary files")
	os.remove(database_processing_path)
	print("Done. Turn off and on Safe Access in order to use the new database. (Safe Access -> Security -> Network Protection)")

if __name__ == '__main__':
    main()