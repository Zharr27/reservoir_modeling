# Модуль визуализации результатов
import matplotlib.pyplot as plt

def plot_result(values, label, ylabel):
    """
    Строит график по списку значений.
    :param values: список значений
    :param label: подпись кривой
    :param ylabel: подпись оси Y
    """
    plt.figure(figsize=(10, 5))
    plt.plot(values, marker='o', label=label)
    plt.xlabel("Время (дни)")
    plt.ylabel(ylabel)
    plt.title("Результаты моделирования")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
