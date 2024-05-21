from core.client import OpenmeshClient

class EthereumLogs(OpenmeshClient):
    def subscribe(self):
        """
        Subscribes to Ethereum Logs events.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "ethereum_logs"
        }
        self.send_message(subscription_message)

    def unsubscribe(self):
        """
        Unsubscribes from Ethereum Logs events.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "ethereum_logs"
        }
        self.send_message(unsubscription_message)