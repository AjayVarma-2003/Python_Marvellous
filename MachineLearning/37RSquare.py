from sklearn.metrics import r2_score

def main():
    y_actual = [100, 200, 300, 400, 500]
    y_predicted = [110, 190, 310, 390, 510]

    R2 = r2_score(y_actual, y_predicted)

    print("Actual values are : ", y_actual)
    print("Predicted values are : ", y_predicted)
    print("R-square value is : ", R2)

if __name__ == "__main__":
    main()