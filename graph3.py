# Данные для графика работы оборудования на НПЗ
import matplotlib.pyplot as plt
import numpy as np

equipment = [
    "Колонны перегонки",
    "Реакторы крекинга",
    "Гидроочистка",
    "Компрессоры и насосы",
    "Теплообменники",
    "Системы водоочистки"
]

# Показатели оборудования (в условных единицах)
efficiency = [85, 80, 75, 90, 88, 95]  # Эффективность использования (%)
modernization_need = [300, 400, 500, 200, 300, 100]  # Необходимость модернизации (оценка: 1 - низкая, 5 - высокая)
emissions = [120, 100, 110, 70, 60, 30]  # Выбросы (в условных ед.)
performance = [1000, 850, 900, 950, 880, 700]  # Производительность (тонны/час)

x = np.arange(len(equipment))  # Позиции для графиков

# Создаем график
fig, ax1 = plt.subplots(figsize=(12, 6))

# График 1: Производительность
ax1.bar(x - 0.3, performance, width=0.3, label='Производительность (тонны/час)', color='skyblue')
ax1.set_ylabel('Производительность (тонны/час)', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# График 2: Эффективность
ax2 = ax1.twinx()
ax2.plot(x, efficiency, label='Эффективность (%)', color='green', marker='o', linewidth=2)
ax2.set_ylabel('Эффективность (%)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# График 3: Выбросы
ax1.bar(x, emissions, width=0.3, label='Выбросы (условные ед.)', color='orange', alpha=0.7)

# График 4: Необходимость модернизации
ax1.bar(x + 0.3, modernization_need, width=0.3, label='Модернизация (оценка): 100 - наименее необходимо, 500 - наиболее', color='red', alpha=0.5)

# Оформление
ax1.set_xticks(x)
ax1.set_xticklabels(equipment, rotation=45, ha='right')
fig.suptitle("Показатели работы оборудования НПЗ")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
