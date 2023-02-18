## Pipeline
  Logstash can be used to extract and transform log data, ELB can be used to manage traffic to instances running Logstash, and Kafka can be used to integrate Logstash with other data processing systems. These tools can work together to build a robust and scalable data processing pipeline, 
### ELB
- ELB is Elastic load balancer. It is used to distribute incoming traffic across multiple instances of an application to improve its availability and scalability. ELB can be used to manage traffic to a set of backend instances that are running Logstash, for example, to improve the reliability and performance of log data processing.

### Logstash
- Logstash is an open-source data processing pipeline that can collect, parse, transform, and store data from various sources. It can be used to extract and transform log data from various applications, and it supports a wide range of input and output plugins for integrating with different data sources and destinations.

### Kafka
- Kafka is an open-source distributed streaming platform that can be used to build real-time data processing applications. It is designed to handle large volumes of data streams, and it can be used for a variety of use cases, including log data processing, event streaming, and messaging. Kafka can be used to integrate Logstash with other data processing tools and systems, and it provides a scalable and fault-tolerant messaging system for sending and receiving data.


## Type
 ```mermaid
graph TD;
    log-->security;
    log-->business;
    log-->CMDB;
    
    CMDB-->assets;
    CMDB-->vuls;
    
    assets-->domain;
    assets-->IP;
    assets-->version/software;
    assets-->acl;
    
    business-->web-access;
    business-->audit;
    audit-->apigw;
    audit-->vpn;
    audit-->cloud;
    
    security-->network;
    security-->host;
    security-->application;
    
    host-->alarms;
    host-->process;
    host-->history;
    host-->file;
    host-->network;
    
    
    network-->NDR;
    network-->NIPS;
    network-->honeypot;
    
    application-->WAF;
    application-->RASP;
    application-->fingerprint;
    application-->web-logs;
    
```



