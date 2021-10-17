"""This module uses an ORM approach and stores results processed from client requests."""

from config import db


class Factorial(db.Model):
    __tablename__ = 'factorial'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    factorial = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Factorial(number='%s', factorial='%s')>" % (self.number, self.factorial)

    def json(self):
        return {'id': self.id, 'number': self.number, 'factorial': self.factorial}

    @staticmethod
    def create_factorial(number, factorial):
        new_factorial = Factorial(number=number, factorial=factorial)
        db.session.add(new_factorial)
        db.session.commit()

    @staticmethod
    def read_all_factorials():
        return [Factorial.json(factorial) for factorial in Factorial.query.all()]

    @staticmethod
    def read_factorial(id_):
        # return [Factorial.json(Factorial.query.filter_by(id=_id).first())]
        result = Factorial.query.filter_by(id=id_).first()
        if not result:
            raise AttributeError(f"Unable to retrieve factorial from DB for id: {id_}")
        return Factorial.json(result)

    @staticmethod
    def update_factorial(id_, number, factorial):
        factorial_to_update = Factorial.query.filter_by(id=id_).first()
        if not factorial_to_update:
            raise AttributeError(f"Unable to update factorial in DB for id: {id_}")
        factorial_to_update.number = number
        factorial_to_update.factorial = factorial
        db.session.commit()

    @staticmethod
    def delete_factorial(id_):
        result = Factorial.query.filter_by(id=id_).delete()
        db.session.commit()
        return result


class Fibonacci(db.Model):
    __tablename__ = 'fibonacci'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    fibonacci = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Fibonacci(number='%s', fibonacci='%s')>" % (self.number, self.fibonacci)

    def json(self):
        return {'id': self.id, 'number': self.number, 'fibonacci': self.fibonacci}

    @staticmethod
    def create_fibonacci(number, fibonacci):
        new_fibonacci = Fibonacci(number=number, fibonacci=fibonacci)
        db.session.add(new_fibonacci)
        db.session.commit()

    @staticmethod
    def read_all_fibonacci():
        return [Fibonacci.json(fibonacci) for fibonacci in Fibonacci.query.all()]

    @staticmethod
    def read_fibonacci(id_):
        result = Fibonacci.query.filter_by(id=id_).first()
        if not result:
            raise AttributeError(f"Unable to retrieve fibonacci from DB for id: {id_}")
        return Fibonacci.json(result)

    @staticmethod
    def update_fibonacci(id_, number, fibonacci):
        result = Fibonacci.query.filter_by(id=id_).first()
        if not result:
            raise AttributeError(f"Unable to update fibonacci in DB for id: {id_}")
        result.number = number
        result.fibonacci = fibonacci
        db.session.commit()

    @staticmethod
    def delete_fibonacci(id_):
        result = Fibonacci.query.filter_by(id=id_).delete()
        db.session.commit()
        return result


class Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.Integer, nullable=False)
    exponent = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Power(base='%s', exponent='%s', power='%s')>" % (
            self.base, self.exponent, self.power)

    def json(self):
        return {'id': self.id, 'base': self.base, 'exponent': self.exponent, 'power': self.power}

    @staticmethod
    def create_power(base, exponent, power):
        new_power = Power(base=base, exponent=exponent, power=power)
        db.session.add(new_power)
        db.session.commit()

    @staticmethod
    def read_all_powers():
        return [Power.json(power) for power in Power.query.all()]

    @staticmethod
    def read_power(id_):
        # return [Power.json(Power.query.filter_by(id=_id).first())]
        result = Power.query.filter_by(id=id_).first()
        if not result:
            raise AttributeError(f"Unable to retrieve power from DB for id: {id_}")
        return Power.json(result)

    @staticmethod
    def update_power(id_, base, exponent, power):
        power_to_update = Power.query.filter_by(id=id_).first()
        if not power_to_update:
            raise AttributeError(f"Unable to update power in DB for id: {id_}")
        power_to_update.base = base
        power_to_update.exponent = exponent
        power_to_update.power = power
        db.session.commit()

    @staticmethod
    def delete_power(id_):
        result = Power.query.filter_by(id=id_).delete()
        db.session.commit()
        return result
