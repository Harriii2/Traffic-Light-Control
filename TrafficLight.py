# Simple Traffic Light control system(Expert System)
# - To control Traffic Light
# - Python

import time

class TrafficLightExpertSystem:
    def __init__(self, traffic_density="Medium"):
        # Initial state of Traffic Light
        self.state = "RED" 
        self.traffic_density = traffic_density

    def apply_rules(self):
        if self.state == "RED":
            self.handle_red_light()
        elif self.state == "GREEN":
            self.handle_green_light()
        elif self.state == "YELLOW":
            self.handle_yellow_light()

    def handle_red_light(self):
        print("Traffic Light: RED 🔴")
        time.sleep(5)
        self.state = "GREEN"

    def handle_green_light(self):
        if self.traffic_density == "High":
            print("Traffic Light: GREEN 🟢") #High Traffic - Extended Time
            time.sleep(8)

        elif self.traffic_density == "Medium":
            print("Traffic Light: GREEN 🟢")  #High Traffic - Normal Time
            time.sleep(5)

        else:  # Low traffic
            print("Traffic Light: GREEN 🟢")  #Low Traffic - Shortened Time
            time.sleep(3) 
        self.state = "YELLOW"

    def handle_yellow_light(self):
        print("Traffic Light: YELLOW 🟡")
        time.sleep(2) 
        self.state = "RED"

    def run(self):
        while True:
            self.apply_rules()

if __name__ == "__main__":
    # Simulate different traffic conditions (High, Medium, Low)
    traffic_density = input("Enter traffic density (High/Medium/Low): ")
    traffic_light = TrafficLightExpertSystem(traffic_density)
    print("🚦 Traffic Light Control Based On Expert System is running...")
    traffic_light.run()