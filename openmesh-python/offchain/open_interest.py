from core.client import OpenmeshClient

class OpenInterest(OpenmeshClient):
    def subscribe(self, exchange, symbol):
        """
        Subscribes to Open Interest events for a specific exchange and symbol.

        Args:
            exchange (str): The exchange to subscribe to.
            symbol (str): The symbol to subscribe to.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "exchange": exchange,
            "channel": "open_interest",
            "symbol": symbol
        }
        self.send_message(subscription_message)

    def unsubscribe(self, exchange, symbol):
        """
        Unsubscribes from Open Interest events for a specific exchange and symbol.

        Args:
            exchange (str): The exchange to unsubscribe from.
            symbol (str): The symbol to unsubscribe from.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "exchange": exchange,
            "channel": "open_interest",
            "symbol": symbol
        }
        self.send_message(unsubscription_message)