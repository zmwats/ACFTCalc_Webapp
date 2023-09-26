#agerangetest

class ageranges():
    def __init__(self, agerange1m, agerange1f, agerange2m, agerange2f, agerange3m, agerange3f,
                 agerange4m, agerange4f, agerange5m, agerange5f, agerange6m, agerange6f,
                 agerange7m, agerange7f, agerange8m, agerange8f, agerange9m, agerange9f, 
                 agerange10m, agerange10f, agerangeplnkmax):
        self.agerange1m = agerange1m # Use for males
        self.agerange1f = agerange1f # Use for females
        self.agerange2m = agerange2m
        self.agerange2f = agerange2f
        self.agerange3m = agerange3m
        self.agerange3f = agerange3f
        self.agerange4m = agerange4m
        self.agerange4f = agerange4f
        self.agerange5m = agerange5m
        self.agerange5f = agerange5f
        self.agerange6m = agerange6m
        self.agerange6f = agerange6f
        self.agerange7m = agerange7m
        self.agerange7f = agerange7f
        self.agerange8m = agerange8m
        self.agerange8f = agerange8f
        self.agerange9m = agerange9m
        self.agerange9f = agerange9f
        self.agerange10m = agerange10m
        self.agerange10f = agerange10f
        self.agerangeplnkmax = agerangeplnkmax


ranges = ageranges(range(17, 21), range(17, 21), range(22, 26), range(22, 26), range(27, 31), range(27, 31),
        range(32, 36), range(32, 36), range(37,41), range(37, 41), range(42, 46), range(42, 46),
        range(47, 51), range(47, 51), range(52, 56), range(52, 56), range(57, 61), range(57, 61), range(62, 66), range(62, 66), range(37, 100))
