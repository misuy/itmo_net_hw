import matplotlib.pyplot as plt

def plot_signal(x_list: list, y_list: list, title: str):
    plt.title(title)
    plt.grid(True)
    plt.step(x_list, y_list, where = "post", linewidth = 3)
    plt.show()