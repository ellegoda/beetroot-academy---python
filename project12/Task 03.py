CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_Channel = 1

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[2]

    def turn_channel(self, n):
        self.current_Channel = n
        return self.channels[n]

    def next_channel(self):
        if self.current_Channel == 3:
            self.current_Channel = 1
        else:
            self.current_Channel += 1

        return self.channels[self.current_Channel - 1]

    def previous_channel(self):
        if self.current_Channel == 1:
            self.current_Channel = 3
        else:
            self.current_Channel -= 1

        return self.channels[self.current_Channel - 1]

    def current_channel(self):
        return self.channels[self.current_Channel - 1]

    def is_exist(self, n):
        if type(n) == int:
            if 1 <= n <= 3:
                return "Yes"
            else:
                return "No"
        else:
            for channel in self.channels:
                if channel == n:
                    return "Yes"

            return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
