"""
使用 QT 界面生成器 QT Designer
将下面的文本信息薪资分类
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


import os.path

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox,QApplication

class Stats():

    def __init__(self):

        self.app = QApplication([])

        # 加载界面生成器QT Designer 生成的文件stats.ui
        self.window=QUiLoader().load(os.path.join((os.path.dirname(__file__)),'ui\\stats.ui'))

        # 主窗口button按钮连接 主窗口文本信息 处理信息
        self.window.button.clicked.connect(self.handleCalc)

        self.window.show()

        self.app.exec_()


    def handleCalc(self):
        """对文本框中的信息处理，2w以上及2w以下薪资分类"""
        # 拿到文本框中用户输入的信息
        info = self.window.textEdit.toPlainText()

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
                    info_err += '第%d行  ' % num + '%-5s  ' % name + salary + '\n' + age
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

    stats=Stats()



