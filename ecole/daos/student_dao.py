# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class StudentDao(Dao[Student]):
    def create(self, student: Student) -> int:
        ...
        return 0

    def read(self, student_nbr: int) -> Optional[Student]:
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = ("""
                    SELECT * FROM student
                    LEFT JOIN person ON person.id_person = student.id_person
                    WHERE student.student_nbr=%s
                    """)
            cursor.execute(sql, (student_nbr,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'], record['last_name'], record['age'])
        else:
            student = None

        return student

    @staticmethod
    def read_all() -> Optional[list[Student]]:
        student: Optional[list[Student]]

        with Dao.connection.cursor() as cursor:
            sql = ("""
                    SELECT * FROM student
                    LEFT JOIN person ON person.id_person = student.id_person
                    """)
            cursor.execute(sql)
            record = cursor.fetchall()
        if record is not None:
            student = [Student(rec['first_name'], rec['last_name'], rec['age']) for rec in record]
        else:
            student = None

        return student

    def update(self, student: Student) -> bool:
        ...
        return True

    def delete(self, student: Student) -> bool:
        ...
        return True
