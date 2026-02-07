import random
import time

class DataLogger:
    # 1. 构造函数 (__init__)：初始化对象属性
    def __init__(self, device_name):
        self.name = device_name   # self 相当于 C++ 的 this 指针
        self.logs = []            # 初始化一个空列表存数据

    # 2. 实例方法：添加数据
    def add_entry(self, msg, level="INFO"):
        timestamp = time.strftime("%H:%M:%S")
        # 将数据存为一个元组 (Tuple)，元组是不可变的数组
        entry = (timestamp, level, msg)
        self.logs.append(entry)

    # 3. 实例方法：批量处理并保存文件
    def save_to_file(self, filename="system.log"):
        print(f"[{self.name}] 正在写入文件...")
        try:
            # 4. with open 上下文管理器：自动处理文件关闭，防止内存泄漏
            with open(filename, "w", encoding="utf-8") as f:
                for t, l, m in self.logs:
                    f.write(f"[{t}] <{l}> {m}\n")
            print("写入完成！")
        except Exception as e:
            print(f"写入出错: {e}")

    # 5. 高级用法：筛选错误日志
    def get_errors(self):
        # 列表推导式：一行代码完成遍历和筛选
        return [log for log in self.logs if log[1] == "ERROR"]

# --- 主程序 ---
if __name__ == "__main__":
    # 实例化对象
    logger = DataLogger("Sensor_Master_01")

    # 模拟产生数据
    actions = ["启动", "读取数据", "连接超时", "校准", "内存溢出"]
    for i in range(5):
        act = random.choice(actions)
        # 三元运算符：如果 act 是报错信息，等级设为 ERROR，否则 INFO
        lvl = "ERROR" if act in ["连接超时", "内存溢出"] else "INFO"
        logger.add_entry(act, lvl)

    # 调用方法
    logger.save_to_file()
    
    # 获取并打印错误
    errs = logger.get_errors()
    print(f"发现 {len(errs)} 个错误: {errs}")