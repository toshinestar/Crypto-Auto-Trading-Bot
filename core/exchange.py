from ccxt import Exchange, OrderNotFound


class CryptoExchange:

    def __init__(self, exchange: Exchange):
        self.exchange = exchange
        self.exchange.load_markets()

    @property
    def free_balance(self):
        balance = self.exchange.fetch_free_balance()
        # surprisingly there are balances with 0, so we need to filter these out
        return {k: v for k, v in balance.items() if v > 0}

    def fetch_open_orders(self, symbol: str = None):
        return self.exchange.fetch_open_orders(symbol=symbol)

    def fetch_order(self, order_id: int):
        return self.exchange.fetch_order(order_id)

    def cancel_order(self, order_id: int):
        try:
            self.exchange.cancel_order(order_id)
        except OrderNotFound:
            # treat as success
            pass

    def create_sell_order(self, symbol: str, amount: float, price: float):
        return self.exchange.create_order(symbol=symbol, type="limit", side="sell", amount=amount, price=price)

    def create_buy_order(self, symbol: str, amount: float, price: float):
        return self.exchange.create_order(symbol=symbol, type="limit", side="buy", amount=amount, price=price)
