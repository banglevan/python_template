from <module> import <function>
...
from config.config import config

class Example():
    def __init__(self):
        """
        class doc here
        """
        self.configurations()
        self.load_processor()
        self.load_model()

    def configurations(self):
        """
        init config here
        :return:
        """

    def load_model(self): # for dl
        """
        load model here
        :return:
        """

    def load_processor(self): # for other program
        """
        load processor here
        :return:
        """
        return #main processor

    def set_some_infor(self):
        """
        update params
        :return:
        """

    def get_some_infor(self):
        """
        get infor/meta data
        :return:
        """

    def pre_process(self, data):
        """
        data pre process here
        :return:
        """

    def post_process(self, data):
        """
        data post process here
        :param data:
        :return:
        """

    def run_on_data(self, data):
        """
        infer/main process here
        :param data:
        :return:
        """

    def transform(self, data):
        """
        program executor
        :param data:
        :return:
        """
        data = self.pre_process(data)
        data = self.run_on_data(data)
        rest = self.post_process(data)
        return rest