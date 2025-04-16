import numpy as np
import matplotlib.pyplot as plt

def sum_up(N):
    """从小到大计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从小到大求和
    # 提示: 使用循环从1加到N，每次加上1/n
    result = 0.0  # 初始化结果为0
    for n in range(1, N + 1):  # 从1到N逐项累加
        result += 1 / n  # 每次加上1/n
    return result  # 返回最终结果
    pass

def sum_down(N):
    """从大到小计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从大到小求和
    # 提示: 使用循环从N减到1，每次加上1/n
    result = 0.0  # 初始化结果为0
    for n in range(N, 0, -1):  # 从N到1逐项累加
        result += 1 / n  # 每次加上1/n
    return result  # 返回最终结果
    pass

def calculate_relative_difference(N):
    """计算两种方法的相对差异
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 相对差异值
    """
    # 学生在此实现相对差异计算
    # 提示: 使用公式 |S_up - S_down| / ((S_up + S_down)/2)
    S_up = sum_up(N)  # 从小到大求和
    S_down = sum_down(N)  # 从大到小求和
    return abs(S_up - S_down) / ((S_up + S_down) / 2)  # 计算相对差异
    pass

def plot_differences():
    """绘制相对差异随N的变化"""
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用np.logspace生成N值
    # 2. 计算每个N对应的相对差异
    # 3. 使用plt.loglog绘制双对数坐标图
    N_values = np.logspace(1, 6, 50, dtype=int)  # 生成从10到10^6的对数间隔点
    differences = [calculate_relative_difference(N) for N in N_values]  # 计算每个N的相对差异

    plt.figure(figsize=(10, 6))  # 创建图表
    plt.loglog(N_values, differences, 'o-', label="Relative Difference")  # 绘制双对数图
    plt.xlabel("Number of Terms (N)")  # 设置x轴标签
    plt.ylabel("Relative Difference")  # 设置y轴标签
    plt.title("Relative Difference vs N (Harmonic Sum)")  # 设置标题
    plt.grid(True, which="both", linestyle="--")  # 添加网格线
    plt.legend()  # 添加图例
    plt.show()  # 显示图表
    pass

def print_results():
    """打印典型N值的计算结果"""
    # 学生在此实现结果打印
    # 提示:
    # 1. 选择几个典型N值(如10,100,1000,10000)
    # 2. 计算并格式化输出两种方法的和及相对差异
    N_values = [10, 100, 1000, 10000, 100000]  # 选择几个典型的N值
    print(f"{'N':<10}{'S_up':<20}{'S_down':<20}{'Relative Difference':<20}")  # 打印表头
    print("-" * 70)  # 打印分隔线
    for N in N_values:
        S_up = sum_up(N)  # 从小到大求和
        S_down = sum_down(N)  # 从大到小求和
        diff = calculate_relative_difference(N)  # 计算相对差异
        print(f"{N:<10}{S_up:<20.10f}{S_down:<20.10f}{diff:<20.10e}")  # 格式化输出结果
    pass

def main():
    """主函数"""
    # 打印计算结果
    print_results()
    
    # 绘制误差图
    plot_differences()

if __name__ == "__main__":
    main()
