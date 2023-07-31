import configparser

config = configparser.ConfigParser()
config.read('config.ini')

link = int(config['Telegram']['https://t.me/treportest'])
group_id = int(config['Telegram']['-1001824856185'])
admin_id = int(config['Telegram']['6056591125'])
sticker = int(config['Telegram']['CAACAgEAAxkBAAEJ3K5kx0JvDnWjIIWq__9YIiTH7dWszwAC6AIAAuWAwUS8QzStENdBxy8E'])


DB_HOST = config['Database']['DB_HOST']
DB_USER = config['Database']['DB_USER']
DB_PASS = config['Database']['DB_PASS']
DB_NAME = config['Database']['DB_NAME']
DB_PORT = config['Database']['DB_PORT']

user_data_dict = dict()

num_reports = 5
ban_time = 300
