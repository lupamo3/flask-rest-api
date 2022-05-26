
from datetime import datetime

import json
import enum

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_login import UserMixin



db = SQLAlchemy()


class Users(UserMixin, db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.Text())
    jwt_auth_active = db.Column(db.Boolean())
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    roles = db.relationship('Role', secondary='user_roles')
    leads = db.relationship('Leads', backref='users', lazy='dynamic')
    customer = db.relationship('Customer', backref='users', lazy='dynamic')

    def __repr__(self):
        return f"User {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_email(self, new_email):
        self.email = new_email

    def update_username(self, new_username):
        self.username = new_username

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    def get_all_users():
        users = Users.query.all()
        return users

    # @login.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def toDICT(self):
        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['username'] = self.username
        cls_dict['email'] = self.email
        return cls_dict

    def toJSON(self):
        return self.toDICT()

class RolesDefault(enum.Enum):
    lead_create = '989'
    customer_create = '2' 

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Enum(
                        RolesDefault), 
                        default=RolesDefault.lead_create,
                        nullable=False)

    def __repr__(self):
        return f"Role {self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class JWTTokenBlocklist(db.Model):
    __tablename__ = 'jwt_token_blocklist'

    id = db.Column(db.Integer(), primary_key=True)
    jwt_token = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"


    def save(self):
        db.session.add(self)
        db.session.commit()


class Leads(db.Model):

    __tablename__ = 'leads'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    # created_by_user = db.relationship("Users", backref=backref("leads", uselist=False))


    def __repr__(self):
        return f"Leads {self.first_name} {self.last_name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def toDICT(self):
        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['first_name'] = self.first_name
        cls_dict['last_name'] = self.last_name
        cls_dict['middle_name'] = self.middle_name
        cls_dict['phone_number'] = self.phone_number
        cls_dict['location'] = self.location
        cls_dict['gender'] = self.gender
        cls_dict['date_created'] = self.date_created
        cls_dict['created_by'] = self.created_by
        # cls_dict['created_by_user'] = self.created_by_user

    def toJSON(self):
        return self.toDICT()

    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def get_all_leads():
        leads = Leads.query.all()
        return leads

class ProductsofInterest(enum.Enum):
    product_a = 10,000
    product_b = 20,000  
    product_c = 30,000

class Customer(db.Model):
    __tablename__ = 'customer'
    

    id = db.Column(db.Integer(), primary_key=True)
    photo = db.Column(db.String(64), nullable=False)
    annual_earnings = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    products_interested = db.Column(
                                db.Enum(ProductsofInterest), 
                                default=ProductsofInterest.product_a, 
                                nullable=False
    )
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Customer {self.id}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def toDICT(self):
        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['photo'] = self.photo
        cls_dict['annual_earnings'] = self.annual_earnings
        cls_dict['date_created'] = self.date_created
        cls_dict['products_interested'] = self.products_interested
        cls_dict['created_by'] = self.created_by
        return cls_dict

    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def toJSON(self):
        return self.toDICT()

    def update_photo(self, new_photo):
        self.photo = new_photo

    


