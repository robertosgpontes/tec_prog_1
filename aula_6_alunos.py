from sqlalchemy import create_engine
import pandas as pd
from pandasql import PandaSQL

engine = create_engine("mysql+mysqldb://root:@localhost/test")
#engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
connection = engine.connect()
pdsql = PandaSQL()

#query = "SELECT * FROM timer"
#df = pd.read_sql(query, connection)
#print(df)

#query = "SELECT * FROM estado_cidade"
#df = pd.read_sql(query, connection)
#query_python = "SELECT * FROM df WHERE uf = 'AC'"
#df_final = pdsql(query_python)
#print(df_final)


d = {'start_time': ['7:00 pm'], 'end_time': ['8:00 am']}
df = pd.DataFrame(data=d)
print(df)
df.to_sql('teste_ada', con=engine, index=False, if_exists='replace')
print("Deu certo!")


