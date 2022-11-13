import pandas as pd
import pyspark.sql
from pyspark.sql import Row

def main():
    session = pyspark.sql.SparkSession.builder.getOrCreate()

    pd_df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Billy', 'Van', 'Mark'],
        'age': [35, 53, 46],
        'height': [185, 176, 180]
    })
    df = session.createDataFrame(pd_df)

    df.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
