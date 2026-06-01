from fastapi import APIRouter, HTTPException
from models.model import Player
from database.mdbconnection import players_collection

router = APIRouter()

# GET ALL PLAYERS
@router.get("/players")
def get_players():
    try:
        players = list(players_collection.find({}, {"_id": 0}))
        return players
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ADD NEW PLAYER
@router.post("/players")
def add_player(player: Player):
    try:
        # Duplicate check using name + club
        existing_player = players_collection.find_one({
            "name": player.name,
            "club": player.club
        })
        if existing_player:
            raise HTTPException(
                status_code=400,
                detail="Player already exists in this club"
            )
        players_collection.insert_one(player.dict())
        return {
            "message": "Player added successfully"
        }
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET SINGLE PLAYER
@router.get("/players/{player_name}")
def get_player(player_name: str):
    try:
        player = players_collection.find_one(
            {"name": player_name},
            {"_id": 0}
        )
        if not player:
            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )
        return player
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# UPDATE PLAYER
@router.put("/players/{player_name}")
def update_player(player_name: str, updated_player: Player):
    try:
        result = players_collection.update_one(
            {"name": player_name},
            {"$set": updated_player.dict()}
        )
        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )
        return {
            "message": "Player updated successfully"
        }
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE PLAYER
@router.delete("/players/{player_name}")
def delete_player(player_name: str):
    try:
        result = players_collection.delete_one(
            {"name": player_name}
        )
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Player not found"
            )
        return {
            "message": "Player deleted successfully"
        }
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))