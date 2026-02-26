# Financial Calculator

Учебный проект на Python для выполнения базовых финансовых расчётов.

## 📌 Возможности

Проект реализует три функции:

### 1. Простой процент
Формула:
principal * rate * time / 100

### 2. Сложный процент
Формула:
principal * (1 + rate / (100 * n)) ** (n * time)

### 3. Расчёт налога
Формула:
amount * tax_rate / 100

---

## 🧮 Использование

```python
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax,
)

print(calculate_simple_interest(1000, 10, 2))
print(calculate_compound_interest(1000, 10, 2))
print(calculate_tax(1000, 20))
