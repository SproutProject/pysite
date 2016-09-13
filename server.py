#!/usr/bin/python3

import config

import tornado.ioloop
import tornado.web
import tornado.httpserver
import redis

class DebugHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world")

if __name__ == "__main__":

  rs = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
  
  args = {
    'rs' : rs,
  }

  app = tornado.web.Application([
    # the web structure refers to 'go version' website by pzread
    #(r"/qa", , args), # RoutineQA
    #(r"/poll", , args), # RoutinePoll
    #(r"/login", , args), # RoutineLogin
    #(r"/req/getpre", , args), # RoutineReqGetPre
    #(r"/req/checkpre", , args), # RoutineReqCheckPre
    #(r"/req/checkmail", , args), # RoutineReqCheckMail
    #(r"/req/verify", , args), # RoutineReqVerify
    #(r"/req/data", , args), # RoutineReqData
    #(r"/mg", , args), # RoutineMg
    #(r"/mg/qa", , args), # RoutineMgQA
    #(r"/mg/qa_add", , args), # RoutineMgQA_Add
    #(r"/mg/poll", , args), # RoutineMgPoll
    #(r"/mg/poll_add", , args), # RoutineMgPoll_Add
    #(r"/mg/req", , args), # RoutineMgReq
    (r"/", DebugHandler),
  ], cookie_secret = config.COOKIE_SEC, autoescape = 'xhtml_escape')
  
  server = tornado.httpserver.HTTPServer(app)
  # bind server port on port 8080, and let nginx to bridge the server to the client
  server.bind(8080, address='127.0.0.1')
  # server.start(0) will run multiple process on every core
  server.start(0)
  tornado.ioloop.IOLoop.current().start()
