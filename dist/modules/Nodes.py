# Numerical Class: Takes in an Integer or a Float
class Numerical:
    def __init__(self, tokenised_int_float):
        self.tokenised_int_float = tokenised_int_float

        self.pos_start = self.tokenised_int_float.pos_start
        self.pos_end = self.tokenised_int_float.pos_end

    def __str__(self):
        return self.tokenised_int_float


# Calculation Class: Preform operation on the given nodes/vars
class Calculation:
    def __init__(self, var_l, var_operator, var_r):
        self.var_l = var_l
        self.var_operator = var_operator
        self.var_r = var_r

        self.pos_start = self.var_l.pos_start
        self.pos_end = self.var_r.pos_end

    def __str__(self):
        return "(%s,%s,%s)" % (self.var_l, self.var_operator, self.var_r)


# PositiveNegative Class: Takes in the Operator node and Numerical node for pos/neg
class PositiveNegative:
    def __init__(self, var_operator, tokenised_int_float):
        self.var_operator = var_operator
        self.tokenised_int_float = tokenised_int_float

        self.pos_start = self.var_operator.pos_start
        self.pos_end = tokenised_int_float.pos_end

    def __str__(self):
        return "%s,%s" % (self.var_operator, self.tokenised_int_float)
