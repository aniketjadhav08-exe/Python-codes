# ============================================================
# DEEP LEARNING ASSIGNMENT
# LOAN DEFAULT PREDICTION USING MULTI-LAYER PERCEPTRON
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

def load_dataset(filename):
    df = pd.read_csv(filename)

    print("\nDataset Loaded Successfully")
    print("Shape:", df.shape)

    return df


# ============================================================
# 2. UNDERSTAND DATASET
# ============================================================

def understand_dataset(df):

    print("\n========== FIRST 5 RECORDS ==========")
    print(df.head())

    print("\n========== DATASET INFORMATION ==========")
    print(df.info())

    print("\n========== STATISTICAL SUMMARY ==========")
    print(df.describe())

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)


# ============================================================
# 3. EXPLORATORY DATA ANALYSIS
# ============================================================

def exploratory_analysis(df):

    print("\n========== EXPLORATORY DATA ANALYSIS ==========")

    print("\nNumber of Rows:", df.shape[0])
    print("Number of Columns:", df.shape[1])

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nUnique Values:")
    for column in df.columns:
        print(column, ":", df[column].nunique())


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

def check_missing_values(df):

    print("\n========== MISSING VALUES ==========")

    missing = df.isnull().sum()

    print(missing)

    print("\nTotal Missing Values:", missing.sum())

    if missing.sum() == 0:
        print("No missing values found.")
    else:
        print("Missing values are present.")


# ============================================================
# 5. CHECK CLASS BALANCE
# ============================================================

def check_class_balance(df):

    print("\n========== TARGET CLASS BALANCE ==========")

    counts = df["Default"].value_counts()

    print("\nClass Counts:")
    print(counts)

    print("\nClass Percentages:")
    print(df["Default"].value_counts(normalize=True) * 100)

    if abs(counts.iloc[0] - counts.iloc[1]) > 0:
        print("\nConclusion: Target classes are imbalanced.")
        print("Stratified splitting should be used.")
    else:
        print("\nConclusion: Target classes are balanced.")

    # Plot
    plt.figure(figsize=(6, 4))

    counts.plot(kind="bar")

    plt.title("Loan Default Distribution")
    plt.xlabel("Default")
    plt.ylabel("Number of Applicants")
    plt.xticks(rotation=0)

    plt.show()


# ============================================================
# 6. ENCODE CATEGORICAL VARIABLES
# ============================================================

def encode_categorical_variables(X):

    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns

    print("\n========== CATEGORICAL VARIABLES ==========")
    print(categorical_columns.tolist())

    X = pd.get_dummies(
        X,
        columns=categorical_columns,
        drop_first=True
    )

    X = X.astype(float)

    print("\nCategorical variables encoded successfully.")

    return X


# ============================================================
# 7. SEPARATE X AND Y
# ============================================================

def separate_features_target(df):

    X = df.drop("Default", axis=1)
    y = df["Default"]

    print("\n========== FEATURES AND TARGET ==========")

    print("X Shape:", X.shape)
    print("Y Shape:", y.shape)

    return X, y


# ============================================================
# 8. TRAIN TEST SPLIT
# ============================================================

