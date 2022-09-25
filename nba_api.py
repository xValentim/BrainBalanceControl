import pandas as pd
from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'A API está no ar'


@app.route('/getstats')
def getStats():
    season_id = '2020-21'
    per_mode = 'Totals'
    player_infor_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + per_mode + '&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season_id + '&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    # Requisição para coletar os dados
    response = requests.get(url=player_infor_url, headers=headers).json()
    player_info = response['resultSets'][0]['rowSet']
    columns_list = [
        'season_id',  # this is key, need this to join and sort by seasons
        'player_id',
        'player_name',
        'team_id',
        'team_abbreviation',
        'age',
        'gp',
        'w',
        'l',
        'w_pct',
        'min',
        'fgm',
        'fga',
        'fg_pct',
        'fg3m',
        'fg3a',
        'fg3_pct',
        'ftm',
        'fta',
        'ft_pct',
        'oreb',
        'dreb',
        'reb',
        'ast',
        'tov',
        'stl',
        'blk',
        'blka',
        'pf',
        'pfd',
        'pts',
        'plus_minus',
        'nba_fantasy_pts',
        'dd2',
        'td3',
        'gp_rank',
        'w_rank',
        'l_rank',
        'w_pct_rank',
        'min_rank',
        'fgm_rank',
        'fga_rank',
        'fg_pct_rank',
        'fg3m_rank',
        'fg3a_rank',
        'fg3_pct_rank',
        'ftm_rank',
        'fta_rank',
        'ft_pct_rank',
        'oreb_rank',
        'dreb_rank',
        'reb_rank',
        'ast_rank',
        'tov_rank',
        'stl_rank',
        'blk_rank',
        'blka_rank',
        'pf_rank',
        'pfd_rank',
        'pts_rank',
        'plus_minus_rank',
        'nba_fantasy_pts_rank',
        'dd2_rank',
        'td3_rank',
        'cfid',
        'cfparams'
        'und0',
        'und1',
        'und2',
    ]
    df = pd.DataFrame(player_info, columns=columns_list)
    output = df.set_index('player_name').T.to_dict('list')
    return jsonify(output)

app.run(host='0.0.0.0')
