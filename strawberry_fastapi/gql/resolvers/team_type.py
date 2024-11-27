from ..object_types.team_type import TeamType

def resolve_team_type(key: str) -> TeamType:
    mock_teams = {
        "dev": TeamType(key="dev", display_name="Development Team"),
        "qa": TeamType(key="qa", display_name="QA Team"),
        "ops": TeamType(key="ops", display_name="Operations Team"),
    }
    return mock_teams.get(key, TeamType(key="unknown", display_name="Unknown Team"))