def split_data(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\n========== TRAIN TEST SPLIT ==========")

    print("Training Data:", X_train.shape)
    print("Testing Data:", X_test.shape)

    print("\nTraining Class Distribution:")
    print(y_train.value_counts(normalize=True))

    print("\nTesting Class Distribution:")
    print(y_test.value_counts(normalize=True))

    print("\nStratified splitting used.")

    return X_train, X_test, y_train, y_test


# ============================================================
# 9. SCALE FEATURES
# ============================================================

def scale_features(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print("\n========== FEATURE SCALING ==========")
    print("Features scaled using StandardScaler.")

    return X_train_scaled, X_test_scaled, scaler


# ============================================================
# 10. CREATE MLP MODEL
# ============================================================

def create_model(
    hidden_layers=(32, 16),
    activation="relu",
    learning_rate=0.001
):

    model = MLPClassifier(
        hidden_layer_sizes=hidden_layers,
        activation=activation,
        solver="adam",
        learning_rate_init=learning_rate,
        max_iter=2000,
        random_state=42
    )

    return model


# ============================================================
# 11. TRAIN MODEL
# ============================================================

def train_model(model, X_train, y_train):

    print("\n========== MODEL TRAINING ==========")

    model.fit(X_train, y_train)

    print("Model trained successfully.")

    return model


# ============================================================
# 12. PREDICT
# ============================================================

def make_predictions(model, X_test):

    y_pred = model.predict(X_test)

    return y_pred


# ============================================================
# 13. EVALUATE MODEL
# ============================================================

def evaluate_model(y_test, y_pred):

    print("\n========== MODEL EVALUATION ==========")

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    print("\nAccuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

    print("\nAccuracy Percentage:",
          round(accuracy * 100, 2), "%")

    return accuracy, precision, recall, f1


# ============================================================
# 14. CONFUSION MATRIX
# ============================================================

def show_confusion_matrix(y_test, y_pred):

    cm = confusion_matrix(y_test, y_pred)

    print("\n========== CONFUSION MATRIX ==========")
    print(cm)

    plt.figure(figsize=(6, 5))

    plt.imshow(cm)

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.xticks(
        [0, 1],
        ["Low Risk", "High Risk"]
    )

    plt.yticks(
        [0, 1],
        ["Low Risk", "High Risk"]
    )

    for i in range(2):
        for j in range(2):
            plt.text(
                j,
                i,
                cm[i, j],
                ha="center",
                va="center"
            )

    plt.colorbar()
    plt.show()


# ============================================================
# 15. CLASSIFICATION REPORT
# ============================================================

def show_classification_report(y_test, y_pred):

    print("\n========== CLASSIFICATION REPORT ==========")

    report = classification_report(
        y_test,
        y_pred,
        target_names=[
            "Low Default Risk",
            "High Default Risk"
        ],
        zero_division=0
    )

    print(report)


# ============================================================
# 16. PLOT TRAINING LOSS
# ============================================================

def plot_training_loss(model):

    print("\n========== TRAINING LOSS ==========")

    plt.figure(figsize=(8, 5))

    plt.plot(model.loss_curve_)

    plt.title("MLP Training Loss")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.grid()

    plt.show()


# ============================================================
# 17. NEW APPLICANT PREDICTION
# ============================================================

def predict_new_applicant(
    model,
    scaler,
    X_train,
    categorical_columns
):

    print("\n========== NEW LOAN APPLICANT ==========")

    new_applicant = pd.DataFrame({
        "Age": [35],
        "Income": [600000],
        "LoanAmount": [300000],
        "CreditScore": [700],
        "EmploymentYears": [8],
        "ExistingLoans": [1],
        "MonthlyDebt": [15000],
        "LoanTerm": [36],
        "PreviousDefault": ["No"],
        "HomeOwnership": ["Own"]
    })

    new_applicant = pd.get_dummies(
        new_applicant,
        columns=categorical_columns,
        drop_first=True
    )

    new_applicant = new_applicant.reindex(
        columns=X_train.columns,
        fill_value=0
    )

    new_applicant = new_applicant.astype(float)

    new_applicant_scaled = scaler.transform(
        new_applicant
    )

    prediction = model.predict(
        new_applicant_scaled
    )

    probability = model.predict_proba(
        new_applicant_scaled
    )

    print("\nPrediction:", prediction[0])

    print(
        "Low Risk Probability:",
        round(probability[0][0] * 100, 2),
        "%"
    )

    print(
        "High Risk Probability:",
        round(probability[0][1] * 100, 2),
        "%"
    )

    if prediction[0] == 1:
        print("\nRESULT: HIGH DEFAULT RISK")
    else:
        print("\nRESULT: LOW DEFAULT RISK")


# ============================================================
# 18. EXPERIMENT 1 - ACTIVATION FUNCTION
# ============================================================

def activation_experiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    print("\n========== EXPERIMENT 1 ==========")
    print("ACTIVATION FUNCTION")

    activations = [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]

    results = []

    for activation in activations:

        model = create_model(
            hidden_layers=(32, 16),
            activation=activation
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        results.append(
            [activation, accuracy]
        )

    result_df = pd.DataFrame(
        results,
        columns=["Activation", "Accuracy"]
    )

    print("\n", result_df)

    plt.figure(figsize=(8, 5))

    plt.bar(
        result_df["Activation"],
        result_df["Accuracy"]
    )

    plt.title("Activation Function Comparison")
    plt.xlabel("Activation")
    plt.ylabel("Accuracy")

    plt.show()

    return result_df


# ============================================================
# 19. EXPERIMENT 2 - HIDDEN LAYERS
# ============================================================

def hidden_layer_experiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    print("\n========== EXPERIMENT 2 ==========")
    print("HIDDEN LAYERS")

    hidden_layers = [
        (10,),
        (20, 10),
        (50, 25),
        (100, 50, 25)
    ]

    results = []

    for layers in hidden_layers:

        model = create_model(
            hidden_layers=layers,
            activation="relu"
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        results.append(
            [str(layers), accuracy]
        )

    result_df = pd.DataFrame(
        results,
        columns=["Hidden Layers", "Accuracy"]
    )

    print("\n", result_df)

    plt.figure(figsize=(10, 5))

    plt.bar(
        result_df["Hidden Layers"],
        result_df["Accuracy"]
    )

    plt.title("Hidden Layer Comparison")
    plt.xlabel("Hidden Layers")
    plt.ylabel("Accuracy")

    plt.show()

    return result_df


# ============================================================
# 20. EXPERIMENT 3 - LEARNING RATE
# ============================================================

def learning_rate_experiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    print("\n========== EXPERIMENT 3 ==========")
    print("LEARNING RATE")

    learning_rates = [
        0.0001,
        0.001,
        0.01
    ]

    results = []

    for rate in learning_rates:

        model = create_model(
            hidden_layers=(32, 16),
            activation="relu",
            learning_rate=rate
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        results.append(
            [rate, accuracy]
        )

    result_df = pd.DataFrame(
        results,
        columns=["Learning Rate", "Accuracy"]
    )

    print("\n", result_df)

    plt.figure(figsize=(8, 5))

    plt.plot(
        result_df["Learning Rate"],
        result_df["Accuracy"],
        marker="o"
    )

    plt.title("Learning Rate Comparison")
    plt.xlabel("Learning Rate")
    plt.ylabel("Accuracy")

    plt.grid()

    plt.show()

    return result_df


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print("=" * 60)
    print("LOAN DEFAULT PREDICTION")
    print("DEEP LEARNING PROJECT")
    print("=" * 60)

    # 1. Load dataset
    df = load_dataset("Loan_Default.csv")

    # 2. Understand dataset
    understand_dataset(df)

    # 3. Exploratory analysis
    exploratory_analysis(df)

    # 4. Missing values
    check_missing_values(df)

    # 5. Class balance
    check_class_balance(df)

    # 6. Separate X and y
    X, y = separate_features_target(df)

    # Store categorical columns
    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # 7. Encode categorical variables
    X = encode_categorical_variables(X)

    # 8. Train-test split
    X_train, X_test, y_train, y_test = split_data(
        X,
        y
    )

    # 9. Feature scaling
    X_train_scaled, X_test_scaled, scaler = scale_features(
        X_train,
        X_test
    )

    # 10. Create model
    model = create_model(
        hidden_layers=(32, 16),
        activation="relu",
        learning_rate=0.001
    )

    # 11. Train model
    model = train_model(
        model,
        X_train_scaled,
        y_train
    )

    # 12. Prediction
    y_pred = make_predictions(
        model,
        X_test_scaled
    )

    # 13. Evaluation
    evaluate_model(
        y_test,
        y_pred
    )

    # 14. Confusion matrix
    show_confusion_matrix(
        y_test,
        y_pred
    )

    # 15. Classification report
    show_classification_report(
        y_test,
        y_pred
    )

    # 16. Training loss
    plot_training_loss(model)

    # 17. New applicant
    predict_new_applicant(
        model,
        scaler,
        X_train,
        categorical_columns
    )

    # 18. Activation experiment
    activation_experiment(
        X_train_scaled,
        X_test_scaled,
        y_train,
        y_test
    )

    # 19. Hidden layer experiment
    hidden_layer_experiment(
        X_train_scaled,
        X_test_scaled,
        y_train,
        y_test
    )

    # 20. Learning rate experiment
    learning_rate_experiment(
        X_train_scaled,
        X_test_scaled,
        y_train,
        y_test
    )

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
