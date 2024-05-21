import websocket
import json

class OpenmeshClient:
    def __init__(self, url):
        """
        Initializes the Openmesh WebSocket client.

        Args:
            url (str): The WebSocket URL to connect to.
        """
        self.url = url
        self.ws = None

    def on_message(self, message):
        """
        Callback function invoked when a message is received.

        Args:
            message (str): The received message.
        """
        print("Received message:", message)

    def on_error(self, error):
        """
        Callback function invoked when an error occurs.

        Args:
            error (Exception): The error that occurred.
        """
        print("Error:", error)

    def on_close(self):
        """Callback function invoked when the connection is closed."""
        print("Connection closed")

    def on_open(self):
        """Callback function invoked when the connection is opened."""
        print("Connection opened")

    def connect(self):
        """Establishes a WebSocket connection."""
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def send_message(self, message):
        """
        Sends a message over the WebSocket connection.

        Args:
            message (dict): The message to send, as a dictionary.
        """
        if self.ws:
            self.ws.send(json.dumps(message))