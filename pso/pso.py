#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    案例1：求解 𝑓(𝑥) = 𝑥𝑠𝑖𝑛(𝑥)𝑐𝑜𝑠(2𝑥) - 2𝑥𝑠𝑖𝑛(3𝑥) + 3𝑥𝑠𝑖𝑛(4𝑥) 在 [0, 50] 的最小值
"""
import numpy as np
from matplotlib import pyplot as plt
from numpy import sin, cos, random, min

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def show(definition: list):
    """
    画出函数图像
    :param definition: 定义域
    """
    axis_x = np.arange(definition[0], definition[1], 0.1)
    axis_y = fn(axis_x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('目标函数')
    plt.plot(axis_x, axis_y)
    plt.show()


def fn(axis_x):
    # 目标函数（同时也是适应度函数）
    return axis_x * sin(axis_x) * cos(2 * axis_x) - 2 * axis_x * sin(3 * axis_x) + 3 * axis_x * sin(4 * axis_x)


N = 20  # 初始化种群个数
generation = 100  # 最大迭代次数
x_limit = [0, 50]  # 设置位置参数限制

v_limit = [-10, 10]  # 设置速度限制
w = 0.8  # 惯性权重
c1 = 0.5  # 自我学习因子
c2 = 0.5  # 群体学习因子

# 初始化种群的位置
x = [x_limit[0] + (x_limit[1] - x_limit[0]) * random.random() for i in range(N)]
# 初始化种群的速度
v = [v_limit[0] + (v_limit[1] - v_limit[0]) * random.random() for i_1 in range(N)]
# 记录每个个体的历史最佳位置
p_best = [i for i in x]
# 记录种群最佳位置
g_best = 0
# 记录每个个体的历史最佳适应度
fitness_p_best = [float('inf') for i_2 in range(N)]
# 记录种群最佳适应度
fitness_g_best = float('inf')

print('############################### 初始化参数 ###############################')
print('初始化种群的位置: {0}'.format(x))
print(f'粒子数量：{len(x)}')
print(f'初始化粒子速度: {v}')
print(f'初始化个体历史最佳位置: {x}')
print(f'初始化种群最佳位置: {g_best}')
print(f'初始化个体历史最佳适应度: {fitness_p_best}')
print(f'初始化种群最佳适应度: {fitness_g_best}')


# 迭代
for gen in range(generation):
    for i in range(N):
        fitness = fn(x[i])  # 计算当前个体适应度
        if fitness < fitness_p_best[i]:
            fitness_p_best[i] = fitness  # 更新个体历史最佳适应度
            p_best[i] = x[i]  # 更新个体历史最佳位置

    mfb = min(fitness_p_best)
    if mfb < fitness_g_best:
        fitness_g_best = mfb  # 更新种群历史最佳适应度
        g_best = x[fitness_p_best.index(mfb)]  # 更新群体历史最佳位置

    # 更新速度和位置
    for i in range(N):
        v[i] = v[i] * w + c1 * random.random() * (p_best[i] - x[i]) + c2 * random.random() * (g_best - x[i])
        # 速度边界处理
        if v[i] > v_limit[1]:
            v[i] = v_limit[1]
        if v[i] < v_limit[0]:
            v[i] = v_limit[0]
        # 位置边界处理
        x[i] = x[i] + v[i]
        if x[i] > x_limit[1]:
            x[i] = x_limit[1]
        if x[i] < x_limit[0]:
            x[i] = x_limit[0]

print('############################### 迭代结束 ###############################')
print(f'迭代结束后所有粒子的位置: {x}')
print(f'迭代结束后所有的粒子的最佳位置: {p_best}')
print(f'迭代结束后种群最佳位置: {g_best}')

# 画图
show(x_limit)
