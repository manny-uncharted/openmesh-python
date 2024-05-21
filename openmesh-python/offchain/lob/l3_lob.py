from core.client import OpenmeshClient

class L3LOB(OpenmeshClient):
    def subscribe(self, exchange, symbol):
        """
        Subscribes to L3 Lob Events for a specific exchange and symbol.

        Args:
            exchange (str): The exchange to subscribe to.
            symbol (str): The symbol to subscribe to.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "exchange": exchange,
            "channel": "lob_l3",
            "symbol": symbol
        }
        self.send_message(subscription_message)

    def unsubscribe(self, exchange, symbol):
        """
        Unsubscribes from L3 Lob Events for a specific exchange and symbol.

        Args:
            exchange (str): The exchange to unsubscribe from.
            symbol (str): The symbol to unsubscribe from.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "exchange": exchange,
            "channel": "lob_l3",
            "symbol": symbol
        }
        self.send_message(unsubscription_message)