# import streamlit as st


# def calculator(num1,num2,opr):

#     if opr=="+":
#         return num1+num2
#     elif opr=="-":
#         return num1-num2
#     elif opr=="*":
#         return num1*num2
#     else:
#         if num2!=0:
#             return num1/num2
#         else:
#             return "Division by zero is not allowed"

# def main():   
#     st.title("welcome to My Calculator...")    
#     number1=st.number_input("Enter number..",format="%2f")
#     operator=st.selectbox("Select operator",["+","-","*","/"])
#     number2=st.number_input("Enter Number..",format="%2f")

#     result=calculator(number1,number2,operator)
#     if st.button("calculate"):
#         st.success(result)

# if __name__=="__main__":
#     main()









import streamlit as st

def calculator(num1, num2, opr):
    # Perform the calculation based on the operator
    if opr == "+":
        return num1 + num2
    elif opr == "-":
        return num1 - num2
    elif opr == "*":
        return num1 * num2
    elif opr == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"

def main():
    st.title("Welcome to My Calculator")

    # User input for numbers and operator
    number1 = st.number_input("Enter first number", format="%.2f")
    operator = st.selectbox("Select operator", ["+", "-", "*", "/"])
    number2 = st.number_input("Enter second number", format="%.2f")

    # Calculate the result when the button is pressed
    if st.button("Calculate"):
        result = calculator(number1, number2, operator)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
