# __init__.py

from .plugin import ImageFormatConverter  # 导入插件的主要功能实现

def register_plugin():
    """
    插件的初始化方法，用于注册插件或执行初始化操作
    """
    print("转换图片格式 插件已加载并初始化！")
    # 你可以在这里执行任何需要在插件加载时执行的操作
    # 比如加载配置文件，设置默认值，或其他初始化操作

# 调用插件的注册函数
register_plugin()
