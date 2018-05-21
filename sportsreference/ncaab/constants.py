PARSING_SCHEME = {
    'name': 'a',
    'games_played': 'td[data-stat="g"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'win_percentage': 'td[data-stat="win_loss_pct"]:first',
    'simple_rating_system': 'td[data-stat="srs"]:first',
    'strength_of_schedule': 'td[data-stat="sos"]:first',
    'conference_wins': 'td[data-stat="wins_conf"]:first',
    'conference_losses': 'td[data-stat="losses_conf"]:first',
    'home_wins': 'td[data-stat="wins_home"]:first',
    'home_losses': 'td[data-stat="losses_home"]:first',
    'away_wins': 'td[data-stat="wins_visitor"]:first',
    'away_losses': 'td[data-stat="losses_visitor"]:first',
    'points': 'td[data-stat="pts"]:first',
    'opp_points': 'td[data-stat="opp_pts"]:first',
    'minutes_played': 'td[data-stat="mp"]:first',
    'field_goals': 'td[data-stat="fg"]:first',
    'field_goal_attempts': 'td[data-stat="fga"]:first',
    'field_goal_percentage': 'td[data-stat="fg_pct"]:first',
    'three_point_field_goals': 'td[data-stat="fg3"]:first',
    'three_point_field_goal_attempts': 'td[data-stat="fg3a"]:first',
    'three_point_field_goal_percentage': 'td[data-stat="fg3_pct"]:first',
    'two_point_field_goals': 'td[data-stat="fg2"]:first',
    'two_point_field_goal_attempts': 'td[data-stat="fg2a"]:first',
    'two_point_field_goal_percentage': 'td[data-stat="fg2_pct"]:first',
    'free_throws': 'td[data-stat="ft"]:first',
    'free_throw_attempts': 'td[data-stat="fta"]:first',
    'free_throw_percentage': 'td[data-stat="ft_pct"]:first',
    'offensive_rebounds': 'td[data-stat="orb"]:first',
    'defensive_rebounds': 'td[data-stat="drb"]:first',
    'total_rebounds': 'td[data-stat="trb"]:first',
    'assists': 'td[data-stat="ast"]:first',
    'steals': 'td[data-stat="stl"]:first',
    'blocks': 'td[data-stat="blk"]:first',
    'turnovers': 'td[data-stat="tov"]:first',
    'personal_fouls': 'td[data-stat="pf"]:first',
    'points': 'td[data-stat="pts"]:first',
    'opp_minutes_played': 'td[data-stat="opp_mp"]:first',
    'opp_field_goals': 'td[data-stat="opp_fg"]:first',
    'opp_field_goal_attempts': 'td[data-stat="opp_fga"]:first',
    'opp_field_goal_percentage': 'td[data-stat="opp_fg_pct"]:first',
    'opp_three_point_field_goals': 'td[data-stat="opp_fg3"]:first',
    'opp_three_point_field_goal_attempts': 'td[data-stat="opp_fg3a"]:first',
    'opp_three_point_field_goal_percentage':
    'td[data-stat="opp_fg3_pct"]:first',
    'opp_two_point_field_goals': 'td[data-stat="opp_fg2"]:first',
    'opp_two_point_field_goal_attempts': 'td[data-stat="opp_fg2a"]:first',
    'opp_two_point_field_goal_percentage': 'td[data-stat="opp_fg2_pct"]:first',
    'opp_free_throws': 'td[data-stat="opp_ft"]:first',
    'opp_free_throw_attempts': 'td[data-stat="opp_fta"]:first',
    'opp_free_throw_percentage': 'td[data-stat="opp_ft_pct"]:first',
    'opp_offensive_rebounds': 'td[data-stat="opp_orb"]:first',
    'opp_defensive_rebounds': 'td[data-stat="opp_drb"]:first',
    'opp_total_rebounds': 'td[data-stat="opp_trb"]:first',
    'opp_assists': 'td[data-stat="opp_ast"]:first',
    'opp_steals': 'td[data-stat="opp_stl"]:first',
    'opp_blocks': 'td[data-stat="opp_blk"]:first',
    'opp_turnovers': 'td[data-stat="opp_tov"]:first',
    'opp_personal_fouls': 'td[data-stat="opp_pf"]:first',
    'opp_points': 'td[data-stat="opp_pts"]:first',
    'pace': 'td[data-stat="pace"]:first',
    'offensive_rating': 'td[data-stat="off_rtg"]:first',
    'free_throw_attempt_rate': 'td[data-stat="fta_per_fga_pct"]:first',
    'three_point_attempt_rate': 'td[data-stat="fg3a_per_fga_pct"]:first',
    'true_shooting_percentage': 'td[data-stat="ts_pct"]:first',
    'total_rebound_percentage': 'td[data-stat="trb_pct"]:first',
    'assist_percentage': 'td[data-stat="ast_pct"]:first',
    'steal_percentage': 'td[data-stat="stl_pct"]:first',
    'block_percentage': 'td[data-stat="blk_pct"]:first',
    'effective_field_goal_percentage': 'td[data-stat="efg_pct"]:first',
    'turnover_percentage': 'td[data-stat="tov_pct"]:first',
    'offensive_rebound_percentage': 'td[data-stat="orb_pct"]:first',
    'free_throws_per_field_goal_attempt': 'td[data-stat="ft_rate"]:first',
    'opp_offensive_rating': 'td[data-stat="def_rtg"]:first',
    'opp_free_throw_attempt_rate': 'td[data-stat="opp_fta_per_fga_pct"]:first',
    'opp_three_point_attempt_rate':
    'td[data-stat="opp_fg3a_per_fga_pct"]:first',
    'opp_true_shooting_percentage': 'td[data-stat="opp_ts_pct"]:first',
    'opp_total_rebound_percentage': 'td[data-stat="opp_trb_pct"]:first',
    'opp_assist_percentage': 'td[data-stat="opp_ast_pct"]:first',
    'opp_steal_percentage': 'td[data-stat="opp_stl_pct"]:first',
    'opp_block_percentage': 'td[data-stat="opp_blk_pct"]:first',
    'opp_effective_field_goal_percentage': 'td[data-stat="opp_efg_pct"]:first',
    'opp_turnover_percentage': 'td[data-stat="opp_tov_pct"]:first',
    'opp_offensive_rebound_percentage': 'td[data-stat="opp_orb_pct"]:first',
    'opp_free_throws_per_field_goal_attempt':
    'td[data-stat="opp_ft_rate"]:first'
}

BASIC_STATS_URL = ('http://www.sports-reference.com/cbb/seasons/'
                   '%s-school-stats.html')
BASIC_OPPONENT_STATS_URL = ('http://www.sports-reference.com/cbb/seasons/'
                            '%s-opponent-stats.html')
ADVANCED_STATS_URL = ('http://www.sports-reference.com/cbb/seasons/'
                      '%s-advanced-school-stats.html')
ADVANCED_OPPONENT_STATS_URL = ('http://www.sports-reference.com/cbb/seasons/'
                               '%s-advanced-opponent-stats.html')
