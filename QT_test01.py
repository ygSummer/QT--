"""
简单图形界面QT：弹窗模式 统计薪资2W以上薪资及2W以下的人员
姓名      薪资 年龄
薛蟠     4560   25
薛蝌     4460  25
薛宝钗   35776  23
薛宝琴   14346  18
王夫人   43360  45
王熙凤   24460  25
王子腾   55660  45
王仁     15034  65
尤二姐   5324  24
贾芹     5663  25
贾兰     13443  35
贾芸     4522  25
尤三姐   5905  22
贾珍     54603  35
"""

from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QMessageBox


class Stats():

    def __init__(self):

        self.app = QApplication([])
        # 实例化主窗口
        self.window = QMainWindow()
        # 设置主窗口的长宽
        self.window.resize(550, 450)
        # 设置主窗口在屏幕中的位置
        self.window.move(350, 300)
        # 设置主窗口的题目
        self.window.setWindowTitle('薪资统计表')

        # 实例化文本框，在window中嵌入
        self.textEdit = QPlainTextEdit(self.window)
        # 文本框预显示的文本提示
        self.textEdit.setPlaceholderText("""请输入薪资表（姓名 薪资 年龄）：
        
        张三  2000  18
        李四  3000  20""")
        # 文本框的长宽及在window中的位置
        self.textEdit.resize(450, 300)
        self.textEdit.move(50, 10)

        # 实例化按钮控件 在window框上，设置位置
        button = QPushButton('统计', self.window)
        button.move(230, 360)

        # 点击按钮控件可以 连接到文本框中的信息 进行代码运算处理
        button.clicked.connect(self.handleSalary)
        self.window.show()
        self.app.exec_()

    def handleSalary(self):
        """对文本框中的信息处理，2w以上及2w以下薪资分类"""
        # 拿到文本框中用户输入的信息
        info = self.textEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        info_err = ''

        for num, line in enumerate(info.splitlines()):

            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉中间的空格列表中只存放名字，薪资，年龄
            parts = [p for p in parts if p]

            if len(parts) == 3:
                name, salary, age = parts

                if not parts[1].isdigit():
                    info_err += '第%d行  ' % num + '%-5s  ' % name  + salary + '\n' + age
                    continue

                if int(salary) >= 20000:
                    salary_above_20k += '%-5s' % name + '\t' + salary + '\n'
                else:
                    salary_below_20k += '%-5s' % name + '\t' + salary + '\n'

            else:
                QMessageBox.about(self.window, '格式错误', '请输入正确格式')
                return

        QMessageBox.about(self.window, '统计结果', f'薪资2W以上的有:\n{salary_above_20k}\n薪资2W以下的有:\n{salary_below_20k}\n '
                                               f'无法处理信息：\n{info_err}')


if __name__ == '__main__':
    stats = Stats()
