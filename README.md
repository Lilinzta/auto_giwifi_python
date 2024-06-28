# 介绍

一个使用 selenium 实现的 giwif 自动登录脚本(适用于 LIT) ，默认每9分半重新登陆一次以实现白嫖。

> 宇宙免责声明: 本项目仅用于学习，不得用于非法用途，否则一切后果自负。

# 灵感来源

[GiraffeLe/Auto-Giwifi](https://github.com/GiraffeLe/Auto-Giwifi)

[老哥的分析过程](https://giraffele.site/post/%E6%B2%B3%E5%8D%97%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6GiWifi%E8%AE%A4%E8%AF%81%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90%E5%8F%8A%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95/)

本来打算只使用 python 的 requests 库来实现的，使用 selenium 的原因有以下两点：

1. 调试了半天，登录功能就是实现不了，一直报错。
2. 使用原作者的 js 实现时，请求登录个几次，就会提示 ”账户可用时长不足，请充值“ ，使用 requests 库实现的话，大概率会出现同样的问题。
3. 个人能力不足，之前没有深入接触过网络这一块的东西。其实代码大部分都是 [ChatGPT](https://chatgpt.com) 写的，本人只完成了调试和测试的工作。

# 使用

1. 克隆仓库

```bash
git clone https://github.com/Lilinzta/auto_giwifi_python.git
```

2. 创建并激活虚拟环境(可选)

```bash
python -m venv venv
source venv/bin/activate
```

2.5 安装依赖

```bash
pip install -r requirements.txt
```

3. 修改 config.toml 配置文件

```toml
# 校园网网关ip，LIT用户无需更改
base_url = "http://10.189.1.3"
# 打开浏览器，手动登录认证一次，获取地址栏url填入下面，LIT用户应该只需更改最后的ip地址(即校园网分配的ip地址)即可
open_url = "http://10.189.1.3/gportal/web/login?wlanacname=LITBAS4&wlanuserip=172.24.23.227"

[user_info]
uname = "YOUR_USERNAME"
passwd = "YOUR_PASSWORD"
```

4. 运行

```bash
python main.py
```
