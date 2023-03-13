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
    monitor_alerms.py-->polling;
    polling-->t_soar;
    key_type-->t_soar;
    key_status-->t_soar;
    
    t_soar-->Security_API;  
    soar_action.py-->Security_API;
    switch_action_type-->Security_API;
    key_metadata-->Security_API;
    monitor_soar-->Security_API;
    
    Security_API-->execute_script;
    Security_API-->trigger_handler;
    Security_API-->t_soar_result;
```
