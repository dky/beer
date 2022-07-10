#!/usr/bin/env python3

import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("beer.db")
c = conn.cursor()

c.execute("SELECT * from beer_counter ORDER BY count DESC LIMIT 30")

items = c.fetchall()

print(tabulate(items, headers=['User', 'Count']))

conn.close()
