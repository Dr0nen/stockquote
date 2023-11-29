#stockquote
# basis: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-yahoo
# 

import pandas as pd
import numpy as np
import pandas_datareader.data as web
from datetime import datetime
# import plotly.graph.objs as go
# import datetime as dt
#import pandas.io.data as web
#from datetime import datetime

tickers = ['ORCL', 'TSLA', 'IBM', 'MSFT']
ls_key = 'Adj Close'
start = datetime(2022,1,1)
end = datetime(2022,12,31)
df = web.DataReader(tickers, 'yahoo', start, end)
df.head
