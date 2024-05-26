

import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Визначення змінних
Lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість лимонаду
FruitJuice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Додавання обмежень
model += 2 * Lemonade + 1 * FruitJuice <= 100  # Обмеження на воду
model += 1 * Lemonade <= 50  # Обмеження на цукор
model += 1 * Lemonade <= 30  # Обмеження на лимонний сік
model += 2 * FruitJuice <= 40  # Обмеження на фруктове пюре

# Цільова функція (максимізація кількості напоїв)
model += Lemonade + FruitJuice, "Total_Products"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Максимальна кількість лимонаду: {Lemonade.varValue}")
print(f"Максимальна кількість фруктового соку: {FruitJuice.varValue}")
print(f"Максимальна загальна кількість напоїв: {pulp.value(model.objective)}")
