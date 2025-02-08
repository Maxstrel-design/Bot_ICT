from keys import api_key, api_secret # Importing the API keys from keys.py
import ccxt

# Создаем объект MEXC для фьючерсного аккаунта
mexc = ccxt.mexc({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',  # Указываем, что работаем с фьючерсами
    },
})

# Функция для получения фьючерсного баланса в USDT
def get_futures_balance():
    try:
        # Делаем запрос к API для получения баланса фьючерсного счета
        balance = mexc.private_get('/api/v2/private/futures/asset')

        # Ищем значение баланса для USDT
        usdt_balance = balance['data'].get('USDT', {}).get('total', 0)
        return usdt_balance
    except ccxt.BaseError as e:
        print(f"Ошибка при получении баланса: {e}")
        return None

# Печатаем баланс
usdt_balance = get_futures_balance()
if usdt_balance is not None:
    print(f"Ваш фьючерсный баланс в USDT: {usdt_balance}")
else:
    print("Не удалось получить баланс.")












