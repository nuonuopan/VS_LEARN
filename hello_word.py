from doctest import DocTestFailure


def hello_world():
    """hello function 
    """
    print("hello world!!")


# NOTE：为什么note不显示
# TODO: 用来标记待办的地方。常常在有些地方，我们的功能并没有实现，使用ToDo标记我们可以快速定位需要实现的部分。
# HACK: 用来标记可能需要更改的地方。在写代码的时候，有的地方我们并不确定他是正确的，可能未来有所更改，这时候可以使用HACK标记。
# NOTE: 添加一些说明文字。
# INFO: 用来表达一些信息。
# TAG: 用来创建一些标记。
# XXX: 用来标记一些草率实现的地方。在写代码的时候，有些地方需要频繁修改，这时候使用XXX标记。
# BUG: 用来标记BUG~
# FIXME: 用来标记一些需要修复的位置，可以快速定位。

if __name__ == "__main__":
    hello_world()
