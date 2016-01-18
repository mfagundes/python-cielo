#coding: utf-8
from datetime import datetime


class Payment(object):

    def __init__(self, captured, option_code, form_code, total, created_at):
        self.captured = captured
        self.option_code = option_code
        self.form_code = form_code
        self.total = total
        self.created_at = created_at

