import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import sympy as sp

# 定义符号变量
t = sp.symbols('t')


def plot_vector_function(x_expr, y_expr, t_max):
    try:
        # 将字符串转换成数学表达式
        x_func = sp.lambdify(t, sp.sympify(x_expr), 'numpy')
        y_func = sp.lambdify(t, sp.sympify(y_expr), 'numpy')

        # 生成采样点
        t_vals = np.linspace(0, t_max, 500)

        # 计算坐标
        x_vals = x_func(t_vals)
        y_vals = y_func(t_vals)

        # 创建图形
        fig, ax = plt.subplots(figsize=(6, 6))

        # 设置坐标范围
        ax.set_xlim(np.min(x_vals) - 1, np.max(x_vals) + 1)
        ax.set_ylim(np.min(y_vals) - 1, np.max(y_vals) + 1)

        # 保持 x、y 比例相同
        ax.set_aspect('equal')

        # 网格
        ax.grid(True)

        # x、y 轴
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        # 绘制完整轨迹
        ax.plot(
            x_vals,
            y_vals,
            color='lightblue',
            linewidth=1,
            label='轨迹'
        )

        # t = 0 时的位置
        x0 = x_func(0)
        y0 = y_func(0)

        # 绘制初始向量
        vector = ax.quiver(
            0, 0,
            x0, y0,
            angles='xy',
            scale_units='xy',
            scale=1,
            color='red',
            width=0.02
        )

        # 当前点
        point, = ax.plot(
            [x0],
            [y0],
            'ro'
        )

        # 更新函数
        def update(t_value):
            x = x_func(t_value)
            y = y_func(t_value)

            # 更新向量
            vector.set_UVC(x, y)

            # 更新点
            point.set_data([x], [y])

            # 更新标题
            ax.set_title(
                f"t = {t_value:.2f}   "
                f"位置 = ({x:.2f}, {y:.2f})"
            )

            fig.canvas.draw_idle()

        # 创建滑块
        interact(
            update,
            t_value=FloatSlider(
                min=0,
                max=t_max,
                step=t_max / 100,
                value=0,
                description='参数 t'
            )
        )

        plt.legend()
        plt.show()

    except Exception as e:
        print("输入的数学表达式有错误！")
        print("错误信息：", e)


# ==========================
# 用户输入区域
# ==========================

print("===== 参数方程向量可视化 =====")
print("请输入数学表达式，例如：")
print("  cos(t)")
print("  sin(t)")
print("  t")
print("  t**2")
print()

x_expr = input("请输入 x(t)：")
y_expr = input("请输入 y(t)：")

t_max = float(input("请输入 t 的最大值："))

# 开始绘图
plot_vector_function(x_expr, y_expr, t_max)