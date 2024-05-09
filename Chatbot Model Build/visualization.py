import matplotlib.pyplot as plt

class Visualization:
    def __init__(self):
        self.visualizations = []

    def display_graph(self, data, graph_type="bar", title="Graph", xlabel="X-axis", ylabel="Y-axis"):
        plt.figure(figsize=(10, 5))
        if graph_type == "bar":
            plt.bar(data.keys(), data.values())
        elif graph_type == "line":
            plt.plot(list(data.keys()), list(data.values()))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        self.visualizations.append((graph_type, data))

    def modify_graph(self, graph_type="bar"): # Allow for Bot to choose which graph would work best for each question
        print(f"Changing graph to {graph_type} type.")

    def save_graph(self, filename="graph.png"): # Create more dynamic way for Bot to name graphs
        plt.savefig(filename)
        print(f"Graph saved as {filename}.")
