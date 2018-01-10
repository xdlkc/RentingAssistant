from setuptools import setup, find_packages
setup(
    name = "spider",
    version = "0.1",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            '58zf = Spiders.spiders.58HS.py:runspider',
            'ljzf = Spiders.spiders.LJHS.py:runspider',
            'zrzf = Spiders.spiders.ZRHS.py:runspider',
            'city = Spiders.spiders.CityS.py:runspider'
        ]
    }
)