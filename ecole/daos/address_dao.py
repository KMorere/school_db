# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        ...
        return 0

    def read(self, id_address: int) -> Optional[Address]:
        address: Optional[Address]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address WHERE id_address=%s"
            cursor.execute(sql, (id_address,))
            record = cursor.fetchone()
        if record is not None:
            address = Address(record['street'], record['city'], record['postal_code'])
            address.id = record['id_address']
        else:
            address = None

        return address

    @staticmethod
    def read_all() -> Optional[list[Address]]:
        address: Optional[list[Address]]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address"
            cursor.execute(sql)
            record = cursor.fetchall()
        if record is not None:
            address = [Address(rec['street'], rec['city'], rec['postal_code']) for rec in record]
        else:
            address = None

        return address

    def update(self, address: Address) -> bool:
        ...
        return True

    def delete(self, address: Address) -> bool:
        ...
        return True
