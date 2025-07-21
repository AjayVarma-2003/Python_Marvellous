import numpy as np
import math


line = "-" * 50

def EucDistance(P1, P2):
    ans = math.sqrt(((P1['x'] - P2['x']) ** 2) + ((P1['y'] - P2['y']) ** 2))

    return ans

def Result(sortdata):
    # let hyperparameter be 3. i.e k = 3
    k = 5
    nearest = sortdata[:k]

    print(line)
    print("Nearest points are : ")
    for d in nearest:
        print(d)
    print(line)

    # voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print(line)
    print("Result of voting is : ")
    for d in votes:
        print("Name : ", d, "Value :", votes[d])
    print(line)

    # Predicted class
    prediction = max(votes, key = votes.get)

    return prediction

def MarvellousKNN():
    data = [{'point' : 'A', 'x' : 1, 'y' : 2, 'label' : 'Red'},
            {'point' : 'B', 'x' : 2, 'y' : 3, 'label' : 'Red'},
            {'point' : 'C', 'x' : 3, 'y' : 1, 'label' : 'Blue'},
            {'point' : 'D', 'x' : 6, 'y' : 5, 'label' : 'Blue'},
            {'point' : 'E', 'x' : 4, 'y' : 4, 'label' : 'Blue'},
            {'point' : 'F', 'x' : 3, 'y' : 5, 'label' : 'Red'},
            {'point' : 'G', 'x' : 6, 'y' : 2, 'label' : 'Blue'},
            {'point' : 'H', 'x' : 4, 'y' : 2, 'label' : 'Blue'},
            {'point' : 'I', 'x' : 4, 'y' : 3, 'label' : 'Red'},
            {'point' : 'J', 'x' : 2, 'y' : 4, 'label' : 'Red'}]
    
    print(line)
    print("Training dataset : ")
    print(line)
    for i in data:
        print(i)
    print(line)

    new_point = {'x' : 3, 'y' : 3}

    # Calculate distance
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(line)
    print("Calculated distances are : ")
    for d in data:
        print(d)
    print(line)

    # Sort by distance
    sorted_data = sorted(data, key = lambda item: item['distance'])

    print(line)
    print("Sorted data is : ")
    for d in sorted_data:
        print(d)
    print(line)

    predicted_class = Result(sorted_data)

    print(f"Predicted class for {new_point} is : {predicted_class}")

def main():
    print("Demonstration of KNN algorithm.")
    MarvellousKNN()

if __name__ == "__main__":
    main()