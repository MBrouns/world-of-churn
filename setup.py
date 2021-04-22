def normalize_colnames(df):
    return df.rename(columns=lambda s: s.strip())