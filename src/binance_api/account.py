from binance.spot import Spot

class BinanceAccount(Spot):
    
    
    
    
    
    def decorator_quantity(self,func):
        def inner(self,symbol):
            Account = self.client.account()
            for coin in Account['balances']:
                if coin['asset'] != symbol:
                    continue
                return func(self.client,symbol,coin = coin)
        return inner
    
    
    
    
    
    
    
    

    def quantity_free(self,symbol:str) -> float:
        '''
        * Get your coins free quantitiy.

        - Input
            * Coin symbol: BTC , DENT , ETH , TROY

        - Outputs
            * Free quantitiy -> Float
        '''
        coin_free = 0
        for coin in self.account()['balances']:
            if coin['asset'] != symbol:
                continue
            coin_free = float(coin['free'])
            break
        return coin_free