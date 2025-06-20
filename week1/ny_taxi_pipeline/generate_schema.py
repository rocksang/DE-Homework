import pandas as pd
import json

# Load a sample of the CSV to infer schema
df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "STRING"

schema = []
for col in df.columns:
    schema.append({
        "name": col,
        "type": map_dtype(df[col].dtype),
        "mode": "NULLABLE"
    })

with open('schema.json', 'w') as f:
    json.dump(schema, f, indent=2)

print("schema.json generated.")