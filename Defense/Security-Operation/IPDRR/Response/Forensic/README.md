# Process
- Collection
- Parse and Search


## Linux 
1. OS info
- cmds
  - shell
  - 
- crontab
  - root/user
  - startup services
  - systemctl
  
- user
  - /etc/passwd
  - group

- files
  - high permissions
  - network connect
  
- ssh
  - authorized
  - known_hosts
  
- logs
  - last
  - history
  - audit
  - message
  - wtmp
  
- configure
  - ~/.profile   [ATT&CK](https://github.com/Jayway007/Offense-and-Deffense/blob/main/Offense/Red-Team/Persistence/Event_Triggered_Execution.md#unix-shell-configuration-modification)
  - ~/.bashrc
  - sudoer/SUID 
  
- kernel
  - info : /proc/*
  - kernel images
  
  
2. network
- netstat
- routes
- iptables
- hosts.allow/deny
- DNS info
- abnormal connection

3. process
  - cmdline
  - process-tree  
  - lsof
  - top

4. application
- logs
  - web
  - database
  
- configure
  - version
  - fingerprint
  - file
  
- path/file
 - important web path
 - files added or modified
 
5. scanning
- webshell
  - normal
  - mem-shell
  - root-kit


## Windows
- Registry
- 

## Response
- Security logs
- 


## Resources
- [数字取证大合集](https://blue.y1ng.org/0xA_digital_forensics/#awesome-forensics)  @y1ng
