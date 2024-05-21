from core.client import OpenmeshClient

class L2Trades(OpenmeshClient):
    def subscribe(self, symbol, exchange, frequency):
        """
        Subscribes to L2 trades data for a specific symbol, exchange, and frequency.

        Args:
            symbol (str): The symbol to subscribe to.
            exchange (str): The exchange to subscribe to.
            frequency (str): The frequency of messages.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "exchange": exchange,
            "channel": "trades",
            "symbol": symbol,
            "frequency": frequency
        }
        self.send_message(subscription_message)

    def unsubscribe(self, symbol):
        """
        Unsubscribes from L2 trades data for a specific symbol.

        Args:
            symbol (str): The symbol to unsubscribe from.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "trades",
            "symbol": symbol
        }
        self.send_message(unsubscription_message)