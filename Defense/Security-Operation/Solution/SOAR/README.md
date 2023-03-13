## Type
- automatic alarm handling


## Practice
- WAF：IP Block
- RASP ：block RCE / file access / oubound domain
- HIPS ：account delete/ webshell delete / iptables block / process kill / DNS / 
- Honeypot : DNS / WAF

## Difficulty
- Fields Normalized

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
## database
- t_alarms

| type  | accident-id | title | SIP | DIP |
| ------- | ----- | ----- | ----- |  ----- |
| WAF  | accident-123  | Log4j injection | 9.9.9.9 | 10.1.1.3 |
| HIDS | accident-124  | Reverse shell | 7.7.7.7 | 10.1.1.4 |

- t_soar

| type  | job-id | title | SIP | DIP | action | 
| ------- | ----- | ----- | ----- |  ----- |  ----- |
| WAF  | job-123  | Log4j injection | 9.9.9.9 | 10.1.1.3 | block-ip |
| HIDS | job-124  | Reverse shell | 7.7.7.7 | 10.1.1.4 | kill-pid |

- Security_API
  - Router: type, action, metadata:{sip, dip}
    - POST /waf/block  {sip:"SIP"}
    - POST /hids/v1/api  {command: kill -9 \"pid\"}
