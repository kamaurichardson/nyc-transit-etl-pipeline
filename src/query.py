import sqlite3

DB_PATH = "data/transit.db"

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.execute("""
        SELECT
            borough,
            SUM(ridership) AS total_ridership
        FROM ridership
        GROUP BY borough
        ORDER BY total_ridership DESC
    """)

    for row in cursor.fetchall():
        print(row)
