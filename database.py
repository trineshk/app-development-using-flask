from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_questions_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM quiz"))
    result_all = result.all()
    questions = []
    for row in result_all:
      questions.append(row._asdict())
    return questions
