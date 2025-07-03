from sklearn import tree

def main():
    BallFeatures = [[35, "rough"], [47, "rough"], [90, "smooth"], [48, "rough"], [90, "smooth"], [35, "rough"], [92, "smooth"], [35, "rough"], [35, "rough"], [35, "rough"]]
    
    BallNames = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Cricket", "Tennis", "Tennis", "Tennis"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(BallFeatures, BallNames)

    print(obj.predict([93, "smooth"]))

if __name__ == "__main__":
    main()