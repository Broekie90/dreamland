import sqlite3, json, pathlib

DB = pathlib.Path("exports/Dreamland.db")   # <-- pas aan naar jouw echte sqlite file
OUT = pathlib.Path("data.json")

QUERY = """
SELECT orignal_internal_id AS Old_internal_id, ns_internalid AS New_internal_id, created_in_ns AS Created_in_NS, 'Done' AS Status
FROM item
Where created_in_ns = 1
ORDER BY orignal_internal_id;
"""

def main():
    if not DB.exists():
        raise FileNotFoundError(f"SQLite file not found: {DB}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(QUERY)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} with {len(rows)} rows")

if __name__ == "__main__":
    main()
