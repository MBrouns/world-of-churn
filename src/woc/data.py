import pandas as pd
import numpy as numpy
from woc.utils import log_info, log_debug


@log_debug
def _load_csv(path):
    return pd.read_csv(path, nrows=100_000)


@log_debug
def _normalize_colnames(df):
    return df.rename(columns=lambda s: s.strip())


@log_debug
def _parse_dtypes(df):
    return df.assign(
        timestamp=lambda d: pd.to_datetime(d['timestamp']),
        race=lambda d: pd.Categorical(d['race']),
        charclass=lambda d: pd.Categorical(d['charclass'])
    )


@log_info
def load(path):
    return (
        _load_csv(path)
        .pipe(_normalize_colnames)
        .pipe(_parse_dtypes)
    )