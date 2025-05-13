import random as r


class Decisions:
    def __init__(self):
        self.decis = set()

    def new(self, choice):
        self.decis.add(choice)

    def remove(self, choice):
        self.decis.remove(choice)

    def rand_select(self):
        r.choice(self.decis)

    def reset(self):
        u_resp = input("Are you sure you want to clear the decisions? This cannot be undone!")
        if u_resp.lower() == "yes":
            self.decis.clear()
            return "Cache Cleared"
        else:
            return "Reset aborted!"





