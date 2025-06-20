import pandas as pd
from sqlalchemy import create_engine
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--user', required=True)
parser.add_argument('--password', required=True)
parser.add_argument('--host', required=True)
parser.add_argument('--port', required=True)
parser.add_argument('--db', required=True)
parser.add_argument('--table_name', required=True)
parser.add_argument('--url', required=True)

args = parser.parse_args()

df = pd.read_csv(args.url)

engine = create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}')

df.head(0).to_sql(name=args.table_name, con=engine, if_exists='replace')
df.to_sql(name=args.table_name, con=engine, if_exists='append')
