# Football Stats API ⚽

This is a simple football statistics API project built using FastAPI.
The project stores football player data such as goals, assists, club, and country.
It also includes a player comparison feature to compare two players and find who is leading in goals and assists.

## Features

- View all players
- Get individual player details
- Compare player stats
- Find goal leader
- Find assist leader
- JSON API responses

## Technologies Used

- Python
- FastAPI

## Run the Project

```bash
uvicorn main:app --reload --port 9001
```

## API Routes

- `/players`
- `/players/{player_id}`
- `/compare/{player1_id}/{player2_id}`

## About

I created this project to practice backend API development using Python and FastAPI while building something related to football.
