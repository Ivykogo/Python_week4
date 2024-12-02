class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def browse_internet(self, website):
        print(f"Browsing {website}")

# Creating a Smartphone object
my_phone = Smartphone("Apple", "iPhone 15", 256, "Black")

# Using the methods
my_phone.make_call("+1234567890")
my_phone.send_message("+9876543210", "Hello, World!")
my_phone.browse_internet("google.com")