from core.client import OpenmeshClient

class DexLiquidity(OpenmeshClient):
    def subscribe(self, exchange):
        """
        Subscribes to Dex Liquidity events for a specific DEX exchange.

        Args:
            exchange (str): The DEX exchange to subscribe to.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "dex_liquidity",
            "exchange": exchange
        }
        self.send_message(subscription_message)

    def unsubscribe(self, exchange):
        """
        Unsubscribes from Dex Liquidity events for a specific DEX exchange.

        Args:
            exchange (str): The DEX exchange to unsubscribe from.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "dex_liquidity",
            "exchange": exchange
        }
        self.send_message(unsubscription_message)
