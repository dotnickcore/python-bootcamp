"""
Lookup Results

Win/Loss of Each Team

Most Super Bowl Wins - Count how many times each team has won.

Most Super Bowl Losses - Count how many times each team has lost.

Win/Loss Ratio - For teams that have appeared multiple times.

Biggest Point Differential - Largest margin of victory in a Super Bowl.

Smallest Point Differential - Closest Super Bowl games.

Highest Scoring Game - Total points scored by both teams.

Lowest Scoring Game - Fewest total points scored by both teams.

Teams with Multiple Wins - List teams that have won more than once.

Teams That Have Never Won - List teams that have appeared but never won.

Most Common Venue - Which stadium has hosted the most Super Bowls?

Most Common City - Which city has hosted the most Super Bowls?

Most Common State - Which state has hosted the most Super Bowls?

Attendance Statistics - Highest, lowest, and average attendance.

Head to Head
"""


def main():
    superbowl_winners = build_superbowl_winners_dictionary()
    nfl_teams = build_nfl_teams_list()
    usa_states = build_usa_states_list()

def build_superbowl_winners_dictionary():
    return {
        '1967': {
            'winning_team': 'Green Bay Packers',
            'winning_score': 35,
            'losing_team': 'Kansas City Chiefs',
            'losing_score': 10,
            'venue': 'Los Angeles Memorial Coliseum',
            'city': 'Los Angeles',
            'state': 'California',
            'attendance': 61946
        },
        '1968': {
            'winning_team': 'Green Bay Packers',
            'winning_score': 33,
            'losing_team': 'Oakland Raiders',
            'losing_score': 14,
            'venue': 'Miami Orange Bowl',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 75546
        },
        '1969': {
            'winning_team': 'New York Jets',
            'winning_score': 16,
            'losing_team': 'Baltimore Colts',
            'losing_score': 7,
            'venue': 'Miami Orange Bowl',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 75389
        },
        '1970': {
            'winning_team': 'Kansas City Chiefs',
            'winning_score': 23,
            'losing_team': 'Minnesota Vikings',
            'losing_score': 7,
            'venue': 'Tulane Stadium',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 80562
        },
        '1971': {
            'winning_team': 'Baltimore Colts',
            'winning_score': 16,
            'losing_team': 'Dallas Cowboys',
            'losing_score': 13,
            'venue': 'Miami Orange Bowl',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 79204
        },
        '1972': {
            'winning_team': 'Dallas Cowboys',
            'winning_score': 24,
            'losing_team': 'Miami Dolphins',
            'losing_score': 3,
            'venue': 'Tulane Stadium',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 81023
        },
        '1973': {
            'winning_team': 'Miami Dolphins',
            'winning_score': 14,
            'losing_team': 'Washington Redskins',
            'losing_score': 7,
            'venue': 'Los Angeles Memorial Coliseum',
            'city': 'Los Angeles',
            'state': 'California',
            'attendance': 90182
        },
        '1974': {
            'winning_team': 'Miami Dolphins',
            'winning_score': 24,
            'losing_team': 'Minnesota Vikings',
            'losing_score': 7,
            'venue': 'Rice Stadium',
            'city': 'Houston',
            'state': 'Texas',
            'attendance': 71882
        },
        '1975': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 16,
            'losing_team': 'Minnesota Vikings',
            'losing_score': 6,
            'venue': 'Tulane Stadium',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 80997
        },
        '1976': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 21,
            'losing_team': 'Dallas Cowboys',
            'losing_score': 17,
            'venue': 'Miami Orange Bowl',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 80187
        },
        '1977': {
            'winning_team': 'Oakland Raiders',
            'winning_score': 32,
            'losing_team': 'Minnesota Vikings',
            'losing_score': 14,
            'venue': 'Rose Bowl',
            'city': 'Pasadena',
            'state': 'California',
            'attendance': 103438
        },
        '1978': {
            'winning_team': 'Dallas Cowboys',
            'winning_score': 27,
            'losing_team': 'Denver Broncos',
            'losing_score': 10,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 76400
        },
        '1979': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 35,
            'losing_team': 'Dallas Cowboys',
            'losing_score': 31,
            'venue': 'Miami Orange Bowl',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 79484
        },
        '1980': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 31,
            'losing_team': 'Los Angeles Rams',
            'losing_score': 19,
            'venue': 'Rose Bowl',
            'city': 'Pasadena',
            'state': 'California',
            'attendance': 103985
        },
        '1981': {
            'winning_team': 'Oakland Raiders',
            'winning_score': 27,
            'losing_team': 'Philadelphia Eagles',
            'losing_score': 10,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 76135
        },
        '1982': {
            'winning_team': 'San Francisco 49ers',
            'winning_score': 26,
            'losing_team': 'Cincinnati Bengals',
            'losing_score': 21,
            'venue': 'Pontiac Silverdome',
            'city': 'Pontiac',
            'state': 'Michigan',
            'attendance': 81270
        },
        '1983': {
            'winning_team': 'Washington Redskins',
            'winning_score': 27,
            'losing_team': 'Miami Dolphins',
            'losing_score': 17,
            'venue': 'Rose Bowl',
            'city': 'Pasadena',
            'state': 'California',
            'attendance': 103667
        },
        '1984': {
            'winning_team': 'Los Angeles Raiders',
            'winning_score': 38,
            'losing_team': 'Washington Redskins',
            'losing_score': 9,
            'venue': 'Tampa Stadium',
            'city': 'Tampa',
            'state': 'Florida',
            'attendance': 72920
        },
        '1985': {
            'winning_team': 'San Francisco 49ers',
            'winning_score': 38,
            'losing_team': 'Miami Dolphins',
            'losing_score': 16,
            'venue': 'Stanford Stadium',
            'city': 'Stanford',
            'state': 'California',
            'attendance': 84059
        },
        '1986': {
            'winning_team': 'Chicago Bears',
            'winning_score': 46,
            'losing_team': 'New England Patriots',
            'losing_score': 10,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 73818
        },
        '1987': {
            'winning_team': 'New York Giants',
            'winning_score': 39,
            'losing_team': 'Denver Broncos',
            'losing_score': 20,
            'venue': 'Rose Bowl',
            'city': 'Pasadena',
            'state': 'California',
            'attendance': 101063
        },
        '1988': {
            'winning_team': 'Washington Redskins',
            'winning_score': 42,
            'losing_team': 'Denver Broncos',
            'losing_score': 10,
            'venue': 'San Diego-Jack Murphy Stadium',
            'city': 'San Diego',
            'state': 'California',
            'attendance': 73302
        },
        '1989': {
            'winning_team': 'San Francisco 49ers',
            'winning_score': 20,
            'losing_team': 'Cincinnati Bengals',
            'losing_score': 16,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 75129
        },
        '1990': {
            'winning_team': 'San Francisco 49ers',
            'winning_score': 55,
            'losing_team': 'Denver Broncos',
            'losing_score': 10,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 72919
        },
        '1991': {
            'winning_team': 'New York Giants',
            'winning_score': 20,
            'losing_team': 'Buffalo Bills',
            'losing_score': 19,
            'venue': 'Tampa Stadium',
            'city': 'Tampa',
            'state': 'Florida',
            'attendance': 73813
        },
        '1992': {
            'winning_team': 'Washington Redskins',
            'winning_score': 37,
            'losing_team': 'Buffalo Bills',
            'losing_score': 24,
            'venue': 'Metrodome',
            'city': 'Minneapolis',
            'state': 'Minnesota',
            'attendance': 63130
        },
        '1993': {
            'winning_team': 'Dallas Cowboys',
            'winning_score': 52,
            'losing_team': 'Buffalo Bills',
            'losing_score': 17,
            'venue': 'Rose Bowl',
            'city': 'Pasadena',
            'state': 'California',
            'attendance': 98374
        },
        '1994': {
            'winning_team': 'Dallas Cowboys',
            'winning_score': 30,
            'losing_team': 'Buffalo Bills',
            'losing_score': 13,
            'venue': 'Georgia Dome',
            'city': 'Atlanta',
            'state': 'Georgia',
            'attendance': 72817
        },
        '1995': {
            'winning_team': 'San Francisco 49ers',
            'winning_score': 49,
            'losing_team': 'San Diego Chargers',
            'losing_score': 26,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 74107
        },
        '1996': {
            'winning_team': 'Dallas Cowboys',
            'winning_score': 27,
            'losing_team': 'Pittsburgh Steelers',
            'losing_score': 17,
            'venue': 'Sun Devil Stadium',
            'city': 'Tempe',
            'state': 'Arizona',
            'attendance': 76347
        },
        '1997': {
            'winning_team': 'Green Bay Packers',
            'winning_score': 35,
            'losing_team': 'New England Patriots',
            'losing_score': 21,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 72301
        },
        '1998': {
            'winning_team': 'Denver Broncos',
            'winning_score': 31,
            'losing_team': 'Green Bay Packers',
            'losing_score': 24,
            'venue': 'San Diego-Jack Murphy Stadium',
            'city': 'San Diego',
            'state': 'California',
            'attendance': 68912
        },
        '1999': {
            'winning_team': 'Denver Broncos',
            'winning_score': 34,
            'losing_team': 'Atlanta Falcons',
            'losing_score': 19,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 74803
        },
        '2000': {
            'winning_team': 'St. Louis Rams',
            'winning_score': 23,
            'losing_team': 'Tennessee Titans',
            'losing_score': 16,
            'venue': 'Georgia Dome',
            'city': 'Atlanta',
            'state': 'Georgia',
            'attendance': 72625
        },
        '2001': {
            'winning_team': 'Baltimore Ravens',
            'winning_score': 34,
            'losing_team': 'New York Giants',
            'losing_score': 7,
            'venue': 'Raymond James Stadium',
            'city': 'Tampa',
            'state': 'Florida',
            'attendance': 71921
        },
        '2002': {
            'winning_team': 'New England Patriots',
            'winning_score': 20,
            'losing_team': 'St. Louis Rams',
            'losing_score': 17,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 72922
        },
        '2003': {
            'winning_team': 'Tampa Bay Buccaneers',
            'winning_score': 48,
            'losing_team': 'Oakland Raiders',
            'losing_score': 21,
            'venue': 'San Diego-Jack Murphy Stadium',
            'city': 'San Diego',
            'state': 'California',
            'attendance': 67603
        },
        '2004': {
            'winning_team': 'New England Patriots',
            'winning_score': 32,
            'losing_team': 'Carolina Panthers',
            'losing_score': 29,
            'venue': 'Houston Stadium',
            'city': 'Houston',
            'state': 'Texas',
            'attendance': 71525
        },
        '2005': {
            'winning_team': 'New England Patriots',
            'winning_score': 24,
            'losing_team': 'Philadelphia Eagles',
            'losing_score': 21,
            'venue': 'Jacksonville Municipal Stadium',
            'city': 'Jacksonville,',
            'state': 'Florida',
            'attendance': 78125
        },
        '2006': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 21,
            'losing_team': 'Seattle Seahawks',
            'losing_score': 10,
            'venue': 'Ford Field',
            'city': 'Detroit',
            'state': 'Michigan',
            'attendance': 68206
        },
        '2007': {
            'winning_team': 'Indianapolis Colts',
            'winning_score': 29,
            'losing_team': 'Chicago Bears',
            'losing_score': 17,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 74512
        },
        '2008': {
            'winning_team': 'New York Giants',
            'winning_score': 17,
            'losing_team': 'New England Patriots',
            'losing_score': 14,
            'venue': 'Cardinals Stadium',
            'city': 'Glendale',
            'state': 'Arizona',
            'attendance': 70774
        },
        '2009': {
            'winning_team': 'Pittsburgh Steelers',
            'winning_score': 27,
            'losing_team': 'Arizona Cardinals',
            'losing_score': 23,
            'venue': 'Raymond James Stadium',
            'city': 'Tampa',
            'state': 'Florida',
            'attendance': 70774
        },
        '2010': {
            'winning_team': 'New Orleans Saints',
            'winning_score': 31,
            'losing_team': 'Indianapolis Colts',
            'losing_score': 17,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 74059
        },
        '2011': {
            'winning_team': 'Green Bay Packers',
            'winning_score': 31,
            'losing_team': 'Pittsburgh Steelers',
            'losing_score': 25,
            'venue': 'Cowboys Stadium',
            'city': 'Arlington',
            'state': ' Texas',
            'attendance': 103219
        },
        '2012': {
            'winning_team': 'New York Giants',
            'winning_score': 21,
            'losing_team': 'New England Patriots',
            'losing_score': 17,
            'venue': 'Lucas Oil Stadium',
            'city': 'Indianapolis',
            'state': 'Indiana',
            'attendance': 68658
        },
        '2013': {
            'winning_team': 'Baltimore Ravens',
            'winning_score': 34,
            'losing_team': 'San Francisco 49ers',
            'losing_score': 31,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 71024
        },
        '2014': {
            'winning_team': 'Seattle Seahawks',
            'winning_score': 43,
            'losing_team': 'Denver Broncos',
            'losing_score': 10,
            'venue': 'New York/New Jersey Stadium',
            'city': 'East Rutherford',
            'state': 'New Jersey',
            'attendance': 82529
        },
        '2015': {
            'winning_team': 'New England Patriots',
            'winning_score': 28,
            'losing_team': 'Seattle Seahawks',
            'losing_score': 24,
            'venue': 'Cardinals Stadium',
            'city': 'Glendale',
            'state': 'Arizona',
            'attendance': 70288
        },
        '2016': {
            'winning_team': 'Denver Broncos',
            'winning_score': 24,
            'losing_team': 'Carolina Panthers',
            'losing_score': 10,
            'venue': "Levi's Stadium",
            'city': 'Santa Clara',
            'state': 'California',
            'attendance': 71088
        },
        '2017': {
            'winning_team': 'New England Patriots',
            'winning_score': 34,
            'losing_team': 'Atlanta Falcons',
            'losing_score': 28,
            'venue': 'Houston Stadium',
            'city': 'Houston',
            'state': 'Texas',
            'attendance': 70807
        },
        '2018': {
            'winning_team': 'Philadelphia Eagles',
            'winning_score': 41,
            'losing_team': 'New England Patriots',
            'losing_score': 33,
            'venue': 'U.S. Bank Stadium',
            'city': 'Minneapolis',
            'state': 'Minnesota',
            'attendance': 67612
        },
        '2019': {
            'winning_team': 'New England Patriots',
            'winning_score': 13,
            'losing_team': 'Kansas City Chiefa',
            'losing_score': 3,
            'venue': 'Mercedes-Benz Stadium',
            'city': 'Atlanta',
            'state': 'Georgia',
            'attendance': 70081
        },
        '2020': {
            'winning_team': 'Kansas City Chiefs',
            'winning_score': 31,
            'losing_team': 'San Francisco 49ers',
            'losing_score': 20,
            'venue': 'Joe Robbie Stadium',
            'city': 'Miami',
            'state': 'Florida',
            'attendance': 62417
        },
        '2021': {
            'winning_team': 'Tampa Bay Buccaneers',
            'winning_score': 31,
            'losing_team': 'Kansas City Chiefs',
            'losing_score': 9,
            'venue': 'Raymond James Stadium',
            'city': 'Tampa',
            'state': 'Florida',
            'attendance': 24835
        },
        '2022': {
            'winning_team': 'Los Angeles Rams',
            'winning_score': 23,
            'losing_team': 'Cincinnati Bengals',
            'losing_score': 20,
            'venue': 'SoFi Stadium',
            'city': 'Inglewood',
            'state': 'California',
            'attendance': 70048
        },
        '2023': {
            'winning_team': 'Kansas City Chiefs',
            'winning_score': 38,
            'losing_team': 'Philadelphia Eagles',
            'losing_score': 35,
            'venue': 'Cardinals Stadium',
            'city': 'Glendale',
            'state': 'Arizona',
            'attendance': 67827
        },
        '2024': {
            'winning_team': 'Kansas City Chiefs',
            'winning_score': 25,
            'losing_team': 'San Francisco 49ers',
            'losing_score': 22,
            'venue': 'Allegiant Stadium',
            'city': 'Paradise',
            'state': 'Nevada',
            'attendance': 61629
        },
        '2025': {
            'winning_team': 'Philadelphia Eagles',
            'winning_score': 40,
            'losing_team': 'Kansas City Chiefs',
            'losing_score': 22,
            'venue': 'Louisiana Superdome',
            'city': 'New Orleans',
            'state': 'Louisiana',
            'attendance': 65719
        }
    }

