## Summary
- [Classification](#classification)
- [Rules](#rules)
- [Cases](#case)


## Theory
  Distinguish the differences between normal actions, suspicious actions and attacking actions.

## Classification
| classification  | Blacklist | Whitelist |
| ------------- | ------------- | ------------- | 
| Definition  | define the characters of attack actions  | define the normal actions, others are abnormal|
| Advantages  | 1. precise | 1. unkown attacks |
|   | 1. explainable | 2.few updates |
| Disadvantages  | 1.False negative  | 1.False positive |
|  | 2.professional experience | 2.Unexplainable and understandable |

## Types
  - Business whitelist
    - Scene: unable to enumerate all attack scenes / unable to use experience / detect unknown attack scene
    - Types: Time seuence / unsupervised algorithm / 
    
  - Abnormal Blacklist
    - Types: count and frequency / response time and body size / behavior: time location action / 
    - 
  - Malicious Blacklist
    - Type: expert experience / Threat Inteligence /

  - Joint Detect
    - Type: logic / summary / sequence / attack chain / several ruels of same time&target / 
  
  - Automation Analysis
    - Type：assets character / external trigger API or shell
  

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


## Algorithms 
- provenance graphs
  - [Provenance-based Intrusion Detection](https://tfjmp.org/slides/2020-winter.pdf)
  - [Threat detection and investigation with system-level provenance graphs](https://www.sciencedirect.com/science/article/pii/S0167404821001061)
