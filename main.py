# Точка входа в программу, демонстрация расчётов и визуализации
from nodal_analysis import run_nodal_solver, plot_result

if __name__ == "__main__":
    # Входные параметры
    coef_productivity = 40
    p_w = 200
    p_e = 300
    time = 7

    # Выполнение расчёта
    q, p = run_nodal_solver(coef_productivity, p_w, p_e, time)

    # Визуализация результатов
    days = list(range(1, time + 1))
    q_values = [coef_productivity * (p_w - p_e) * __import__('math').exp(-0.5 * i) for i in range(time)]
    p_values = [(-coef_productivity * p_w * __import__('math').exp(-5 * i)) / coef_productivity + p_w for i in range(time)]

    plot_result(q_values, label="Дебит", ylabel="Дебит, м3/сут")
    plot_result(p_values, label="Давление", ylabel="Забойное давление, атм")
    