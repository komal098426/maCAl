import streamlit as st
st.title("Komal's Calculator")
# Define the operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():
    st.title("Simple Calculator")

    # Get user input
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

    # Select operator
    operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/"])

    # Perform the calculation based on the operator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = sub(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    # Display the result
    st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
