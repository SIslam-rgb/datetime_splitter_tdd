import pandas as pd

def datetime_splitter(start,end):

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    if end < start:
        raise ValueError(f'{end} cannot be before {start}')

    rows_needed = (end.date() - start.date()).days

    return rows_needed + 1