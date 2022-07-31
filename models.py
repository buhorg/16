from config import db


class Order(db.Model):
    """
    В таблицу Order добавим отношения, чтобы был доступ сразу к пользователю через атрибуты
    .customer
    .executor
    """
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def __repr__(self):
        return f"Order: id={self.id} name={self.name}"

    def data_to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'address': self.address,
                'price': self.price,
                'customer_id': self.customer_id,
                'executor_id': self.customer_id,
                'customer': self.customer.first_name + ' ' + self.customer.last_name,
                'executor': self.executor.first_name + ' ' + self.executor.last_name,
                }


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def __repr__(self):
        return f"User: id ={self.id}, name = {self.first_name} {self.last_name}"

    def data_to_dict(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
                'email': self.email,
                'role': self.role,
                'phone': self.phone}


class Offer(db.Model):
    """
    В таблицу Offer добавим отношения, чтобы был доступ сразу к пользователю и заявкам через атрибуты
    .order (.order.name - наименование заявки)
    .executor (.executor.first_name - имя)
    """
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    order = db.relationship("Order", foreign_keys=[order_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def __repr__(self):
        return f"Offer: id ={self.id}"

    def data_to_dict(self):
        return {'id': self.id,
                'order_id': self.order_id,
                'executor_id': self.executor_id,
                'order_name': self.order.name,
                'executor_name': self.executor.first_name + ' ' + self.executor.last_name,
                'customer': self.order.customer.first_name + ' ' + self.order.customer.last_name}
