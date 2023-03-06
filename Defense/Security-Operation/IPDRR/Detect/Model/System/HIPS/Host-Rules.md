
## Process
| scene | rule | tacnic |
|------|-----------|-------|
| dowload file from external network | name: wget, curl, rsync, ftp, sftp | Init Access, resistence |
| reverse shell | 1. black command lines 2. file descriptor redirect to a socket or pipe 3. | |
| view sensitive information in system | cmd: tail, head, vi, cat, less, more, tac && file | Collection |
| RCE from Java Application | pathlink contains java && path contains /usr/bin/ | Execution | 
| ssh trust replationship | view file: known_host and login the same ip | Lateral Movement| 


## Network
| scene | rule | tacnic |
|------|-----------|-------|
| external connecting | CTI: black ip & domain | |
| internal access | high risk open port connection | |

## Log
| scene | rule | tacnic |
|------|-----------|-------|


## AI

| scene | rule | tacnic | link |
|------|-----------|-------|--|
| abnormal | child process relationship based on graph|   | [discovering-anomalous-patterns-based-on-parent-child-process-relationship](https://www.elastic.co/cn/blog/discovering-anomalous-patterns-based-on-parent-child-process-relationships) |


# Open-source
- [detection-rules-linux](https://github.com/elastic/detection-rules/tree/main/rules/linux)  @elastic


## Referer
- [如何利用AgentSmith-HIDS检测反弹shell](https://github.com/EBWi11/AgentSmith-HIDS/blob/master/doc/How-to-use-AgentSmith-HIDS-to-detect-reverse-shell/%E5%A6%82%E4%BD%95%E5%88%A9%E7%94%A8AgentSmith-HIDS%E6%A3%80%E6%B5%8B%E5%8F%8D%E5%BC%B9shell.md)

