## Process



## Type
 ```mermaid
graph TD;
    log-->security;
    log-->business;
    log-->CMDB;
    CMDB-->assets;
    CMDB-->vuls;
    business-->logs;
    security-->network;
    security-->host;
    security-->application;
    host-->alarms;
    host-->access;
    host-->history/cmds;
    network-->NDR;
    network-->NIPS;
    network-->honeypot;
    
```



