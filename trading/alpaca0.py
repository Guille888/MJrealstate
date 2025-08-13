from alpaca.trading.client import TradingClient

# paper=True enables paper trading
trading_client = TradingClient('PK3NZYHG9SELUDIFKJJG', 'zXN5YgTS068KGwjv4PpW2k65nIRBIG43oKuGhSqr')

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)