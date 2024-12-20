import pygetwindow as gw

def rgb2hex(rgbcolor):
    '''RGB转HEX
    :param rgbcolor: RGB颜色元组，Tuple[int, int, int]
    :return: str
    '''
    r, g, b = rgbcolor
    result = (r << 16) + (g << 8) + b
    return str(hex(result))[-6:]

def check_script(info):
        if "|" not in info:
             return
        check_info = info.split("|")
        if len(check_info) != 12:
            return False
        return True

def decode_script(script):
    script_list = script.split("|")
    bot = script_list[0]
    message_info = script_list[1]
    input_rate = script_list[2]
    work_interval = script_list[3]
    is_use = script_list[4]
    is_safe = script_list[5]
    window_title = script_list[6]
    x = script_list[7]
    y = script_list[8]
    pixel = script_list[9]
    is_need_postion_check = script_list[10]
    is_need_auto_position = script_list[11]
    return bot, message_info, input_rate, work_interval, is_use, is_safe, window_title, x, y, pixel, is_need_postion_check, is_need_auto_position

def encode_script(bot, message_info, input_rate, work_interval, is_use, is_safe, x, y, pixel, is_need_postion_check, is_need_auto_position, window_title):
     return "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s"%(bot, message_info, input_rate, work_interval, is_use, is_safe, window_title, x, y, pixel,is_need_postion_check, is_need_auto_position)

def check_float(num):
    num = float(num)
    if num < 0:
         raise Exception

def check_int(num):
     num = int(num)
     if num < 0:
          raise Exception

bot_name = ("小小","汐汐酱","一念成仙","小北")

def validate_activate_code(s):
  if len(s) != 32:
      return False
  for char in s:
    if not char.isalpha() and not char.isdigit():
      return False
  return True

def get_win_title_list(content):
    win_titles = gw.getAllTitles()
    res = ["未选择"]
    for t in win_titles:
        if content in t and "修仙小助手" not in t and "修仙小助手" not in t :
            res.append(t)
    return res
