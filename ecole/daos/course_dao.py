# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = ("CREATE TABLE IF NOT EXISTS course ("
                   "id_course int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                   "name varchar(50) NOT NULL,"
                   "start_date date NOT NULL,"
                   "end_date date NOT NULL,"
                   "id_teacher int NOT NULL,"
                   "FOREIGN KEY(id_teacher) REFERENCES teacher(id_teacher)"
                   ")")
            cursor.execute(sql)

        return course.id

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'], record['id_teacher'])
            course.id = record['id_course']
            course.id_teacher = record['id_teacher']
        else:
            course = None

        return course

    @staticmethod
    def read_all() -> Optional[list[Course]]:
        course: Optional[list[Course]]

        with Dao.connection.cursor() as cursor:
            sql = """
            SELECT * FROM course
            LEFT JOIN teacher ON teacher.id_teacher = course.id_teacher
            """
            cursor.execute(sql)
            record = cursor.fetchall()
        if record is not None:
            course = [Course(
                rec['name'], rec['start_date'], rec['end_date'], rec['id_teacher'])
                for rec in record]
        else:
            course = None

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = ("INSERT INTO course (id_course, name, start_date, end_date, id_teacher) VALUES"
                   "(%s, %s, %s, %s, %s)")
            data = [course.id, course.name, course.start_date, course.end_date, course.teacher.id]
            cursor.execute(sql, data)
            print(cursor.rowcount)

        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
