from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Boolean, ARRAY, ForeignKey

from app.store.database.sqlalchemy_base import db


@dataclass
class Theme:
    id: int | None
    title: str


@dataclass
class Question:
    id: int | None
    title: str
    theme_id: int
    answers: list["Answer"]


@dataclass
class Answer:
    title: str
    is_correct: bool


class ThemeModel(db):
    __tablename__ = "themes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


class QuestionModel(db):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    theme_id = Column(Integer, nullable=False)
    # answers = Column(ARRAY(), ForeignKey())


class AnswerModel(db):
    __tablename__ = "answers"
    title = Column(String, primary_key=True)
    is_correct = Column(Boolean, nullable=False)
