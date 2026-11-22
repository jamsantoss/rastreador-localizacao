import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse

app = FastAPI(title="Rastreador de localização")

BANCO = Path(__file__).parent / "rastreador.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabela():
    with conectar() as con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS posicoes (
                usuario TEXT PRIMARY KEY,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                atualizado_em TEXT NOT NULL
            )
            """
        )


criar_tabela()


class Posicao(BaseModel):
    usuario: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


@app.post("/posicao")
def enviar_posicao(p: Posicao):
    agora = datetime.now(timezone.utc).isoformat()
    with conectar() as con:
        con.execute(
            """
            INSERT INTO posicoes (usuario, latitude, longitude, atualizado_em)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(usuario) DO UPDATE SET
                latitude = excluded.latitude,
                longitude = excluded.longitude,
                atualizado_em = excluded.atualizado_em
            """,
            (p.usuario, p.latitude, p.longitude, agora),
        )
    return {"status": "ok"}


@app.get("/posicao/{usuario}")
def ver_posicao(usuario: str):
    with conectar() as con:
        cursor = con.execute(
            "SELECT usuario, latitude, longitude, atualizado_em "
            "FROM posicoes WHERE usuario = ?",
            (usuario,),
        )
        linha = cursor.fetchone()
    if linha is None:
        raise HTTPException(status_code=404, detail="Usuário sem posição")
    return {
        "usuario": linha[0],
        "latitude": linha[1],
        "longitude": linha[2],
        "atualizado_em": linha[3],
    }
@app.get("/")
def pagina_mapa():
    return FileResponse(Path(__file__).parent / "index.html")