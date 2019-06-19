from sklearn import linear_model


class MyService(object):
    def __init__(self):
        self.name = 'My Service'

    def do_it(self):
        print('do it')
        print(self.data_science())

    def data_science(self):
        model = linear_model.LinearRegression()
        model.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
        coefs = ','.join(['{}'.format(c) for c in model.coef_])
        return coefs


def main():
    my_service = MyService()
    my_service.do_it()

