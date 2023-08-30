from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://24xkxe6gpnd8kijcdlh3:pscale_pw_6Je8h9UktydO1uYHGmLvk7jVeNDL1I3j8Y9KIS5aE4G@aws.connect.psdb.cloud/quizbook?charset=utf8mb4"

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