import tornado.web


class RequestHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.db_engine = kwargs.pop('db_engine')

        super().__init__(*args, **kwargs)

    async def get_db(self):
        return await self.db_engine.acquire()


class IndexHandler(RequestHandler):
    async def get(self):
        db = await self.get_db()
        self.write("Ello World")
