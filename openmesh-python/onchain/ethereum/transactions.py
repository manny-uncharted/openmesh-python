from core.client import OpenmeshClient

class EthereumTransactions(OpenmeshClient):
    def subscribe(self):
        """
        Subscribes to Ethereum Transactions events.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "ethereum_transactions"
        }
        self.send_message(subscription_message)

    def unsubscribe(self):
        """
        Unsubscribes from Ethereum Transactions events.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "ethereum_transactions"
        }
        self.send_message(unsubscription_message)
