from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    prediction_test = model.predict(X_test)
    acc = accuracy_score(y_test, prediction_test)
    report = classification_report(y_test, prediction_test)
    print(f"Accuracy: {acc}")
    print(report)

    return acc, report