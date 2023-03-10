## Analysis
- 原始日志->特征工程->异常检测->人工验证->pattern提取->规则匹配


## Algorithm
- 社区发现: [Community Detection](https://towardsdatascience.com/community-detection-algorithms-9bd8951e7dae)
- 图算法
- VGG: converting binary files into color images can emphasize the image features more significantly
  - [一文读懂VGG网络](https://zhuanlan.zhihu.com/p/41423739)
  - [基于VGGNet的恶意代码变种分类](http://www.joca.cn/CN/10.11772/j.issn.1001-9081.2019050953?WebShieldDRSessionVerify=2Rng1AWxPzkRxQzqWmOR)

## Cases:
DNS logs analysis:
1. 密集请求型：例如随机子域名DDoS、反射型DDoS。其特征为QPS高、时序特征强，一般能够可视化观察到波峰。
2. 漏洞攻击型：例如针对DNS server的已知漏洞攻击。其特征为数量少、受DNS type影响，适合分类统计。如果批量PoC的话，则特征同1。
3. 数据传输型：例如DNS Tunnel、Malware DGA、PoC中的DNS回显、SSRF重绑定等。其特征在于域名文本特征明显、适用于规则匹配。
