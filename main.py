import numpy as np

# 1. Створюємо двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100
array_2d = np.random.randint(1, 101, size=(3, 3))
print("1. Original 3x3 array:\n", array_2d)

# 2. Обчислюємо суму всіх елементів масиву
total_sum = np.sum(array_2d)
print("\n2. Sum of all elements:", total_sum)

# 3. Знаходимо максимальне та мінімальне значення, а також їхні індекси
max_val = np.max(array_2d)
min_val = np.min(array_2d)
max_idx = np.unravel_index(np.argmax(array_2d), array_2d.shape)
min_idx = np.unravel_index(np.argmin(array_2d), array_2d.shape)

print(f"\n3. Maximum value: {max_val}, index (row, col): ({int(max_idx[0])}, {int(max_idx[1])})")
print(f"   Minimum value: {min_val}, index (row, col): ({int(min_idx[0])}, {int(min_idx[1])})")

# 4. Відсортовуємо масив по кожному рядку
sorted_array = np.sort(array_2d, axis=1)
print("\n4. Array sorted by each row:\n", sorted_array)