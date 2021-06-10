#!/usr/bin/python

import psycopg2
from config import conn

def check_root(m):
    cursor = conn.cursor()
    cursor.execute(f"SELECT row_number() OVER(ORDER BY message::int DESC), root FROM top_users WHERE user_id = {m.from_user.id};")
    rows = (cursor.fetchall())[0][1]
    return (rows, conn, cursor)