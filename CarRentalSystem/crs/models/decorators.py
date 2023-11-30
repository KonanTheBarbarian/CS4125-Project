
def add_price_for_under_25(self):
    if self.reservation.is_under_25:
        return 100
    else:
        return 0


def add_price_for_child_seat(self):
    if self.reservation.is_child_seat:
        return 25
    else:
        return 0
