## task1

### Результат виконання коду:

- Максимальна кількість лимонаду: 30.0
- Максимальна кількість фруктового соку: 20.0
- Максимальна загальна кількість напоїв: 50.0

## task2

### Результат виконання коду:

- Інтеграл (Метод Монте-Карло): 2.6442953328610246
- Інтеграл (quad):  2.666666666666667      
- Абсолютна помилка:  2.960594732333751e-14

### Порівняння результатів:

**Метод Монте-Карло:**
- Метод Монте-Карло використовує випадкові точки для апроксимації значення інтеграла, тому результат може мати невелику варіацію залежно від кількості точок (N) та їх розподілу.
- Точність методу збільшується зі збільшенням кількості точок.

**Функція quad:**
- Функція quad використовує адаптивні алгоритми для числового інтегрування і надає високу точність з дуже малою абсолютною помилкою (~2.96e-14).

### Висновки:

**Точність методу Монте-Карло:**

- Результат, отриманий методом Монте-Карло, досить близький до точного значення інтеграла, отриманого функцією quad.
- Відносна похибка методу Монте-Карло в нашому випадку складає приблизно 0.84%, що є прийнятним результатом для більшості практичних застосувань.
- Відмінність у значеннях пояснюється випадковим характером методу Монте-Карло та обмеженою кількістю точок (N = 10000). Зі збільшенням N точність результату буде зростати.

**Переваги функції quad:**

- Функція quad надає точніший результат з дуже малою абсолютною помилкою.
- Використання функції quad рекомендується для задач, де необхідна висока точність інтегрування.


Метод Монте-Карло є корисним інструментом для апроксимації значень інтегралів у випадках, коли точні методи обчислення є складними або неможливими. Однак, для задач, де потрібна висока точність, використання числових методів, таких як функція quad, є кращим вибором.
