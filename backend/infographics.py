import matplotlib.pyplot as plt

def generate_bar_chart():
    concepts = ["AI", "ML", "Data Science", "Deep Learning", "Python"]
    popularity = [80, 90, 70, 85, 95]

    plt.bar(concepts, popularity, color='skyblue')
    plt.xlabel("Concepts")
    plt.ylabel("Popularity")
    plt.title("Lecture Topics - Popularity Index")
    plt.show()

if __name__ == "__main__":
    generate_bar_chart()
