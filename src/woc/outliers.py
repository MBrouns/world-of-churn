from woc.utils import log_info, log_debug

@log_debug
def _remove_below_min_level(df, min_lvl=10):
    """removes all characters from the dataset that didn't reach at least level `lvl`"""
    return df.loc[lambda d: d.groupby('char')['level'].transform('max') > min_lvl]


@log_info
def remove(df, min_lvl):
    return (
        df
        .pipe(_remove_below_min_level, min_lvl=min_lvl)
    )
