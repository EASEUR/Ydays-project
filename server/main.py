import json
import sqlite3
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

DB = "data.db"
app = FastAPI()


class Processus(BaseModel):
    pid: int
    name: str | None = None
    cpu_percent: float
    memory_percent: float


class Mesure(BaseModel):
    hostname: str
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    top_processes: list[Processus]


def get_db():
    return sqlite3.connect(DB)


def init_db():
    with get_db() as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS machines ("
            "id INTEGER PRIMARY KEY, hostname TEXT UNIQUE NOT NULL)"
        )
        db.execute(
            "CREATE TABLE IF NOT EXISTS mesures ("
            "id INTEGER PRIMARY KEY, "
            "machine_id INTEGER NOT NULL REFERENCES machines(id), "
            "date TEXT NOT NULL, cpu REAL, memoire REAL, disque REAL, "
            "processus TEXT)"
        )


init_db()


@app.post("/mesures")
def recevoir(m: Mesure):
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO machines (hostname) VALUES (?)", (m.hostname,))
        machine_id = db.execute(
            "SELECT id FROM machines WHERE hostname = ?", (m.hostname,)
        ).fetchone()[0]
        db.execute(
            "INSERT INTO mesures (machine_id, date, cpu, memoire, disque, processus) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                machine_id,
                datetime.now(timezone.utc).isoformat(),
                m.cpu_percent,
                m.memory_percent,
                m.disk_percent,
                json.dumps([p.model_dump() for p in m.top_processes]),
            ),
        )
    return {"status": "ok"}


@app.get("/mesures")
def lister(limit: int = 20):
    with get_db() as db:
        lignes = db.execute(
            "SELECT m.hostname, x.date, x.cpu, x.memoire, x.disque "
            "FROM mesures x JOIN machines m ON m.id = x.machine_id "
            "ORDER BY x.id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [
        {"hostname": h, "date": d, "cpu": c, "memoire": me, "disque": di}
        for h, d, c, me, di in lignes
    ]