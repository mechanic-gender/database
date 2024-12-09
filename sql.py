import sqlite3
from sqlite3 import connect


# cur.execute("create table fractions (id integer primary key autoincrement,"
#             "fraction text unique not null,"
#             "location text not null);")
# cur.execute("create table character (id integer primary key autoincrement,"
#             "character text not null,"
#             "name text not null,"
#             "fraction_h_l integer not null,"
#             "skils  text not null"
#             "foreign key(fraction_h_l) references fractions(id)"
#
db=sqlite3.connect("swc.db")
cur=db.cursor()
cur.execute('INSERT INTO fractions (id, fraction, location) VALUES (?, ?, ?),(1, banking_clan, Muunilinst)')
conn.commit()
conn