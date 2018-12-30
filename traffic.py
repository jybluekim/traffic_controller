class controller:
    def __init__(self, priority=False):
        self.state = "RESET"
        self.priority = priority 

    def tick(self, waiting_mine=False, waiting_opp=False):
        if self.state == "RESET":
            if self.priority == True:
                self.state = "GREEN"
            else:
                self.state = "RED"
        elif self.state == "RED":
            self.state = "GREEN"
        elif self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"


    def output(self):
        if self.state == "RESET" or self.state == "RED":
            return "RED"
        elif self.state == "YELLOW" or self.state == "GREEN":
            return self.state



if __name__ == "__main__":
    ctrl = controller(priority=True)

    for t in range(10):
        ctrl.tick()
        print (ctrl.output())

