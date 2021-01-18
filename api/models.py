import rethinkdb as r

from flask import current_app

conn = r.connect(db="papers")

class RethinkDBModel(object):
  pass


class User(RethinkDBModel):
  _table = 'users'

  @classmethod
  def create(cls, **kwargs):
      fullname = kwargs.get('fullname')
      email = kwargs.get('email')
      password = kwargs.get('password')
      password_conf = kwargs.get('password_conf')
      if password != password_conf:
        raise ValidationError("Password and Confirm password need to be the same value")
      
      password = cls.hash_password(password)
      doc = {
        'fullname': fullname,
        'email': email,
        'password': password,
        'date_created': datetime.now(r.make_timezone('+01:00')),
        'date_modified': datetime.now(r.make_timezone('+01:00'))
        }
      r.table(cls._table).insert(doc).run(conn)
