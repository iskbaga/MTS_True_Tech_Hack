RUSSIAN_WORD2VEC_GENSIM_PATH = "word2vec-ruscorpora-300"
RUSSIAN_WORD2VEC_LOCAL_PATH = "text_processing/models/russian_word2vec.wordvectors"

THRESHOLD = 0.65

CATEGORIES = [
    "запрос на отправку платежей",
    "запрос на отправку переводов",
    "запрос на проверку баланса",
    "запрос на озвучивание того, что есть на экране",
    "переход по кнопке",
    "вбивание инфы в поле",
]

EXAMPLES = {
    "PAY_BILLS": ["оплати электричество"
                                    "оплатить коммунальные услуги",
                                    "Оплатить счет за интернет",
                                    "перевести деньги на мобильный телефон",
                                    "сделать платеж за квартиру"],
    "PAY_MONEY": ["переведи деньги",
                                     "отправить рублей на номер +7",
                                     "перевести деньги",
                                     "перевести деньги другу на банковскую карту",
                                     "отправь по сбп",
                                     "отправить деньги в другой город",
                                     "сделать перевод на имя"],
    "CHECK_BALANCE": ["сколько денег на карте",
                                   "посмотреть счет",
                                   "сколько денег у меня",
                                   "cколько у меня осталось денег на карте",
                                   "пожалуйста укажите текущий баланс моего счета"],
    "READ_SCREEN": ["какие кнопки на странице доступны",
                                                       "что я могу сделать сейчас",
                                                       "прослушайте пожалуйста содержимое экрана",
                                                       "что находится на экране сейчас",
                                                       "озвучьте мне пожалуйста список доступных действий"],
    "GOTO_BUTTON": ["нажать кнопку отправить",
                          "перейти к оплате",
                          "кликнуть на кнопку отправить",
                          "нажать на кнопку подтвердить"],
}
