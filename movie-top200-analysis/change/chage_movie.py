import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 全局配置
# =========================

def set_plot_style():
    """设置 Matplotlib 图表样式"""

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 解决负号显示问题
    plt.rcParams['axes.unicode_minus'] = False


# =========================
# 数据读取与清洗
# =========================

def load_data(file_path):
    """
    加载电影数据

    参数：
        file_path: CSV 文件路径

    返回：
        pandas.DataFrame
    """

    columns = [
        '电影名',
        '电影年份',
        '电影数据',
        '电影标签',
        '电影时长',
        '电影评分',
        '电影语言'
    ]

    data = pd.read_csv(
        file_path,
        usecols=columns
    )

    return data


def clean_data(data):
    """
    清洗电影数据
    """

    # 去除年份两边的括号
    data['电影年份'] = (
        data['电影年份']
        .astype(str)
        .str.strip('()')
    )

    # 转换年份数据类型
    data['电影年份'] = data['电影年份'].astype(int)

    return data


# =========================
# 图表1：年份统计
# =========================

def plot_year_count(ax, data):
    """
    绘制每年电影数量变化折线图
    """

    # 按年份统计电影数量
    year_count = (
        data.groupby('电影年份')['电影年份']
        .count()
    )

    # 获取最小年份和最大年份
    min_year = year_count.index.min()
    max_year = year_count.index.max()

    # 创建完整年份
    years = range(min_year, max_year + 1)

    # 补充没有电影的年份
    year_count = year_count.reindex(
        years,
        fill_value=0
    )

    # 绘制折线图
    ax.plot(
        year_count.index,
        year_count.values,
        marker='o'
    )

    # 设置标题
    ax.set_title(
        '每年电影数量变化折线图',
        fontsize=15
    )

    # 设置坐标轴
    ax.set_xlabel(
        '年份',
        fontsize=12
    )

    ax.set_ylabel(
        '电影数量',
        fontsize=12
    )

    # 设置 X 轴刻度
    ax.set_xticks(
        year_count.index[::8]
    )

    # 设置网格
    ax.grid(alpha=0.5)


# =========================
# 图表2：电影语言统计
# =========================

def plot_language_count(ax, data):
    """
    绘制电影语言分布柱状图
    """

    # 按语言统计电影数量
    language_count = (
        data['电影语言']
        .value_counts()
    )

    # 绘制柱状图
    ax.bar(
        language_count.index,
        language_count.values
    )

    # 设置标题
    ax.set_title(
        '电影语言分布柱状图',
        fontsize=15
    )

    # 设置坐标轴
    ax.set_xlabel(
        '语言',
        fontsize=12
    )

    ax.set_ylabel(
        '电影数量',
        fontsize=12
    )

    # 旋转 X 轴文字
    ax.tick_params(
        axis='x',
        rotation=45
    )

    # 添加网格
    ax.grid(alpha=0.5)


# =========================
# 图表3：电影类型统计
# =========================

def plot_type_count(ax, data):
    """
    绘制电影类型分布柱状图
    """

    # 分割类型
    type_count = (
        data['电影标签']
        .str.split(',')
        .explode()
        .str.strip()
        .value_counts()
    )

    # 绘制柱状图
    ax.bar(
        type_count.index,
        type_count.values
    )

    # 设置标题
    ax.set_title(
        '电影类型分布柱状图',
        fontsize=15
    )

    # 设置坐标轴
    ax.set_xlabel(
        '类型',
        fontsize=12
    )

    ax.set_ylabel(
        '电影数量',
        fontsize=12
    )

    # 旋转 X 轴文字
    ax.tick_params(
        axis='x',
        rotation=45
    )

    # 添加网格
    ax.grid(alpha=0.5)


# =========================
# 图表4：电影评分统计
# =========================

def plot_score_distribution(ax, data):
    """
    绘制电影评分占比饼图
    """

    # 统计评分数量
    score_count = (
        data['电影评分']
        .value_counts()
        .sort_index()
    )

    # 绘制饼图
    ax.pie(
        score_count.values,
        labels=score_count.index,
        autopct='%1.1f%%'
    )

    # 设置标题
    ax.set_title(
        '电影评分占比饼图',
        fontsize=15
    )

    # 保证饼图是圆形
    ax.axis('equal')

    # 图例
    ax.legend(
        loc='lower center',
        ncol=4,
        bbox_to_anchor=(0.5, -0.3),
        fontsize=10
    )


# =========================
# 创建图表
# =========================

def create_figure():
    """
    创建 2×2 子图
    """

    fig, axes = plt.subplots(
        nrows=2,
        ncols=2,
        figsize=(20, 12)
    )

    # 调整子图间距
    fig.subplots_adjust(
        hspace=0.3,
        wspace=0.2
    )

    # 设置总标题
    fig.suptitle(
        '电影Top300榜单数据统计',
        fontsize=23,
        x=0.5,
        y=0.93
    )

    return fig, axes


# =========================
# 主程序
# =========================

def main():

    # 设置图表样式
    set_plot_style()

    # 加载数据
    data = load_data(
        './movie_list.csv'
    )

    # 清洗数据
    data = clean_data(data)

    # 创建图表
    fig, axes = create_figure()

    # 绘制四张图

    plot_year_count(
        axes[0][0],
        data
    )

    plot_language_count(
        axes[0][1],
        data
    )

    plot_type_count(
        axes[1][0],
        data
    )

    plot_score_distribution(
        axes[1][1],
        data
    )

    # 自动调整布局
    plt.tight_layout()

    # 保存图片
    plt.savefig(
        'movie_top300_analysis.png',
        dpi=300,
        bbox_inches='tight'
    )

    # 展示图表
    plt.show()


# =========================
# 程序入口
# =========================

if __name__ == '__main__':
    main()