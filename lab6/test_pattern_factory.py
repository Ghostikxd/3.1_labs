allow_speed_town = 60
allow_speed_outside_town = 110


class Penalty:
    def process(suspectspeed, locality):
        processing = suspect_locality(locality)
        return print(processing(suspectspeed))


def suspect_locality(locality):
    if locality == 'Town':
        return check_over_speed_town
    elif locality == 'Outside town':
        return check_over_speed_outside_town
    else:
        raise ValueError(locality)


def check_over_speed_town(suspectspeed):
    if suspectspeed > allow_speed_town+20:
        return 'Over speed - Yes'
    else:
        return 'Over speed - No'


def check_over_speed_outside_town(suspectspeed):
    if suspectspeed > allow_speed_outside_town+20:
        return 'Over speed - Yes'
    else:
        return 'Over speed - No'


if __name__ == "__main__":
    Penalty.process(suspectspeed=90, locality='Outside town')

""" class Sort:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f': {self.type}'

    def _get_type(type):
        if type == 1:
            return 'go left'
        if type == 2:
            return 'go right'
        if type == 3:
            return 'go forward'
        else:
            return Sort('Error type')


test = Sort._get_type(1)
print(test)
"""
