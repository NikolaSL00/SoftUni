# Create a class called Smartphone. Upon initialization, it should receive a memory (number). It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default). Create 3 methods:
# power() - sets is_on on True if the phone is off, otherwise sets it to False
# install(app, app_memory)
# If there is enough memory on the phone and it is on, installs the app (add it to apps and decrease the memory of the phone) and returns "Installing {app}"
# If there is enough memory, but the phone is off, returns "Turn on your phone to install {app}"
# Otherwise, returns "Not enough memory to install {app}"
# status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"

# Test Code:
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())

# Desired Output:
# Turn on your phone to install Facebook
# Installing Facebook
# Installing Messenger
# Not enough memory to install Instagram
# Total apps: 2. Memory left: 20

class Smartphone:

    def __init__(self, memory: float):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"

        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
