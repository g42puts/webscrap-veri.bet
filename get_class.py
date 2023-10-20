from dataclasses import dataclass
from save_json import save_json
from itens import get_itens, get_item, get_value_list


# definição da dataclass Item
@dataclass
class Item:
    sport_league: str = ''     # the league, can be NFL, NCAAF, MLB ...
    event_date_utc: str = ''   # date of the event, in UTC, ISO format
    team1: str = ''            # team 1 name
    team2: str = ''            # team 2 name
    pitcher: str = ''          # optional, pitcher for baseball
    period: str = ''           # full time, 1st half, 1st quarter and so on
    line_type: str = ''        # whatever site reports as line type, e.g. moneyline, spread, over/under
    price: str = ''            # price site reports, e.g. '-133' or '+105'
    side: str = ''             # side of the bet for over/under, e.g. 'over', 'under'
    team: str = ''             # team name, for over/under bets this will be either team name or total
    spread: float = 0.0        # for handicap and over/under bets, e.g. -1.5, +2.5


# função responsavel por tratar os dados e salvar
def get_class(content) -> None:

    itens = get_itens(content=content)
    item = get_item(itens=itens)
    value_list = get_value_list(itens=itens)
    
    conteudos = []

    i = 1
    line_types = ["moneyline", "spread", "over/under"]
    for x in value_list:
        _side = None
        _team = None
        _line_type = None

        if i < 5:
            if i % 2 == 0:
                _side = item[4]
                _team = item[4]
                
            _line_type = line_types[0] if i < 3 else line_types[1]

        if i % 2 != 0 and i < 5:        
            _side, _team = item[8], item[8]

        if i > 4:
            _line_type = line_types[2]
            _team = "total"    
            _side = "over" if i == 5 else "under"

        class_item = Item(
            sport_league=item[12],
            event_date_utc=item[13],
            team1=item[4],
            team2=item[8],
            pitcher="",
            period=item[0],
            line_type=_line_type, # type: ignore
            price=x[0] if len(x) < 2 else x[1],
            side=_side, # type: ignore
            team=_team, # type: ignore
            spread=0 if len(x) < 2 else x[0]
        )
        i += 1
        conteudos.append(class_item)

    save_json(class_list=conteudos)