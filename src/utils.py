from typing import Union
import math
        
def decorator_quantity(func):
    def inner(client,symbol):
        Account = client.account()
        for coin in Account['balances']:
            if coin['asset'] != symbol:
                continue
            return func(client,symbol,coin = coin)
    return inner

def round_stepsize(value: Union[int,float], step_size: Union[int,float]) -> float:
    """
    * Round value to step_size for Trade Rules.
    """
    precision: int = int(round(-math.log(step_size, 10), 0))
    return float(round(value, precision))