from core.client import OpenmeshClient

class EthereumTokenTransfers(OpenmeshClient):
    def subscribe(self):
        """
        Subscribes to Ethereum Token Transfers events.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "ethereum_token_transfers"
        }
        self.send_message(subscription_message)

    def unsubscribe(self):
        """
        Unsubscribes from Ethereum Token Transfers events.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "ethereum_token_transfers"
        }
        self.send_message(unsubscription_message)
