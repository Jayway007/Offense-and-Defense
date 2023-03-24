# Process
## Scences
| scene | rule | tacnic |
|------|-----------|-------|
| dowload file from external network | name: wget, curl, rsync, ftp, sftp | Initial Access, resistence |
| reverse shell | 1. Blacklist cmdlines  2. File descriptor redirect to a socket or pipe  3. net connect: RAW socket | Initial Access |
| view sensitive information in system | cmd: tail, head, vi, cat, less, more, tac && file | Collection |
| RCE from Java Application | pathlink contains java && path contains /usr/bin/ | Execution | 
| ssh trust replationship |1. view file known_host and login the same ip 2. same srcIP logins to several target IPs | Lateral Movement| 
| port forwarding | 1. cmdlines contain 2. process connect intranet and internet | C2 |

## Logs
- path of program: 
  - write or upload files : /tmp, /root, /upload
  - web path : /webapps
  - fileless : /memfd
- net
  - protocol : socket
  - remote-port : 53
  - remote-ip : CTI
  - local-port 
    - out > 1024 
    - in : high-risk ports
- ancester
  - not sshd
- cmdline
  - sensitive commands or programs and params used: any program can be used 
  - sensitive paths 
    - /usr/bin
    - authentication
    - logs
- 

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
- [进程链关联及检测调研](https://www.cnblogs.com/Mang0/p/13878654.html)  @Mango
