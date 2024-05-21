from core.client import OpenmeshClient

class DexTrades(OpenmeshClient):
    def subscribe(self, exchange):
        """
        Subscribes to Dex Trades events for a specific DEX exchange.

        Args:
            exchange (str): The DEX exchange to subscribe to.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "dex_trades",
            "exchange": exchange
        }
        self.send_message(subscription_message)

    def unsubscribe(self, exchange):
        """
        Unsubscribes from Dex Trades events for a specific DEX exchange.

        Args:
            exchange (str): The DEX exchange to unsubscribe from.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "dex_trades",
            "exchange": exchange
        }
        self.send_message(unsubscription_message)
