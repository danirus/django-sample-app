import re


expression = re.compile(
    r'^((?P<varname>\w{1})=)?'
    r'(?P<operand1>[\-\+]?[\d\w]+)'
    r'(?P<operator>[\+\-\*\/])'
    r'(?P<operand2>[\-\+]?[\d\w]+)$')


class BadExpressionException(Exception):
    pass

class Result(object):    
    def __init__(self, expr_str):
        match_obj = expression.search(expr_str)
        if not match_obj:
            raise BadExpressionException(expr_str)
        self.varname =  match_obj.group('varname')
        self.operand1 = match_obj.group('operand1')
        self.operator = match_obj.group('operator')
        self.operand2 = match_obj.group('operand2')
        self.must_save = self.varname == None
