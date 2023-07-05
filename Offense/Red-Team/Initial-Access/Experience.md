# `Experience`
## 1. Misconfigure
- Nginx config
  - files: config / history / codes / authorization
  - upload
- Spingboot Actuator
- Cloud Service
- Other
  - bak, txt
  - dadabase file


## 2. Vulnerability
- SQL Injection : [clickhouse](https://blog.deteact.com/yandex-clickhouse-injection/)
- Open-source Nday:
  - Fastjson
  - Log4j
  - Shiro
- Third-party products Nday:
  - Yongyou
  - Jypter
  - CMS
  - VPN command injection
  - F5 RCE & Bypass
- XSS : POST / DOM 
- File upload : directory
- Experssion Language Injection
- Code review to 0day
  - File operation
  - 

## 3. API Pentest
- sensitive APIs in js files : unauth
- path brute-force : wordlists


## 4. Service Pentesting
- password brute-force: weak password
- sensitive ports
  - Unauthorization Access: Redis, Mongodb, Etcd, Rsync, Kafka, Zookeper, [Docker](https://askding.github.io/Kali/Exploit/Docker.html), Haddop
  - Specific scene : 
    - [IOT](https://cloud.tencent.com/developer/article/1776815)
    - [Mosquitto-1883](https://book.hacktricks.xyz/network-services-pentesting/1883-pentesting-mqtt-mosquitto)(RabbitMQ)
      ```
      mosquitto_sub -h ip -p port -t '$SYS/#' --cafile --insecure
      ```
- JRMP/[JMX](https://www.anquanke.com/post/id/200682)/RMI 
- [network-services-pentesting](https://book.hacktricks.xyz/network-services-pentesting/)  @hacktricks


## 5. Bypass
- XFF bypass subdomain ACL whitelist : reverse proxy : localhost 
- office network whitelist IP


## 6. Business Logic
- sensitive function/service: FaaS
- text template render from third-part provider
- normal user priviledge escape & internal movement

## Easier ways ---> Side doors
- hidden assest: single ip, domain concat port urls, rare ports and service
- 404/401 pages: path bruteforce
- other types of endpoits: mobile, laptop
- supply chain

