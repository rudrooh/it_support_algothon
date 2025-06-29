import numpy as np

def getMyPosition(prcSoFar):
    (nInst, nt) = prcSoFar.shape
    # --- Final Optimized Parameters ---

    short_lookback = 10 # short lookback period where lookback is the number of days to calculate the moving average
    long_lookback = 25 # long lookback period where lookback is the number of days to calculate the moving average
    allocation_usd = 2500 # allocation in USD, this is the amount of money to allocate to each instrument
    # We need enough data for the longest lookback period
    if nt < long_lookback:
        return np.zeros(nInst, dtype=int) # if there is not enough data, return 0

    # Calculate the short-term and long-term moving averages
    short_ma = np.mean(prcSoFar[:, -short_lookback:], axis=1)
    long_ma = np.mean(prcSoFar[:, -long_lookback:], axis=1)
    positions = np.zeros(nInst, dtype=int)
    latest_prices = prcSoFar[:, -1]

    # Crossover Logic
    for i in range(nInst):
        if latest_prices[i] == 0:
            continue

        if short_ma[i] > long_ma[i]:
            # Fast MA is above Slow MA: Bullish signal, go long
            dollar_position = allocation_usd
            positions[i] = int(dollar_position / latest_prices[i])
        elif short_ma[i] < long_ma[i]:
            # Fast MA is below Slow MA: Bearish signal, go short
            dollar_position = -allocation_usd
            positions[i] = int(dollar_position / latest_prices[i])
    return positions