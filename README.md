<p align="center">
  <a href="https://github.com/WwwwwyDev/asceticism-assistant-QQ"><img src="https://s2.loli.net/2024/12/20/dwA6ZrJaGWFls89.png" alt="fantasy-world-bot4qq"></a>
</p>

<div align="center">

# 修仙小助手

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
qq修仙，支持小小、一念、汐汐、小北等bot
<!-- prettier-ignore-end -->
</div>

## 帮助

### 下载

下载最新版win可执行文件，并运行
[下载地址1](https://github.com/WwwwwyDev/asceticism-assistant-QQ/releases/download/v0.0.1/asceticism-assistant.exe) | [下载地址2](https://gitee.com/wu_wen_yi/asceticism-assistant-QQ/releases/download/v0.0.1/%E4%BF%AE%E4%BB%99%E5%B0%8F%E5%8A%A9%E6%89%8B.exe) | [百度网盘](https://pan.baidu.com/s/1Ajmu1PgfSCLVyxzF00p_PA?pwd=igb7)


### 使用教程
使用步骤：1、定位qq聊天输入框(请打开qq独立窗口) 2、点击开始执行运行脚本 \
定位检查：会对定位处颜色进行检查，避免广告等因素导致脚本错误，重叠的qq输入框无法使用此功能 \
防封：会对脚本执行进行随机延迟，模拟人的行为，会添加一定的防封策略 \
热键：ctrl+p：输入框定位， ctrl+o：终止脚本 \
智能定位：无需手动定位，软件会自动识别输入框的位置 \
常见问题：1、为什么消息无法发出？请查看您的qq输入框是否设置按enter发送消息。2、为什么热键没有反应？请查看该热键是否与别的软件冲突。3、为什么有时候会艾特错人？请确保bot在群内，并在群里手动艾特并回车，查看是否能艾特到bot，艾特不到可以尝试重启qq或者重开一下q群。


## 构建

### 配置python环境
`conda env create -f environment.yml`

### 构建可执行文件
`pyinstaller -F main.py -n 修仙小助手 -i favicon.ico --noconsole --uac-admin` 或 `sh build.sh`

## 相关支持

[tkinter布局助手](https://www.pytk.net/)\
[ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)

## 免责声明
MIT开源协议，如用作商业用途出现的纠纷与原作者无关

