# pylearning

这是一个用于学习目的的 Python 项目。

## 要求

- Python >= 3.13

## 安装

本项目使用现代 Python 工具。

```bash
# 克隆仓库
git clone <repository_url>
cd pylearning

# 安装依赖（如果有）
# 建议使用虚拟环境
python -m venv .venv
source .venv/bin/activate  # 在 Windows 上: .venv\Scripts\activate
pip install .
```

或者，如果您使用 `uv`：

```bash
uv sync
```

## 用法

运行主脚本：

```bash
python main.py
```

## 项目结构

- `main.py`: 应用程序的主要入口点。
- `pyproject.toml`: 依赖项和元数据的配置文件。
