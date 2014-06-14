from decimal import Decimal
import gmpy2
from random import randint

gmpy2.get_context().precision = 160


class Expression(object):

    def __init__(self):
        self.settings = {
            'division': False,
            'division_nesting': 0,
            'nesting': 0,
            'desired_nesting': 1,
        }




class Numeric(Expression):

    def __init__(self, anum):
        self.val = gmpy2.mpfr(anum)

    def __str__(self):
        return self.val.__str__()

    def __repr__(self):
        return "Numeric('" + self.val.__str__() + "')"

    def __add__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val + other.val)
        return Numeric(self.val + gmpy2.mpfr(other))

    def __sub__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val - other.val)
        return Numeric(self.val - gmpy2.mpfr(other))

    def __mul__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val * other.val)
        return Numeric(self.val * gmpy2.mpfr(other))

    def __div__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val / other.val)
        return Numeric(self.val / gmpy2.mpfr(other))

    def __mod__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val % other.val)
        return Numeric(self.val % gmpy2.mpfr(other))

    def __pow__(self, other):
        if hasattr(other, 'val'):
            return Numeric(self.val ** other.val)
        return Numeric(self.val ** gmpy2.mpfr(other))

    def __lt__(self, other):
        if hasattr(other, 'val'):
            return (self.val < other.val)
        return (self.val < gmpy2.mpfr(other))

    def __gt__(self, other):
        if hasattr(other, 'val'):
            return (self.val > other.val)
        return (self.val > gmpy2.mpfr(other))

    def __le__(self, other):
        if hasattr(other, 'val'):
            return (self.val <= other.val)
        return (self.val <= gmpy2.mpfr(other))

    def __ge__(self, other):
        if hasattr(other, 'val'):
            return (self.val >= other.val)
        return (self.val >= gmpy2.mpfr(other))

    def __eq__(self, other):
        if hasattr(other, 'val'):
            return (self.val == other.val)
        return (self.val == gmpy2.mprf(other))

    def ln(self):
        return Numeric(gmpy2.log(self.val))

    def log(self):
        return Numeric(gmpy2.log10(self.val))

    def exp(self):
        return Numeric(gmpy2.exp(self.val))

    def antilog(self):
        return Numeric(gmpy2.exp10(self.val))

    def sin(self):
        return Numeric(gmpy2.sin(self.val))

    def cos(self):
        return Numeric(gmpy2.cos(self.val))

    def tan(self):
        return Numeric(gmpy2.tan(self.val))

    def arcsin(self):
        return Numeric(gmpy2.asin(self.val))

    def arccos(self):
        return Numeric(gmpy2.acos(self.val))

    def arctan(self):
        return Numeric(gmpy2.atan(self.val))

    def square(self):
        return Numeric(gmpy2.square(self.val))

    def sqrt(self):
        return Numeric(gmpy2.sqrt(self.val))

    def inverse(self):
        return self ** (Numeric(-1))

    def round(self, prec=2):
        k = "%.2e" % self.val
        return Numeric(k)

    def n(self):
        return '%.2e' % self.val

    def latex(self):
        d = Decimal('%.2e' % self.val)
        m = d.as_tuple()
        dig = m[1]
        exponent = m[2] + 2
        s = "-" if m[0] == 1 else ""
        if (exponent < -3 or exponent > 4):
            s += (str(dig[0]) + "." + str(dig[1]) + str(dig[2]) +
                        ' \times ' + '10^{' + str(exponent) + '}')
            return s

        if exponent >= 2:
            s += str(dig[0]) + str(dig[1]) + str(dig[2])
            for num in range(exponent - 2, 0, -1):
                s += "0"
            return s

        if exponent <= -1:
            s += "0."
            for i in range(0, exponent + 1, -1):
                s += "0"
            s += str(dig[0]) + str(dig[1]) + str(dig[2])
            return s

        for i in range(3):
            s += str(dig[i])
            if i == exponent:
                s += "."

        return s

    @staticmethod
    def new():
        exponent = randint(-3, 3)
        num1, num2, num3 = randint(0, 9), randint(0, 9), randint(0, 9)
        initializer = (str(num1) + "." + str(num2) +
                            str(num3) + "e" + str(exponent))

        if (randint(0, 1) == 1):
            initializer = "-" + initializer

        return Numeric(initializer)

    @staticmethod
    def create(minexp, maxexp):
        exponent = randint(minexp, maxexp)
        num1, num2, num3 = randint(0, 9), randint(0, 9), randint(0, 9)
        initializer = (str(num1) + "." + str(num2) +
                            str(num3) + "e" + str(exponent))

        if (randint(0, 1) == 1):
            initializer = "-" + initializer

        return Numeric(initializer)


    def eval(self):
        return self

    def getexponent(self):
        return int(gmpy2.floor(self.log().val))



PI = Numeric(gmpy2.const_pi())
PI.latex = lambda: '\pi'
E = Numeric(gmpy2.exp(1))

class Model1(Expression):
    def __init__(self):
        self.value = Numeric.new()
        self.text = str(self.value)

    def gen(self):
        x = randint(1, 550)
        if (x < 120):
            z = Numeric.create(self.value.getexponent() - 1, self.value.getexponent() + 1)
            self.text = z.latex() + " + " + self.value.latex()
            self.value = self.value + z
        elif (x < 240):
            z = Numeric.create(self.value.getexponent() - 1, self.value.getexponent() + 1)
            self.text = z.latex() + " - " + self.latex()
            self.value = self.value - z
        elif (x < 360):
            z = Numeric.create(self.value.getexponent() - 3, self.value.getexponent() + 3)
            self.text = "\\left(" + z.latex() + "\\right) \\left(" + self.value.latex() + "\\right)"
            self.value = self.value - z
        elif (x < 480):
            z = Numeric.new()
            self.text = "\\frac{" + self.value.latex() + "}{" + z.latex() + "}"
            self.value = self.value - z
        elif (z < 550):
            z = Numeric.create(-1, 1)
            self.text = self.value + "^{" + z.latex() + '}'
            self.value = self.value ** z



