import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        #设置窗口初始位置和大小 self.setGeometry(300,50,10,10) self.setWindowTitle('StackedWidget 例子')
        # #创建列表窗口，添加条目
        self.leftlist=QListWidget()
        self.leftlist.insertItem(0,'联系方式')
        self.leftlist.insertItem(1,'个人信息')
        self.leftlist.insertItem(2,'教育程度')
        #创建三个小控件
        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        #在QStackedWidget对象中填充了三个子控件
        self.stack=QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        #水平布局，添加部件到布局中
        HBox=QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)
        self.setLayout(HBox)
        self.leftlist.currentRowChanged.connect(self.display)
    def stack1UI(self):
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        self.stack1.setLayout(layout)
    def stack2UI(self): # zhu表单布局，次水平布局
        layout = QFormLayout()
        sex = QHBoxLayout() # 水平布局添加单选按钮
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女')) # 表单布局添加控件
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())
        self.stack2.setLayout(layout)
    def stack3UI(self): # 水平布局
        layout = QHBoxLayout() # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)
    def display(self,i):
        #设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StackedExample()
    demo.show()
    sys.exit(app.exec_())
