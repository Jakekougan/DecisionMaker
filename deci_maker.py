import random as r


class Decisions:
    def __init__(self):
        self.decis = []

    def new(self, choice):
        self.decis.append(choice)

    def remove(self, choice):
        self.decis.pop(choice)

    def rand_select(self):
        return r.choice(self.decis)


    def reset(self):
        u_resp = input("Are you sure you want to clear the decisions? This cannot be undone!")
        if u_resp.lower() == "yes":
            self.decis.clear()
            return "Cache Cleared"
        else:
            return "Reset aborted!"







