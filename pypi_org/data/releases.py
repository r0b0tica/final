import datetime

import sqlalchemy
from sqlalchemy import orm

from pypi_org.data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    major_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    minor_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    build_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    create_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    comment = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String)
    size = sqlalchemy.Column(sqlalchemy.BigInteger)

    # package relationship
    package_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("packages.id"))
    package = orm.relation('package')

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
