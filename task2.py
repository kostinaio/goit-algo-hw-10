
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтеграла
N = 10000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
integral_mc = (b - a) * np.mean(y_rand)

print(f"Інтеграл (Метод Монте-Карло): {integral_mc}")

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)

print("Інтеграл (quad): ", result)
print("Абсолютна помилка: ", error)

# Побудова графіка функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання випадкових точок
x_rand_all = np.random.uniform(-0.5, 2.5, N)
y_rand_all = np.random.uniform(0, max(y), N)
inside_points_x = []
inside_points_y = []
outside_points_x = []
outside_points_y = []

for i in range(N):
    if y_rand_all[i] <= f(x_rand_all[i]):
        inside_points_x.append(x_rand_all[i])
        inside_points_y.append(y_rand_all[i])
    else:
        outside_points_x.append(x_rand_all[i])
        outside_points_y.append(y_rand_all[i])

ax.scatter(inside_points_x, inside_points_y, color='blue', alpha=0.5, s=1)
ax.scatter(outside_points_x, outside_points_y, color='red', alpha=0.5, s=1)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
