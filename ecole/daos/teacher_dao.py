# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.teacher import Teacher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        ...
        return 0

    def read(self, id_person: int) -> Optional[Teacher]:
        teacher: Optional[Teacher]

        with Dao.connection.cursor() as cursor:
            sql = ("""
                    SELECT * FROM teacher
                    LEFT JOIN person ON person.id_person = teacher.id_person
                    WHERE teacher.id_teacher=%s
                    """)
            cursor.execute(sql, (id_person,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'], record['last_name'], record['age'], record['hiring_date'])
            teacher.id = record['id_teacher']
        else:
            teacher = None

        return teacher

    @staticmethod
    def read_all() -> Optional[list[Teacher]]:
        teacher: Optional[list[Teacher]]

        with Dao.connection.cursor() as cursor:
            sql = ("""
                    SELECT * FROM teacher
                    LEFT JOIN person ON person.id_person = teacher.id_person
                    """)
            cursor.execute(sql)
            record = cursor.fetchall()
        if record is not None:
            teacher = [Teacher(rec['first_name'], rec['last_name'], rec['age'], rec['hiring_date'])
                       for rec in record]
        else:
            teacher = None

        return teacher

    def update(self, teacher: Teacher) -> bool:
        ...
        return True

    def delete(self, teacher: Teacher) -> bool:
        ...
        return True
