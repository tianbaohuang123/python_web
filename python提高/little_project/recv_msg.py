from little_project.common import RECV_DATA_LIST
from little_project.common import HANDLE_FLAG

def recv_msg():
    """模拟接收到数据，然后添加到common模块中的列表中"""
    print("--->recv_msg")
    for i in range(5):
        RECV_DATA_LIST.append(i)

def test_recv_data():
    """测试接收到的数据"""
    print("--->test_recv_data")
    print(RECV_DATA_LIST)

def recv_msg_next():
    """已经处理完成后，再接收另外的其他数据"""
    print("--->recv_msg_next")
    if HANDLE_FLAG:
        print("---发现之前的数据已经处理完成，这里进行接收其他的数据（模拟过程...)---")
    else:
        print("---发现之前的数据未处理完，等待中...---")
