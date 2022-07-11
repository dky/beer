#!/usr/bin/env python3

import sqlite3
import datetime
import sys

conn = sqlite3.connect("beer.db")
c = conn.cursor()

# Create a table to incoming beers
c.execute(
    """CREATE TABLE if not exists beers (
    username TEXT,
    reason TEXT,
    date timestamp
    )"""
)

# Table containing tally of beers for user
c.execute(
    """CREATE TABLE if not exists beer_counter (
    username TEXT UNIQUE,
    count int
    )"""
)


def increment(username):
    # Check if username already exists
    print("Checking to see if we gave", username, "any Beer")
    vals = c.execute(
        "SELECT username FROM beer_counter WHERE username=?", (username,)
    ).fetchone()

    if vals:
        print("Yes, he's got some Beer, give him another round!")
        c.execute(
            "UPDATE beer_counter SET count = count + 1 WHERE username=?", (username,)
        ).fetchone()
    else:
        print("Hasn't received any Beers so far, buying the first!")
        c.execute("INSERT INTO beer_counter VALUES (?,?)", (username, 1))


def beer(username, purpose=""):
    if purpose:
        print("Thanks! Buying a beer for", username, "for", purpose)
        c.execute(
            "INSERT INTO beers VALUES (?,?,?)",
            (username, purpose, datetime.datetime.now()),
        )
        increment(username)
        conn.commit()
    else:
        print("Thanks! Buying a beer for:", username)
        c.execute(
            "INSERT INTO beers VALUES (?,?,?)", (username, "", datetime.datetime.now())
        )
        increment(username)
        conn.commit()


if __name__ == "__main__":

    # Handle args, we should make this more robust but for now...
    # print(len(sys.argv))

    # If beer for user + reason for beer
    if len(sys.argv) == 3:
        username = sys.argv[1]
        reason = sys.argv[2]
        beer(username, reason)
    # If just beer no purpose
    elif len(sys.argv) == 2:
        username = sys.argv[1]
        beer(username)
    else:
        print("Not enough args. Try:")
        print("Usage: ./beer.py username")
        print(
            'Usage: ./beer.py username "If you want to associate a Beer for something awesome"'
        )

    conn.close()
