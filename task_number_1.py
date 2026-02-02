import datetime

# Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між
# заданою датою і поточною датою.
def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    Якщо задана дата пізніша за поточну, результат від'ємний.
    :param date: дата у форматі 'YYYY-MM-DD'
    :return: різниця у днях
    :raise: ValueError якщо формат дати некоректний
    """

    try:
        # Перетворюємо рядок у datetime
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        # Отримуємо поточну дату
        today = datetime.date.today()

        # Різниця між датами
        delta = today - given_date

        return delta.days

    except ValueError:
        raise ValueError("Неправильний формат вхідних даних.")