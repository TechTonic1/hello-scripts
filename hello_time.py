# hello_time.py
from datetime import datetime

# Print Hello, World!
print("Hello, World!")

# Print the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"The current time is: {current_time}")

