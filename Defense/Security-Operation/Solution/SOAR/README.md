## Type
- automatic alarm handling


## Practice
- WAF：IP Block
- RASP ：block RCE / file access / oubound domain
- HIPS ：account delete/ webshell delete / iptables block / process kill / DNS / 
- Honeypot : DNS / WAF

## Process
```mermaid
graph TD;
    t_incidents-->t_alarms;
    detect_logic.py-->t_alarms; 
    
    t_alarms-->t_soar;
    monitor_1min.py-->t_soar;
    key_type-->t_soar;
    key_status-->t_soar;
    
    t_soar-->t_soar_result;
    key_action-->t_soar_result;
    key_metadata-->t_soar_result;
    soar_action.py-->t_soar_result;
    
    
    soar_action.py-->Security_API;
    switch_type-->Security_API;
    
```
