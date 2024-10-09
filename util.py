import pygetwindow as gw

def rgb2hex(rgbcolor):
    '''RGB转HEX
    :param rgbcolor: RGB颜色元组，Tuple[int, int, int]
    :return: str
    '''
    r, g, b = rgbcolor
    result = (r << 16) + (g << 8) + b
    return str(hex(result))[-6:]

bot_name = ("小小","汐汐酱","一念成仙","小北")

def check_script(info):
        if "|" not in info:
             return 
        check_info = info.split("|")
        if len(check_info) != 12:
            return False
        return True

def check_float(num):
    num = float(num)
    if num < 0:
         raise Exception

def check_int(num):
     num = int(num)
     if num < 0:
          raise Exception


def get_win_title_list(content):
    win_titles = gw.getAllTitles()
    res = ["未选择"]
    for t in win_titles:
        if content in t and "修仙小助手" not in t:
            res.append(t)
    return res
