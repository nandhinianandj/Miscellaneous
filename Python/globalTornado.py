# https://gist.github.com/simon-weber/7755289
import tornado

class RequestContextHandler(tornado.web.RequestHandler):

    def _execute(self, transforms, *args, **kwargs):
        # following the example of:
        #  https://github.com/bdarnell/tornado_tracing/blob/master/tornado_tracing/recording.py

        global_data = {}  # add whatever here, e.g. self.request

        with tornado.stack_context.StackContext(functools.partial(ThreadRequestContext, **global_data)):
            super(RequestContextHandler, self)._execute(transforms, *args, **kwargs)

# elsewhere, use ThreadRequestContext.data => a dict


