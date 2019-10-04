参考

https://stackoverflow.com/questions/40018405/cython-cannot-open-include-file-io-h-no-such-file-or-directory

find /c/Program\ Files\ \(x86\)/ -name <name_of_error_causing_file>

例如
find /c/Program\ Files\ \(x86\)/ -name vcruntime.h
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include

https://stackoverflow.com/questions/38290169/cannot-find-corecrt-h-universalcrt-includepath-is-wrong/51219000#51219000

C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include 包括到inclue里面去

**install requires**

<class 'list'>: ['pip>=7.1.0', 'setuptools==41.2.0', 'Logbook==0.12.5', 'pytz==2016.4', 'numpy==1.16.5', 'requests-file==1.4.3', 'scipy==1.0.0', 'pandas==0.19.2', 'pandas-datareader==0.6.0', 'patsy==0.5.0', 'statsmodels==0.8.0', 'python-dateutil==2.7.3', 'six==1.11.0', 'requests==2.20.1', 'Cython==0.27.3', 'cyordereddict==1.0.0', 'bottleneck==1.2.1', 'contextlib2==0.5.5', 'decorator==4.3.0', 'networkx==2.1', 'numexpr==2.6.4', 'bcolz==1.2.1', 'click==6.7', 'toolz==0.9.0', 'multipledispatch==0.4.9', 'MarkupSafe==1.0', 'Mako==1.0.7', 'sqlalchemy==1.2.2', 'alembic==0.9.7', 'sortedcontainers==1.5.9', 'intervaltree==2.1.0', 'lru-dict==1.1.6', 'empyrical==0.2.1', 'tables==3.4.2', 'certifi==2018.1.18', 'ccxt==1.17.94', 'boto3==1.5.27', 'redo==2.0.1', 'web3==4.4.1', 'requests-toolbelt==0.8.0']

**extras_require**

<class 'dict'>: {'dev': ['coverage==4.4.1', 'nose==1.3.7', 'nose-parameterized==0.5.0', 'nose-ignore-docstring==0.2', 'termcolor==1.1.0', 'nose-timer==0.5.0', 'xlrd==0.9.4', 'funcsigs==1.0.2', 'Pygments==2.0.2', 'alabaster==0.7.6', 'babel==1.3', 'docutils==0.12', 'snowballstemmer==1.2.0', 'sphinx-rtd-theme==0.1.8', 'sphinx==1.6.7', 'pbr==1.10.0', 'mock==2.0.0', 'testfixtures==4.1.2', 'flake8==3.3.0', 'mccabe==0.6.0', 'pycodestyle==2.3.1', 'pyflakes==1.5.0', 'pyandoc==0.0.1', 'docopt==0.6.2', 'numpydoc==0.5', 'mistune==0.7', 'certifi==2018.1.18', 'tornado==4.2.1', 'pyparsing==2.2.0', 'cycler==0.10.0', 'matplotlib==2.2.2', 'mpl_finance==0.10.0', 'Markdown==2.6.2', 'futures==3.0.5', 'requests-futures==0.9.7', 'piprot==0.9.6', 'responses==0.4.0'], 'talib': ['TA-Lib==0.4.9'], 'all': ['coverage==4.4.1', 'nose==1.3.7', 'nose-parameterized==0.5.0', 'nose-ignore-docstring==0.2', 'termcolor==1.1.0', 'nose-timer==0.5.0', 'xlrd==0.9.4', 'funcsigs==1.0.2', 'Pygments==2.0.2', 'alabaster==0.7.6', 'babel==1.3', 'docutils==0.12', 'snowballstemmer==1.2.0', 'sphinx-rtd-theme==0.1.8', 'sphinx==1.6.7', 'pbr==1.10.0', 'mock==2.0.0', 'testfixtures==4.1.2', 'flake8==3.3.0', 'mccabe==0.6.0', 'pycodestyle==2.3.1', 'pyflakes==1.5.0', 'pyandoc==0.0.1', 'docopt==0.6.2', 'numpydoc==0.5', 'mistune==0.7', 'certifi==2018.1.18', 'tornado==4.2.1', 'pyparsing==2.2.0', 'cycler==0.10.0', 'matplotlib==2.2.2', 'mpl_finance==0.10.0', 'Markdown==2.6.2', 'futures==3.0.5', 'requests-futures==0.9.7', 'piprot==0.9.6', 'responses==0.4.0', 'TA-Lib==0.4.9']}

windows 安装[参考](https://blog.csdn.net/Kaige_Zhao/article/details/80315697)
D:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.10.25017\bin\HostX64\x64

1. 打开conda命令行，activate catalyst
2. 运行cl测试
3. 转到安装目录，
4. 最后运行
```
python setuo.py clean --all install

python setup.py build_ext --inplace --force
```

catalyst ingest-exchange -x bitfinex -f minute -s 2015 -i btc_usd

  -x, --exchange-name TEXT        The name of the exchange bundle to ingest.
  -f, --data-frequency [minute,daily|daily|daily,minute|minute]
                                  The data frequency of the desired OHLCV
                                  bars.  [default: daily]
  -s, --start DATE                The start date of the data range. (default:
                                  one year from end date)
  -e, --end DATE                  The end date of the data range. (default:
                                  today)
  -i, --include-symbols TEXT      A list of symbols to ingest (optional comma
                                  separated list)
  --exclude-symbols TEXT          A list of symbols to exclude from the
                                  ingestion (optional comma separated list)
  --csv TEXT                      The path of a CSV file containing the data.
                                  If specified, start, end, include-symbols
                                  and exclude-symbols will be ignored.
                                  Instead,all data in the file will be
                                  ingested.
  --show-progress / --no-show-progress
                                  Print progress information to the terminal.
  --verbose / --no-verbose`       Show a progress indicator for every currency
                                  pair.
  --validate / --no-validate`     Report potential anomalies found in data
                                  bundles.
  --help                          Show this message and exit.


https://github.com/enigmampc/catalyst/issues/503 Use Catalyst with a proxy


https://s3.amazonaws.com/enigmaco/catalyst-bundles/exchange-bitfinex/bitfinex-minute-btc_usd-2015-03.tar.gz

https://github.com/pandas-dev/pandas/pull/25263/files/e0e3e254a3cc95cea4a70cae5488fb1fd8367c61

pandas升级带来很多问题
```
 catalyst ingest-exchange -x bitfinex -f minute -s 2019 -i btc_usd --proxies socks5://127.0.0.1:2080 --show-progress

 catalyst ingest-exchange -x binance -f minute -s 2019 -i btc_usd --proxies socks5://127.0.0.1:2080
```
