import sys

# NOTE:把当前test_2.py存在的文件夹的上一级文件夹添加到路径搜索系统里去
sys.path.append("./")


from demo1 import test_1

test_1.print_hello()
