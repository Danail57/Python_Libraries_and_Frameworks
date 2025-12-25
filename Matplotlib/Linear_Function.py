import matplotlib.pyplot as plt

x = range(1, 50)
y = [value * 3 for value in x]
plt.figure(figsize=(10,5))
plt.plot(x, y, color = 'purple', linestyle = '--', marker = 'o', label = 'y = 3x')
plt.fill_between(x, y, alpha = 0.2)

plt.title("Linear function y = 3x", fontsize = 16)
plt.xlabel("x - values", fontsize = 12)
plt.ylabel("y - values", fontsize = 12)
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.legend()

plt.show()
