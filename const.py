# const data

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
EPS_TIME = 0.01 * SECOND

kConfPath = './data/main.conf'
kTokenPath = './data/secret'

chat_id = -1002446099140
token = ''
with open(kTokenPath) as file:
    config = file.readline()

kIvanovo2Moscow = {
    'title': '{} | Иваново -> Москва',
    'options': ['01:10', '06:24', '13:36', '19:16', 'Тык'],
}
kMoscow2Ivanovo = {
    'title': '{} | Москва -> Иваново',
    'options': ['01:56', '07:07', '14:01', '20:07', 'Тык'],
}