def build_nfl_teams_list():
    return [
        'Buffalo Bills',
        'Miami Dolphins',
        'New England Patriots',
        'New York Jets',
        'Baltimore Ravens',
        'Cincinnati Bengals',
        'Cleveland Browns',
        'Pittsburgh Steelers',
        'Houston Texans',
        'Indianapolis Colts',
        'Jacksonville Jaguars',
        'Tennessee Titans',
        'Denver Broncos',
        'Kansas City Chiefs',
        'Las Vegas Raiders',
        'Los Angeles Chargers',
        'Dallas Cowboys',
        'New York Giants',
        'Philadelphia Eagles',
        'Washington Commanders',
        'Chicago Bears',
        'Detroit Lions',
        'Green Bay Packers',
        'Minnesota Vikings',
        'Atlanta Falcons',
        'Carolina Panthers',
        'New Orleans Saints',
        'Tampa Bay Buccaneers',
        'Arizona Cardinals',
        'Los Angeles Rams',
        'San Francisco 49ers',
        'Seattle Seahawks',
        'Baltimore Colts',
        'Oakland Raiders',
        'Los Angeles Raiders',
        'Washington Redskins',
        'San Diego Chargers',
        'St Louis Rams'
    ]

def get_team_with_most_wins(superbowl_data):
    winners = [game['winning_team'] for game in superbowl_data.values()]
    return max(set(winners), key=winners.count)

main()