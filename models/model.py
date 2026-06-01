from pydantic import BaseModel, Field

class Player(BaseModel):
    name: str = Field(..., min_length=2, description="Player nte full name")
    club: str = Field(..., min_length=2, description="Club name")
    country: str = Field(..., min_length=2, description="Country name")
    goals: int = Field(0, ge=0, description="Goals negative aakan padilla")
    assists: int = Field(0, ge=0, description="Assists negative aakan padilla")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Lionel Messi",
                    "club": "Inter Miami",
                    "country": "Argentina",
                    "goals": 800,
                    "assists": 350
                }
            ]
        }
    }