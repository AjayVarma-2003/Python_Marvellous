from sklearn.metrics import confusion_matrix

def main():
    actual = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    predicted = [1, 0, 1, 0, 0, 1, 1, 1, 1, 1]

    Con_Mat = confusion_matrix(actual, predicted)

    # Tn    Fp
    # Fn    Tp

    # 2    2
    # 1    5

    # accuracy = ((Tn + Tp) / (Tn + Tp + Fn + Fp)) * 100 

    print("Confusion matrix is : ")
    print(Con_Mat)

if __name__ == "__main__":
    main()