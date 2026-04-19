from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def train_knn(X_train, X_test, y_train, y_test, k_range=range(1, 21), plot=True):
    accuracies = []

    # Step 1: Try different K values
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k,
                                    # weights='distance',   # try 'uniform' vs 'distance'
                                    # metric='minkowski',   # try 'euclidean', 'manhattan'
                                    # p=2                   # 1 = Manhattan, 2 = Euclidean
                                        )
        model.fit(X_train, y_train)
        acc = model.score(X_test, y_test)
        accuracies.append(acc)

    # Step 2: Find best K
    best_k = k_range[accuracies.index(max(accuracies))]

    # Step 3: Train final model with best K
    best_model = KNeighborsClassifier(n_neighbors=best_k)
    best_model.fit(X_train, y_train)

    print(f"Best K: {best_k}")
    print(f"Best Accuracy: {max(accuracies):.4f}")

    # Step 4: Plot (optional but great for portfolio)
    if plot:
        plt.plot(k_range, accuracies, marker='o')
        plt.axvline(x=best_k, linestyle='--', label=f'Best K = {best_k}')
        plt.title("K vs Accuracy")
        plt.xlabel("K")
        plt.ylabel("Accuracy")
        plt.legend()
        plt.show()

    return best_model, best_k, accuracies

def train_logistic(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)
    return model