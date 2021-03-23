# Slow-HTTP-Attacker

将三种 slow HTTP 攻击简单地移植到了 python 上，包括 Header 型、POST 型、Read 型。【目前 Read 型正在开发中】

参考 repo：

* slowhttptest：参考该仓库功能进行开发，https://github.com/shekyan/slowhttptest
* slowloris：Header 型，为 python 代码，以该代码为基础开发，https://github.com/gkbrk/slowloris

## 运行

直接 `python main.py <host>` 即可使用 Header 型攻击以默认配置攻击 host 的 80 端口。

详细使用说明如下：

```
usage: main.py [-h] [-m MODE] [-p PORT] [-s SOCKETS] [-v] [-ua] [--https]
               [--sleeptime SLEEPTIME]
               [host]

Slow HTTP Attacker, a tool providing three types of slow HTTP attack.

positional arguments:
  host                  Host to perform stress test on

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Mode of attack. The supported options are "header",
                        "post" and "read". Use "header" by default
  -p PORT, --port PORT  Port of webserver, usually 80
  -s SOCKETS, --sockets SOCKETS
                        Number of sockets to use in the test
  -v, --verbose         Increases logging
  -ua, --randuseragents
                        Randomizes user-agents with each request
  --https               Use HTTPS for the requests
  --sleeptime SLEEPTIME
                        Time to sleep between beats
```