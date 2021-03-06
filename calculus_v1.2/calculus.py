from sympy import symbols, diff, integrate, cos, sin, simplify, Interval, exp, sqrt, log, pi, series, limit, E, acos, asin, tan, atan

### ERROR CODES
### -1: dimensional error
### -2: unsupported case


### defines the coordinate system and the temporal coordinate as symbols objects
x, y, z, t = symbols('x, y, z, t')
cart = (x, y, z)  ### this is needed for semplification reasons ahead

### vectors are tuple objects
### below are defined their basic operations

def dot(u, v):
    if len(u) != len(v):
        print('ERROR: the two vectors must belong to the same vectorial space')
        return -1
    else:
        sum = 0
        for i, j in zip(u, v):
            sum = sum + i*j
        return sum

def cross(u, v):
    if len(u) != 3 or len(u) != len(v):
        print('ERROR: the two vectors must belong to R^3')
        return -1
    else:
        return (u[1]*v[2]-u[1]*v[2], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

def norm(u):
    return simplify(sqrt(dot(u, u)))



### sets as defined as set objects with the following attributes
        # n: the dimension of the set (1, 2 or 3)
        # v: the outermost integration variable, if n = 1 this will be the integration variable
        # a: the interval where the integral in dv will be evalueted, both members must be real numbers
        # v2: if n = 2 it's the first variable of integration, if n = 3 it's the second
        # b: the interval in which the integral in dv2 will be evalueted
            #each of the two values, or both, can be a function f(v)
        # v3: insert only if n = 3, will be the first variable of integration
        # c: the interval in which the integral in dv3 will be evaluated
            #each of the two values, or both, can be a function f(v, v2)
#   if n = 1 || n = 2 the values which will not be of use must be left empty (if assigned
#   will not be used)
# no methods are currently defined

class sets():
    def __init__(self, n = 1, v = x, a = Interval(0, 1), v2 = y, b = Interval(0, 1), v3 = z, c = Interval(0, 1)):
        self.n = n
        self.v = v
        self.a = a
        self.v2 = v2
        self.b = b
        self.v3 = v3
        self.c = c


### surfaces are sigma objects with the following attributes:
        # t: is the third variable (the surface is equivalent to z = g(x, y))
        # s: function g(x, y) to be parametrized
        # a: indicates wheter of not n scalar t is positive or negative
class sigma():
    def __init__(self, t = z, g = function(), i = sets(), a = '+'):
        self.t = t
        self.s = s
        self.i = i
        self.a = a

    ### returns a parametrization of the surface
    def sigmap(self):
        pass



### functions are defined as an object with the following attributes:
        # f: the function
        # n: the number of variables
        # var: the variables
### in it the basic calculus functions are defined as functions of the object

class function():
    def __init__(self, f = 0, n = 3, var = (x, y, z)):
        self.f = f
        self.n = n
        self.var = var

    ### simplify the function and returns a new function object as a result
    def sim(self):
        return function(simplify(self.f), self.n, self.var)

    ### returns the derivative of the function in respect to the var variable
    def der(self, var):
        return function(simplify(diff(self.f, var)), self.n)

    ### returns the gradiens
    def grad(self):
        f = self.f
        if n == 2:
            return vector(2, (der(f, var[0]), der(f, var[1])))
        if n == 3:
            return vector(3, (der(f, var[0]), der(f, var[1]), der(f, var[2])))
        else:
            print('ERROR: wrong dimensions, all functions must have at most 3 dimensions')
            return -2

    ### simply prints the function (note that writing print(function()) would return blah.blah object at 0x123456789
    def prnt(self):
        print(f'f({var}) = {simplify(self.f)}')

    ### returns the indefinte integral
    def i_int(self, x):
        return function(simplify(integrate(self.f, x)), self.n)

    ### returns the limit of the function when the variable x approches x0
    def lim(self, x, x0):
        return function(limit(self.f, x, x0), self.n)
    ### returns the directional limit
    def dir_lim(self, x, x0, dir):
        ### dir must be '+' or '-'
        return function(limit(self.f, x, x0, dir), self.n)

    ### Returns the taylor series of the function
    def taylor(self, x, x0, degr):
        ### x is the variable, x0 is the point in which the expansion is evaluated and degr is the degree of the expansion
        ### taylor(function(cos(x), 1), x, 0, 3) = 1 + x**2/2
        return function(series(self.f, x, x0, degr), self.n)

    ### evaluetes the function in the x0 point
    def evl(self, x0):
        pass

    ### returns the integrl of the function; s is a sets object self.n and s.n need to be the same
    def integral(self, s):
        if self.n != s.n:
            print("ERROR: the set and the function don't belong to the same vector space")
            return -1
        else:
            if self.n == 2:
                pass

    def l_integral(self, g):
        pass
    def s_integral(self, s):
        pass
    def max_min(self, x0):
        pass

### vectorial fields are defined as vecotor objects with the following attributes:
        # f: a tuple of function objects
        # n: the number of dimensions

class vector():
    def __init__(self, n = 3, f = (function(), function(), function()), var = (x, y, z)):
        self.n = n
        self.f = f
        self.var = var

    ### Returns the tuple as a vector of the appropriate dimension by appending to an empty
    ### list and then converting it in a tuple and returning
    def vec(self):
        vec_l = []
        for i in range(self.n):
            vec_l.append(simplify(self.f[i].f))
        return tuple(vec_l)
    ### print the vector, same as function class
    def prnt(self):
        print(self.vec())
        return 0

    ### returns the divergence of the vector
    def div(self):
        f = 0
        for i in range(self.n):
            f = f + self.f[i].der(var[i]).f
        return function(simplify(f), self.n)

    ### returns the curl of the vector field
    def curl(self):
        if self.n != 3:
            print('ERROR: curl operation is only applicable to R^3')
            return -2
            ### here returns -2 instead of -1 because while formally curl is indeed
            ### an operation only of R^3 in less formal context could be applicabile
            ### to R^2 vectors, I may implement it later
        else:
            f1 = self.f[2].der(y) - self.f[1].der(z)
            f2 = self.f[0].der(z) - self.f[2].der(x)
            f3 = self.f[1].der(x) - self.f[0].der(y)
            return vector(self.n, f = (f1.sim(), f2.sim(), f3.sim()))

    def gauss(self):
        pass
    def stokes(self):
        pass
    def flux(self):
        pass
    def p_integral(self):
        pass
    def evl(self, x0):
        pass


###### IMPLEMENT DEFINITE INTEGRALS
###### NEED TO ADD PLOTTING FEATURE (MIGHT DO IT WITH An OCTAVE SCRIPT)

###### NEEDS EXTENSIVE TESTING IN EVERY OTHER FRONT

f1 = function(sin(x), n = 1)
f2 = function(cos(x), n = 1)

F = vector(n = 2, f = (f1, f2))

F.prnt()


