import numpy as np

# Definicja macierzy A1 i A2
A1 = np.array([
    [5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064],
    [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
    [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
    [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
    [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]
])

A2 = np.array([
    [5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547],
    [1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433],
    [0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185],
    [-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573],
    [0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695]
])

# Definicja wektora b
b = np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006])

# Rozwiązanie równania A1 * y = b oraz A2 * y = b
y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)

# Generowanie losowego zaburzenia Delta b o normie ||Delta b||2 ≈ 10^(-6)
np.random.seed(0)  # ustalenie ziarna dla powtarzalności wyników
delta_b = np.random.randn(5)  # losowy wektor
delta_b = delta_b / np.linalg.norm(delta_b) * 1e-6  # skalowanie do normy 10^(-6)

# Rozwiązanie równań dla zaburzonego wektora b + Delta b
b_perturbed = b + delta_b
y1_perturbed = np.linalg.solve(A1, b_perturbed)
y2_perturbed = np.linalg.solve(A2, b_perturbed)

# Obliczenie różnicy wyników
diff_y1 = np.linalg.norm(y1 - y1_perturbed)
diff_y2 = np.linalg.norm(y2 - y2_perturbed)

# Wyświetlenie wyników
print("Wyniki dla A1 * y = b:", y1)
print("Wyniki dla A2 * y = b:", y2)
print("\nWyniki dla A1 * y = b + Δb:", y1_perturbed)
print("Wyniki dla A2 * y = b + Δb:", y2_perturbed)
print("\nRóżnica wyników dla A1:", diff_y1)
print("Różnica wyników dla A2:", diff_y2)
