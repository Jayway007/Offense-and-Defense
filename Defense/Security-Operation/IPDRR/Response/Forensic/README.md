# Process
- Collection
- Parse and Search

# Type
## `Linux`
1. OS info
- cmds
  - shell
  
- crontab
  - root/user
  - startup services
  - systemctl
  
- user
  - shadow
  - passwd
  - group

- files
  - high permissions
  - network connect
  
- ssh
  - authorized
  - known_hosts
  
- logs
  - last   ----/var/log/wtmp
  - lastlog ----/var/log/lastlog
  - lastb  ----/var/log/btmp
  - history
  - security
  - message
  - who  ----/var/run/utmp
  - audit
  
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
  - CWD
  - exe
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


## `Windows`
- Login log
- Event log
  - File open
  - Operation
  - Registery
- Application log
- File
  - Registry
  - Delete Recovery
- process
- network
- command history
- Memery
  - Dump
  - Rootkit


## Resources
- [数字取证大合集](https://blue.y1ng.org/0xA_digital_forensics/#awesome-forensics)  @y1ng
