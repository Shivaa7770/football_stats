from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class Player(BaseModel):
    id: int
    name: str
    club: str
    country: str
    goals: int
    assists: int

players = [
    {
        "id": 1,
        "name": "Messi",
        "club": "Inter Miami",
        "country": "Argentina",
        "goals": 25,
        "assists": 18
    },

    {
        "id": 2,
        "name": "Ronaldo",
        "club": "Al Nassr",
        "country": "Portugal",
        "goals": 22,
        "assists": 7
    },

    {
        "id": 3,
        "name": "Mbappe",
        "club": "Real Madrid",
        "country": "France",
        "goals": 30,
        "assists": 10
    },

    {
        "id": 4,
        "name": "Haaland",
        "club": "Manchester City",
        "country": "Norway",
        "goals": 27,
        "assists": 6
    },

    {
        "id": 5,
        "name": "Neymar",
        "club": "Al Hilal",
        "country": "Brazil",
        "goals": 18,
        "assists": 12
    },

    {
        "id": 6,
        "name": "Vinicius Junior",
        "club": "Real Madrid",
        "country": "Brazil",
        "goals": 21,
        "assists": 11
    },

    {
        "id": 7,
        "name": "Kevin De Bruyne",
        "club": "Manchester City",
        "country": "Belgium",
        "goals": 10,
        "assists": 20
    },

    {
        "id": 8,
        "name": "Lewandowski",
        "club": "Barcelona",
        "country": "Poland",
        "goals": 24,
        "assists": 5
    },

    {
        "id": 9,
        "name": "Lamine Yamal",
        "club": "Barcelona",
        "country": "Spain",
        "goals": 14,
        "assists": 16
    }

]


@app.get("/")
def home():
    return {
        "message": "Football Stats API"
    }

@app.post("/players")
def add_player(player: Player):
    for existing_player in players:
        if existing_player["id"] == player.id:
            return {
                "error": "Player ID already exists"
            }
    players.append(player.dict())
    return {
        "message": "Player added successfully",
        "player": player
    }



@app.put("/players/{player_id}")
def update_player(player_id: int, updated_player: Player):
    for player in players:

        if player["id"] == player_id:
            player["name"] = updated_player.name
            player["club"] = updated_player.club
            player["country"] = updated_player.country
            player["goals"] = updated_player.goals
            player["assists"] = updated_player.assists
            return {
                "message": "Player updated successfully",
                "updated_player": player
            }
    return {
        "error": "Player not found"
    }

@app.get("/players")
def get_players():
    return players


@app.get("/players/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player
    return {
        "error": "Player not found"
    }

@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            players.remove(player)
            return {
                "message": "Player deleted successfully"
            }
    return {
        "error": "Player not found"
    }


@app.get("/compare/{player1_id}/{player2_id}")
def compare_players(player1_id: int, player2_id: int):
    player1 = None
    player2 = None
    for player in players:
        if player["id"] == player1_id:
            player1 = player
        if player["id"] == player2_id:
            player2 = player
    if player1 is None or player2 is None:
        return {
            "error": "Player not found"
        }

    if player1["goals"] > player2["goals"]:
        goals_leader = player1["name"]
        goals_number = player1["goals"]

    else:
        goals_leader = player2["name"]
        goals_number = player2["goals"]


    if player1["assists"] > player2["assists"]:
        assists_leader = player1["name"]
        assists_number = player1["assists"]

    else:
        assists_leader = player2["name"]
        assists_number = player2["assists"]


    return {

        "player_1_full_stats": player1,
        "player_2_full_stats": player2,
        "goals_leader": goals_leader,
        "goals": goals_number,
        "assists_leader": assists_leader,
        "assists": assists_number
    }

    