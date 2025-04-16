import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """定义测试函数 f(x) = x(x-1)
    
    参数:
        x (float): 输入值
        
    返回:
        float: 函数计算结果
    """
    return x * (x - 1)

def forward_diff(f, x, delta):
    """前向差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    return (f(x + delta) - f(x)) / delta

def central_diff(f, x, delta):
    """中心差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def analytical_derivative(x):
    """解析导数 f'(x) = 2x - 1
    
    参数:
        x (float): 求导点
        
    返回:
        float: 导数的精确值
    """
    return 2 * x - 1

def calculate_errors(x_point=1.0, custom_deltas=None):
    """计算不同步长下的误差
    
    参数:
        x_point (float): 求导点，默认为1.0
        custom_deltas (array or None): 自定义步长数组，默认为 None。
        
    返回:
        tuple: (deltas, forward_errors, central_errors)
            deltas: 步长数组
            forward_errors: 前向差分误差数组
            central_errors: 中心差分误差数组
    """
    if custom_deltas is None:
        deltas = np.logspace(-10, -1, 50)  # 默认生成步长数组
    else:
        deltas = np.array(custom_deltas)  # 使用自定义步长数组

    exact_value = analytical_derivative(x_point)  # 解析导数值

    forward_errors = []
    central_errors = []

    for delta in deltas:
        forward_approx = forward_diff(f, x_point, delta)
        central_approx = central_diff(f, x_point, delta)

        forward_errors.append(abs(forward_approx - exact_value) / abs(exact_value))
        central_errors.append(abs(central_approx - exact_value) / abs(exact_value))

    return deltas, np.array(forward_errors), np.array(central_errors)

def plot_errors(deltas, forward_errors, central_errors):
    """绘制误差-步长关系图
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    plt.figure(figsize=(10, 6))
    plt.loglog(deltas, forward_errors, label="Forward Difference", marker="o")
    plt.loglog(deltas, central_errors, label="Central Difference", marker="s")

    # 添加参考线
    plt.loglog(deltas, deltas, 'k--', label="O(Δx)")
    plt.loglog(deltas, deltas**2, 'r--', label="O(Δx²)")

    plt.xlabel("Step Size Δx")
    plt.ylabel("Relative Error")
    plt.title("Error vs Step Size in Numerical Differentiation")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

def print_results(deltas, forward_errors, central_errors):
    """打印计算结果表格
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    print(f"{'步长 Δx':<15}{'前向差分误差':<20}{'中心差分误差':<20}")
    print("-" * 55)
    for delta, f_err, c_err in zip(deltas, forward_errors, central_errors):
        print(f"{delta:<15.2e}{f_err:<20.6e}{c_err:<20.6e}")

def main():
    """主函数"""
    x_point = 1.0  # 求导点

    # 自定义步长数组
    custom_deltas = [10**-2, 10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]

    # 计算误差
    deltas, forward_errors, central_errors = calculate_errors(x_point, custom_deltas)

    # 打印结果
    print(f"函数 f(x) = x(x-1) 在 x = {x_point} 处的解析导数值: {analytical_derivative(x_point)}")
    print_results(deltas, forward_errors, central_errors)

    # 绘制误差图
    plot_errors(deltas, forward_errors, central_errors)

    # 最优步长分析
    forward_best_idx = np.argmin(forward_errors)
    central_best_idx = np.argmin(central_errors)

    print("\n最优步长分析:")
    print(f"前向差分最优步长: {deltas[forward_best_idx]:.2e}, 相对误差: {forward_errors[forward_best_idx]:.6e}")
    print(f"中心差分最优步长: {deltas[central_best_idx]:.2e}, 相对误差: {central_errors[central_best_idx]:.6e}")

    # 收敛阶数分析
    mid_idx = len(deltas) // 2
    forward_slope = np.log(forward_errors[mid_idx] / forward_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    central_slope = np.log(central_errors[mid_idx] / central_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])

    print("\n收敛阶数分析:")
    print(f"前向差分收敛阶数约为: {forward_slope:.2f}")
    print(f"中心差分收敛阶数约为: {central_slope:.2f}")

if __name__ == "__main__":
    main()
