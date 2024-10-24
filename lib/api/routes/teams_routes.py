from fastapi import APIRouter, HTTPException
from ..models.teams import Teams


# Route Config
teams_router = APIRouter(prefix='/teams', tags=["teams"])


@teams_router.get('/')
async def get_teams():
    teams = list(Teams.select())
    return { "teams": teams }


@teams_router.get('/${team_id}')
async def get_team_by_id(team_id):
    team = Teams.get_or_none(Teams.id == team_id)

    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return team


@teams_router.post('/')
async def create_team(team_data):
    print(team_data)

    # new_team = Teams.create(**team_data.dict)
    return {'Test': 'Team Post Route Test'}