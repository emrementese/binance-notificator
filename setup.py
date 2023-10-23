from setuptools import setup, find_packages

NAME = "binance-ema"
DESCRIPTION = ("Get crypto coin informations & calculate the custom or constant indicators. (WITH BINANCE API)")
AUTHOR = "Emre MENTESE"
URL = "https://github.com/emrementese/binance-notificator"
VERSION = "0.0.1"
URLS = {
  'MyWebsite': 'https://emrementese.github.io/',
  'Github': 'https://github.com/emrementese',
  'Source': 'https://github.com/emrementese/binance-notificator',
  'Download': 'https://github.com/emrementese/binance-notificator/#files',
}

setup(
    name = 'src',
    packages = find_packages(),
)