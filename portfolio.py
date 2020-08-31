from market import Market
from strategy import Strategy


class Portfolio(object):
    def __init__(
            self,
            market_status: Market,
            portfolio_strategy: Strategy
    ):
        self.position = set()
        self.average_returns = {
            'returns': [],
            'dates': []
        }

        self.portfolio_strategy = portfolio_strategy
        self.market_status = market_status

    def state_transition_function(
            self,
            trade_day: str
    ):
        pass
