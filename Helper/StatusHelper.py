from flask import render_template


class StatusHelper:

    def __init__(self):
        pass

    @staticmethod
    def successPage(title="操作成功", msg="成功", url="/", parent=True, timeout=5):
        return render_template("Status/status.html", title=title, message=msg, url=url, flag=True, parent=parent, timeout=timeout)

    @staticmethod
    def errorPage(title="操作出错", msg="出错", url="/", parent=True, timeout=5):
        return render_template("Status/status.html", title=title, message=msg, url=url, flag=False, parent=parent, timeout=timeout)
