# hello_time_oop.py
from datetime import datetime

class HelloWorld:
    def __init__(self):
        self.message = "Hello, World!"

    def greet(self):
        print(self.message)

class TimeDisplay:
    def __init__(self):
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def show_time(self):
        print(f"The current time is: {self.current_time}")

class HelloWorldWithTime:
    def __init__(self):
        self.hello = HelloWorld()
        self.time_display = TimeDisplay()

    def run(self):
        self.hello.greet()
        self.time_display.show_time()

# Execute the script
if __name__ == "__main__":
    hello_world_with_time = HelloWorldWithTime()
    hello_world_with_time.run()

