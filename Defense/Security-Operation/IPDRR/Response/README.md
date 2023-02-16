## IOC Capture
 ```mermaid
graph TD;
    source -->Security-product;
    source -->Fishing;
    source -->Honeypot;
    
    Security-product -->srcIP;
    Security-product -->content;
    content -->number;
    content -->cookie;
    cookie -->number;
    
    content -->IP;
    content -->domain;
    
    Fishing -->domain;
    Fishing -->Server-IP;
    Fishing -->attachment;
    
    attachment -->IP;
    attachment -->domain;
    
    Honeypot -->IP;
    Honeypot -->browser;
    
    srcIP -->IP;
    Server-IP -->IP;

```


## Tracing Methods
 ```mermaid
graph TD;
    information -->IP;
    information -->Domain;
    information -->Phone-number;
    
    IP -->Basic;
    IP -->Open-port;
    IP -->Domain;
    IP -->Threat-Intelligence;
    
    Basic -->location;
    Basic -->Type/ASN/Supply;
    
    Open-port -->Blog;
    Open-port -->Info-closure;
    Open-port -->Counter;
    
    Threat-Intelligence -->feeds-search;
    Threat-Intelligence -->Google-hacking;
    
    
    Domain -->IP;
    Domain -->Email;
    Domain -->sub-domain;
    Domain -->Content;
    Domain -->Find-function;
    Domain -->Threat-Intelligence;
    
    Phone-number -->Social-media;
    Phone-number -->Register-website;
    
    
    Social-media -->Wechat/QQ/Alipay/Taobao;
    Social-media -->Weibo/Tiktok/Tieba/Maimai;
```


## Data Science 
 ```mermaid
graph TD;
    info -->data;
    info -->method;

    data -->srcip;
    data -->target;
    data -->CTI;
    data -->ioc;
    data -->attack_type;
    data -->specific_payload;
    data -->keywords;
    data -->time;
    data -->User-agent;
    data -->tools;
    data -->cookie;
    data -->other-rare-situation;


    method -->experience;
    method -->algorithm;
    
    experience -->specific;
    experience -->statistic;
    experience -->squence;
    
    specific -->ioc;
    specific -->payload;
    specific -->ip-segment&type;
    specific -->cookie;
       
    squence -->attack-type;
    squence -->tools;
    
    statistic -->ip&time;
    statistic -->attack-type;
    statistic -->time;
    
    algorithm -->LDA;
    algorithm -->isolation-forest;
    algorithm -->graph;
    
 ```

