from core.client import OpenmeshClient

class EthereumBlocks(OpenmeshClient):
    def subscribe(self):
        """
        Subscribes to Ethereum Blocks events.

        Returns:
            None
        """
        subscription_message = {
            "action": "subscribe",
            "channel": "ethereum_blocks"
        }
        self.send_message(subscription_message)

    def unsubscribe(self):
        """
        Unsubscribes from Ethereum Blocks events.

        Returns:
            None
        """
        unsubscription_message = {
            "action": "unsubscribe",
            "channel": "ethereum_blocks"
        }
        self.send_message(unsubscription_message)
