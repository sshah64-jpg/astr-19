class Panda:
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.eye_count = eye_count
        self.has_tail = has_tail
        self.is_furry = is_furry

    def attributes(self):
        print("Panda:\n")
        print("Arm Length: 30cm")
        print("Leg Length: 30 cm")
        print("Eye Count: 2")
        print("Has a tail")
        print("Is very furry")

myPanda = Panda(30, 30, 2, True, True)

myPanda.attributes()