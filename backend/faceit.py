import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE = "https://open.faceit.com/data/v4"


def _client() -> httpx.Client:
    key = os.environ["FACEIT_API_KEY"]
    return httpx.Client(base_url=BASE, headers={"Authorization": f"Bearer {key}"}, timeout=30)


def get_player(nickname: str) -> dict:
    with _client() as c:
        r = c.get("/players", params={"nickname": nickname, "game": "cs2"})
        r.raise_for_status()
        return r.json()


def get_match(match_id: str) -> dict:
    with _client() as c:
        r = c.get(f"/matches/{match_id}")
        r.raise_for_status()
        return r.json()


def get_player_history(player_id: str, limit: int = 20) -> list[dict]:
    with _client() as c:
        r = c.get(f"/players/{player_id}/history", params={"game": "cs2", "limit": limit})
        r.raise_for_status()
        return r.json()["items"]


def enemy_players(match: dict, my_player_id: str) -> list[dict]:
    teams = match["teams"]
    for key in ("faction1", "faction2"):
        ids = [p["player_id"] for p in teams[key]["roster"]]
        if my_player_id in ids:
            other = "faction2" if key == "faction1" else "faction1"
            return teams[other]["roster"]
    raise ValueError("Spilleren er ikke i denne kamp")


def match_map(match: dict) -> str | None:
    picks = match.get("voting", {}).get("map", {}).get("pick", [])
    return picks[0] if picks else None
