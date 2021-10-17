from setuptools import setup

setup(
	name='telegram_shopping_list',
	author = 'Shishir Deshpande',
	packages = ['telegram_shopping_list',],
	package_dir = {'telegram_shopping_list':'telegram_shopping_list',},
	package_data = {'telegram_shopping_list':['mappings/*.csv','sql/*.txt']},
	version='0.0.1',
	description = 'Bot to create, modify and share shopping lists directly on Telegram!',
	install_requires=[
        'python-telegram-bot>=12.7',
        'pyodbc',
    ],

)
