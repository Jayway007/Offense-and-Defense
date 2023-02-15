## Summary
- [Classification](#classification)
- [Rules](#rules)
- [Cases](#case)


## Classification
  - Business whitelist
    - Scene: unable to enumerate all attack scenes / unable to use experience / detect unknown attack scene
    - Types: Time seuence / unsupervised algorithm / 
    
  - Abnormal Blacklist
    - Types: count and frequency / response time and body size / behavior: time location action / 
    - 
  - Malicious Blacklist
    - Type: expert experience / Threat Inteligence /

  - Joint Detect
    - Type: logic / summary / sequence / attack chain /
  
  - Automation Analysis
    - Type：assets character / shell trigger
  

## Rules Develop
   - Function
     - match/regex
   - Semantic Analysis
   - Machine Learning
     - unsupervised algorithm
     - supervised algorithm: add tags
   - 

## Cases
- Case1  @[Huawei](https://mp.weixin.qq.com/s/AVlAoCPEJnNL_DuHGGD0Hg)

![attack case](https://mmbiz.qpic.cn/mmbiz_png/EjJibicwCQS5Soia2skxAg1rOhksZ8fibxQL6RDJcDzgCWGI39p4Ytzz41kUNFyic1icjdNDXr8zibxYU54exz2qdJ8PA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  - Bussiness whitelist ——> web upload api
  - Network blacklist ——> wget C2 script
  - Host blacklist ——> commands
  - Joint alarms ——> SOAR handling


### Tools

 ```mermaid
graph TD;
    Tools-->network;
    Tools-->host;
    Tools-->access;
    Tools-->common;
    
    network-->suricata;

    
```

## Algorithms 
- provenance graphs
  - [Provenance-based Intrusion Detection](https://tfjmp.org/slides/2020-winter.pdf)
  - [Threat detection and investigation with system-level provenance graphs](https://www.sciencedirect.com/science/article/pii/S0167404821001061)
