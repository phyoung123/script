import numpy as np  
from sklearn.metrics import r2_score

# MAE: Mean Absolute Error (平均绝对误差)， 它是衡量预测模型准确性的一种常用指标。MAE 是实际值与预测值之间绝对误差的平均值
# R^2: 决定系数，是用来衡量回归模型拟合优度的一个指标

def cal_MAE(y_true, y_pred):
	delta_y = abs(y_true - y_pred)
	n = len(y_true)
	total = np.sum(delta_y)
	MAE = total / n 
	return MAE

def cal_r2(y_true, y_pred):
    y_mean = np.mean(y_true)
    sst = np.sum((y_true - y_mean) ** 2)  # 总平方和
    sse = np.sum((y_true - y_pred) ** 2)  # 残差平方和
    r2 = 1 - (sse / sst)
    return r2

r2 = r2_score(y_true, y_pred)    # 与 cal_r2 函数等价
print("sklearn 计算 R^2:", r2)
