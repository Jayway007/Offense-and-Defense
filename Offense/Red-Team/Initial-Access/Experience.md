## `Experience`
### 1. Misconfigure
- Nginx config
  - files: config / history / codes / authorization
  - upload
- Spingboot Actuator
- Cloud Service
- Other
  - bak, txt
  - dadabase file

### 2. Vulnerability
- SQL Injection : [clickhouse](https://blog.deteact.com/yandex-clickhouse-injection/)
- Open-source Nday:
  - Fastjson
  - Log4j
  - Shiro
- Third-party products Nday:
  - Yongyou
  - Jypter
  - CMS
  - VPN command injection: ../
- XSS : POST / DOM 
- File upload : directory

### 3. API Pentest
- sensitive APIs in js files
- path brute-force : wordlists

### 4. Open Port
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

### 5. Bypass
- XFF bypass subdomain ACL whitelist : reverse proxy : localhost 
- office network whitelist IP 

## `Resources`


