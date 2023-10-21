import pandas as pd

df = pd.read_csv("C:\\Users\\kumar\\Downloads\\task\\task\\task1\\tradelog.csv")

total_trades = len(df)
df['Profit/Loss'] = df['Exit Price'] - df['Entry Price']

profitable_trades = len(df[df['Profit/Loss'] > 0])
loss_making_trades = len(df[df['Profit/Loss'] < 0])
win_rate = profitable_trades / total_trades
average_profit_per_trade= df[df['Profit/Loss']>0]['Profit/Loss'].mean()
average_loss_per_trade = df[df['Profit/Loss'] < 0]['Profit/Loss'].mean()
initial_portfolio_value = 6500
risk_free_rate = 0.05
risk_reward_ratio = abs(average_profit_per_trade / average_loss_per_trade) if average_loss_per_trade != 0 else 0


loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit_per_trade) - (loss_rate * average_loss_per_trade)


average_ror_per_trade = ((expectancy / 100) - risk_free_rate) / df['Profit/Loss'].std()


rate_of_return = (average_profit_per_trade - average_loss_per_trade) / 100
standard_deviation = df['Profit/Loss'].std()
sharpe_ratio = (rate_of_return - risk_free_rate) / standard_deviation if standard_deviation != 0 else 0


cumulative_profit = df['Profit/Loss'].cumsum()
max_drawdown = cumulative_profit - cumulative_profit.cummax()
max_drawdown_percentage = (max_drawdown / cumulative_profit.cummax()).max()


beginning_value = 6500
ending_value = beginning_value + df['Profit/Loss'].sum()
no_of_periods = len(df)
cagr = (ending_value / beginning_value) ** (1 / no_of_periods) - 1


calmar_ratio = cagr / max_drawdown_percentage if max_drawdown_percentage != 0 else 0


print(f"1. Total Trades: {total_trades}")
print(f"2. Profitable Trades: {profitable_trades}")
print(f"3. Loss Trades:{loss_making_trades}")
print(f"4. Win Ratio:{win_rate}")
print(f"5. Average Profit per trade: {average_profit_per_trade}")
print(f"6. Average Loss per trade: {average_loss_per_trade}")
print(f"7. Risk Reward ratio: {risk_reward_ratio}")
print(f"8. Expectancy: {expectancy}")
print(f"9. Average ROR per trade: {average_ror_per_trade}")
print(f"10. Sharpe Ratio: {sharpe_ratio}")
print(f"11. Max Drawdown: {max_drawdown.max()}")
print(f"12. Max Drawdown Percentage: {max_drawdown_percentage}")
print(f"13. CAGR: {cagr}")
print(f"14. Calmar Ratio: {calmar_ratio}")



#output
# 1. Total Trades: 249
# 2. Profitable Trades: 153
# 3. Loss Trades:96
# 4. Win Ratio:0.6144578313253012
# 5. Average Profit per trade: 76.09542483660131
# 6. Average Loss per trade: -105.54375
# 7. Risk Reward ratio: 0.720984661210174
# 8. Expectancy: 87.44899598393575
# 9. Average ROR per trade: 0.007292289537644512
# 10. Sharpe Ratio: 0.015623040538299339
# 11. Max Drawdown: 0.0
# 12. Max Drawdown Percentage: 0.0
# 13. CAGR: 0.0008394626758629897
# 14. Calmar Ratio: 0