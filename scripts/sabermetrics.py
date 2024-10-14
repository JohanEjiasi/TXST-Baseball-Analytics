import pandas as pd
import requests

# Metrics Functions
def calculate_wrc_manual(plate_appearances, woba, season):
    # TODO: Implement wRC calculation
    pass

def calculate_wraa_manual(plate_appearances, woba, season):
    # TODO: Implement wRAA calculation
    pass

def calculate_woba_manual(plate_appearances, walks, hits_by_pitch, singles, doubles, triples, homeruns, season):
    # TODO: Implement wOBA calculation
    pass

def add_batting_metrics(df):
    # TODO: Implement logic to add additional batting metrics
    pass

# Pitching Functions
def calculate_fip_manual(homeruns, walks, hit_batters, strikeouts, innings_pitched, season):
    # TODO: Implement FIP calculation
    pass

def add_pitching_metrics(df):
    # TODO: Implement logic to add additional pitching metrics
    pass

# Lookup Functions
def lookup_player(player_name, school):
    # TODO: Implement player lookup
    pass

def lookup_player_reverse(player_id):
    # TODO: Implement reverse player lookup
    pass

def lookup_seasons_played(stats_player_seq):
    # TODO: Implement lookup for seasons played
    pass

def lookup_school(school_name):
    # TODO: Implement school lookup
    pass

def lookup_school_reverse(school_id):
    # TODO: Implement reverse school lookup
    pass

def lookup_season_id(season):
    # TODO: Implement season ID lookup
    pass

def lookup_season_ids(season):
    # TODO: Implement lookup for year stat category IDs
    pass

def lookup_season_reverse(season_id):
    # TODO: Implement reverse season lookup
    pass

# Example function to demonstrate getting top offensive players
def display_top_offensive_players(df):
    top_offensive_players = df.nlargest(3, 'OPS')[['player_name', 'OPS']]
    print("Top 3 Offensive Players by OPS:")
    print(top_offensive_players.to_string(index=False))

# Main execution flow (if needed)
if __name__ == "__main__":
    # Example DataFrame for testing
    data = {
        'player_name': ['Lugo, Aaron', 'Farber, Ryne', 'Ramirez, August', 'Doe, John'],
        'OPS': [1.008, 0.934, 0.900, 0.800]
    }
    df = pd.DataFrame(data)

    # Display top offensive players
    display_top_offensive_players(df)
