import math

# Activation functions
def ReLUX(x):
    return max(0, x)

def sigmoid(z):
    return (1 / (1 + math.exp(-z)))

def HiddenLayerCalculations(w, b, inputs):
    # Detailed multiplication steps
    print(f"\nStep 1 : Multiply inputs by weights : ")
    print(f"({w[0]} * {inputs[0]}) = ({w[0] * inputs[0]:.3f})")     # 3f means restricting number till 3 numbers after decimals
    print(f"({w[1]} * {inputs[1]}) = ({w[1] * inputs[1]:.3f})")

    # summation
    z = 0
    z = sum(w_j * x_j for w_j, x_j in zip(w, inputs)) + b
        
    print(f"\nStep 2: Add results and bias {b} : z = {z:.3f}")

    # Activation
    a = ReLUX(z)

    print(f"\nStep 3: Apply Relu: max (0, {z:.3f}) = {a:.3f}")

    return a

def OutputLayerCalculations(weights_output, hidden_outputs, bias_output):

    print("Step 1: Multiply hidden outputs by weights : ")
    print(f"({weights_output[0]} * {hidden_outputs[0]}) = ({weights_output[0]} * {hidden_outputs[0]:.3f})")
    print(f"({weights_output[1]} * {hidden_outputs[1]}) = ({weights_output[1]} * {hidden_outputs[1]:.3f})")

    z_out = 0
    z_out = sum(w_o * h for w_o, h in zip(weights_output, hidden_outputs)) + bias_output

    print(f"\nStep 2: Add results and bias {bias_output}: z = {z_out:.3f}")

    y_hat = sigmoid(z_out)

    print(f"\nStep 3: Apply sigmoid: 1 / (1 + e ^ (-({z_out:.3f}))) = {y_hat:.3f}")

    return y_hat    

def Marvellous_forward_pass(inputs):
    print("Input Layers")
    print(f"Inputs : \nx1 = {inputs[0]}, x2 = {inputs[1]}")

    # Hidden layers
    weights_hidden = [
        [0.5, -0.2],    # Neuron 1 weights
        [0.8, 0.4],    # Neuron 2 weights
    ]
    
    bias_hidden = [0.1, -0.1]    # bias for each neuron of hidden layer 1

    hidden_outputs = []

    print("\nHideen Layer")
    
    for i in range(len(weights_hidden)):
        print(f"\nNeuron {i + 1} : ")
        
        w = weights_hidden[i]
        b = bias_hidden[i]

        a = HiddenLayerCalculations(w, b, inputs)

        hidden_outputs.append(a)

    # Output layer
    weights_output = [1.0, -1.5]    # weights from hidden to output
    bias_output = 0.2

    print("\nOuput Layer")

    y_hat = OutputLayerCalculations(weights_output, hidden_outputs, bias_output)

    print(f"\nFinal Output : {y_hat:.3f} -> {y_hat * 100:.2f}% confidence in postitive class")

def main():
    inputs = [2.0, 3.0]
    Marvellous_forward_pass(inputs)

if __name__ == "__main__":
    main()