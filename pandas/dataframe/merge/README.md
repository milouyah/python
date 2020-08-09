# merge

## Tutorial
[Community tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)

## [Comparing Rows Between Two Pandas DataFrames](https://hackersandslackers.com/compare-rows-pandas-dataframes/)
```python
def dataframe_difference(df1, df2, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv('data/diff.csv')
    return diff_df
```

## [Python Pandas - DataFrame](https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm)

### Links

https://www.tutorialspoint.com/python_pandas/python_pandas_merging_joining.htm