class Streamer:
    def __init__(self, nick, subscribers):
        self.nick = nick
        self.donates = []
        self.subscribers = subscribers

    def add_donate(self, amount):
        # добавляем донат в список
        self.donates.append(amount)

    def total_donates(self):
        # считаем сумму циклом for
        total = 0
        for d in self.donates:
            total += d
        return total

    def average_donate(self):
        # средний донат; если пусто — 0
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)


def print_stats(streamer):
    # печатаем карточку статистики
    print(f"Стример: {streamer.nick}")
    total = streamer.total_donates()
    avg = streamer.average_donate()
    print(f"Донатов: {len(streamer.donates)}, сумма: {total}, средний: {avg:.1f}")
    print(f"Подписчиков: {streamer.subscribers}")


def is_popular(streamer):
    # True, если подписчиков больше 1000
    return streamer.subscribers > 1000


# главная часть
s = Streamer("ShadowStorm", 1500)
s.add_donate(100)
s.add_donate(250)
s.add_donate(50)
print_stats(s)
print("Популярен:", is_popular(s))