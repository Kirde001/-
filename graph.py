import matplotlib.pyplot as plt
import numpy as np

# Данные для вымышленного НПЗ в России (например, за год)
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

# Примерные данные: объем переработки нефти (в тысячах тонн)
crude_processing = np.random.randint(200, 500, size=12)

# Примерные данные: производство бензина (в тысячах тонн)
gasoline_production = np.random.randint(100, 250, size=12)

# Примерные данные: производство дизельного топлива (в тысячах тонн)
diesel_production = np.random.randint(150, 300, size=12)

# Примерные данные: объемы экспорта (в тысячах тонн)
export_volume = np.random.randint(50, 200, size=12)

# Строим график
plt.figure(figsize=(10, 6))

plt.plot(months, crude_processing, label="Переработка нефти", marker='o', linestyle='-', color='blue')
plt.plot(months, gasoline_production, label="Производство бензина", marker='s', linestyle='--', color='green')
plt.plot(months, diesel_production, label="Производство дизельного топлива", marker='^', linestyle='-.', color='red')
plt.plot(months, export_volume, label="Экспорт", marker='d', linestyle=':', color='purple')

plt.title('Статистика работы НПЗ)')
plt.xlabel('Месяцы')
plt.ylabel('Тонн (тыс.)')
plt.xticks(rotation=45)
plt.legend(loc="upper left")

plt.tight_layout()
plt.grid(True)
plt.show()
