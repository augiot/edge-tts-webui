from enum import Enum

# 创建一个名为Color的枚举类
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 使用枚举类型
favorite_color = Color.RED
print(f"我的最爱颜色是{favorite_color}。")  # 输出: 我的最爱颜色是Color.RED。

# 遍历枚举成员
for color in Color:
    print(color)  # 输出: RED, GREEN, BLUE

print(Color)
print(Color.BLUE)
print(Color.BLUE.value)