# Re-importing required libraries after reset
import matplotlib.pyplot as plt
import numpy as np

# Подразделения НПЗ
units = [
    "Первичная переработка нефти",
    "Каталитический крекинг",
    "Гидроочистка",
    "Риформинг",
    "Смазочные материалы",
    "Утилизация и водоочистка",
    "Контроль качества",
    "Термическое коксование"
]

# Примерные данные по каждому подразделению (в условных единицах)
production = [1000, 800, 700, 600, 300, 400, 200, 500]  # Производительность (в тоннах)
efficiency = [90, 85, 80, 75, 60, 70, 95, 65]  # Эффективность (в %)
emissions = [100, 150, 120, 90, 50, 30, 10, 70]  # Выбросы (в условных единицах)

x = np.arange(len(units))  # Позиции для графиков

# Создаем график
fig, ax1 = plt.subplots(figsize=(12, 6))

# График 1: Производительность
ax1.bar(x - 0.2, production, width=0.4, label='Производительность (тонны)', color='skyblue')
ax1.set_ylabel('Производительность (тонны)', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# График 2: Эффективность
ax2 = ax1.twinx()
ax2.plot(x, efficiency, label='Эффективность (%)', color='green', marker='o', linewidth=2)
ax2.set_ylabel('Эффективность (%)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# График 3: Выбросы
ax1.bar(x + 0.2, emissions, width=0.4, label='Выбросы (условные ед.)', color='orange', alpha=0.7)

# Оформление
ax1.set_xticks(x)
ax1.set_xticklabels(units, rotation=45, ha='right')
fig.suptitle("Показатели работы подразделений НПЗ")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
