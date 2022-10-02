class A:

    def __init__(self, a):
        print('A Constructor')
        self.var_a = a


class B(A):

    def __init__(self, a, b):
        super().__init__(a)
        print('B Constructor')
        self.var_b = b


class C(B):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        print('C Constructor')
        self.var_c = c


c_obj = C(1, 2, 3)
print(f'c_obj var_a={c_obj.var_a}, var_b={c_obj.var_b}, var_c={c_obj.var_c}')