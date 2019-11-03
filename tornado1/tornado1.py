#  coding:utf-8
 
'''Tornado 主入口'''
import tornado.web
import tornado.ioloop
 
#自定义Handler处理类型,需要传入tornado.web.RequestHandler
#RequestHandler封装对请求处理的所有信息和处理方法
class TestHandler(tornado.web.RequestHandler):
    #添加一个处理get请求方式的方法
    #封装对应的请求方式
    def get(self):
        #向响应中，添加数据,通俗来说可以理解成写的形式写进响应
        self.write('Hello,World!')
 
#运行当前文件
if __name__ == '__main__':
    #创建一个应用对象
    app = tornado.web.Application([(r'/',TestHandler)])
    #绑定一个监听端口
    app.listen(80)
#启动web程序，开始监听端口的连接
'''
tornado.ioloop：核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
current()返回当前线程的IOLoop实例对象
start()启动IOLoop实力对象的IO循环，开启监听
'''
tornado.ioloop.IOLoop.current().start()
