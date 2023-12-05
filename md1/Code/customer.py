class Customer:

    def __init__(self, cid, arrival_time):
        self.cid = cid
        self.arrival_time = arrival_time
        self.departure_time = None

    def get_wait(self):
        if self.departure_time is None:
            return None
        else:
            return self.departure_time - self.arrival_time

    def __repr__(self):
        return "Customer({}, {}, {})".format(self.cid, self.arrival_time, self.departure_time)