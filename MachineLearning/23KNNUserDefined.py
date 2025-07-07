#      A  B  C  D
# x = [1, 2, 3, 6]
# y = [2, 3, 1, 5]
#      R  R  B  B

import numpy as np
import math

def EucDistance(P1, P2):
    ans = math.sqrt(((P1['x'] - P2['x']) ** 2) + ((P1['y'] - P2['y']) ** 2))

    return ans

def MarvellousKNN():
    line = "-" * 50
    data = [{'point' : 'A', 'x' : 1, 'y' : 2, 'label' : 'Red'},
            {'point' : 'B', 'x' : 2, 'y' : 3, 'label' : 'Red'},
            {'point' : 'C', 'x' : 3, 'y' : 1, 'label' : 'Blue'},
            {'point' : 'D', 'x' : 6, 'y' : 5, 'label' : 'Blue'}]
    
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

    # k = 3
    k = 3
    nearest = sorted_data[:k]

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
    predicted_class = max(votes, key = votes.get)

    print(f"Predicted class for {new_point} is : {predicted_class}")

def main():
    print("Demonstration of KNN algorithm.")
    MarvellousKNN()

if __name__ == "__main__":
    main()