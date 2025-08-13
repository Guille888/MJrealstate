from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest

# paper=True enables paper trading
trading_client = TradingClient('PK3NZYHG9SELUDIFKJJG', 'zXN5YgTS068KGwjv4PpW2k65nIRBIG43oKuGhSqr')
market_order_data = MarketOrderRequest(
    symbol='TSLA',  # Cambiado a 'symbol_or_asset_id' si es necesario
    qty=10,                     # Cantidad de acciones a comprar
    side='buy',                 # Tipo de operación
    order_type='limit',         # Cambiado a 'order_type'
    limit_price=336,            # Precio límite establecido a $336
    time_in_force='gtc'         # Orden válida hasta que se cancele
)

market_order = trading_client.submit_order(market_order_data)
print(market_order)