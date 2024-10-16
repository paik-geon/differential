import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sympy.diffgeom import Differential

st.set_page_config(
    page_title="Differential"
)
# Streamlit 인터페이스
st.title("미분 계산 및 시각화")

# 수식입력 혹은 함수선택
option = st.radio("함수를 선택하거나 직접 수식을 입력하세요", ("함수 선택", "수식 입력"))

if option == "함수 선택":
    func_str = st.selectbox("함수 선택", ("x**2", "sin", "cos", "exp", "log"))

    # t 값 설정
    if func_str == "x**2":
        func = lambda x: x ** 2
        t_values = np.linspace(-10, 10, 500)
    elif func_str == "sin":
        func = np.sin
        t_values = np.linspace(0, 2 * np.pi, 500)
    elif func_str == "cos":
        func = np.cos
        t_values = np.linspace(0, 2 * np.pi, 500)
    elif func_str == "exp":
        func = np.exp
        t_values = np.linspace(-2, 2, 500)
    elif func_str == "log":
        func = np.log
        t_values = np.linspace(0.1, 5, 500)

elif option == "수식 입력":
    #수식을 직접 입력할 수 있도록 text_input 사용
    equation = st.text_input("수식을 입력하세요", "x^2 + 4*x - 12")

    # ^를 **로 변환
    equation = equation.replace("^", "**")

    # numpy 함수들을 사용하도록 변환
    equation = equation.replace("sin", "np.sin")
    equation = equation.replace("cos", "np.cos")
    equation = equation.replace("exp", "np.exp")
    equation = equation.replace("log", "np.log")

    # 수식을 해석하고, 입력값에 따라 함수 생성
    try:
        func = eval(f"lambda x: {equation}", {"np": np})
        t_values = np.linspace(-10, 10, 500)
    except Exception as e:
        st.error(f"수식을 해석하는 데 문제가 있습니다: {e}")
        st.stop()


# 미분 계산 함수
def calculate_derivative(func, t_values):
    y = func(t_values)
    y_d = np.gradient(y, t_values)
    return y, y_d


# 미분 계산
y, y_d = calculate_derivative(func, t_values)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(t_values, y, label=f'Input Function (y)')
ax.plot(t_values, y_d, label="Differentiable Function (y')")
ax.set_xlabel('t')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Streamlit에서 그래프 출력
st.pyplot(fig)
