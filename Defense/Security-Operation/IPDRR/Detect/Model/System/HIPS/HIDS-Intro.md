## Summary
 - [Introduction](#introduction)
 - [Functions](#functions)
 - [Agent information Collection](#information)
   - [Process](#1-process)
   - [Network](#2-network)
   - [File](#3-file)
- [Reference](#reference)

## Introduction
   Host intrusion detection usually divided into two parts: agent and server.
   
   **Agent** is responsible for collecting information, sorting out relevant information and sending it to the server.
   
   **Server** is usually used as an information center to deploy rules, collect data obtained from various security components, analyze the data, and determine whether host behavior is abnormal based on rules, and alarms and prompts the abnormal behaviors of the host.
   
## Functions
- Assets management
- Vulnerability management
- Benchmark check
- Host information Collection
- Intrusion detection alarms
- Analysis and Response 
- Extender script



## Information
### 1. Process 
  In the Linux operating system, almost all operations and intrusion behaviors are reflected in the executed commands, and the essence of command execution is to start the process, therefore, the monitoring of processes is the monitoring of command execution.
#### 1.1 Data  
  Basically obtain data below:
 
| Data  | Meaning |
| ------------- | ------------- |
| create_time | File creation time  |
| modify_time | Last file modification time  |
| path | The path of executable file  |
| pid | Process id  |
| uid | Uer id of the user who started the process  |
| gid | Group id of the user who started the process  |
| path | The path of executable file  |
| cmdline | Process start command  |
| cmdlink | command links of process call  |
| pathlink | Executable file path links of process call  |
| ancestor_info | Ancestor Process pid & path & cmdline |
| parent_info | Parent Process pid & path & cmdline |
| net |  network connection related to process : ip & port  |
| fd | File descriptor |  

#### 1.2 Monitoring methods 
  Process monitoring usually use hook technology, roughly divided into two types：
- _Application-level(Ring3)_ : simple but easy be bypassed
  -  Hijack glibc library
  -  LD_preload


- _Kernel-level(Ring0/Ring1)_ :  complex and may cause compatibility problems, kernel may panic but cannot be bypassed in principle
  - Netlink Connector
  - Audit
  - [Systemcall](https://mp.weixin.qq.com/s/ntE5FNM8UaXQFC5l4iKUUw)  @驭龙
  - Ebpf
  
- referer
  - [Linux 入侵检测中的进程创建监控](https://www.freebuf.com/column/208928.html)

### Detection rules


### 2. Network 
  In the Linux o
  
#### 2.1 Data  
  Basically obtain data below:
 
| Data  | Meaning |
| ------------- | ------------- |
| create_time | File creation time  |
| modify_time | Last file modification time  |
| path | The path of executable file  |
| pid | Process id  |

#### 2.2 Monitoring methods 
  Process monitoring
  
  
### 3. File 
  In the Linux o
  
  
#### 3.1 Data  
- Basically obtain data below:
 
| Data  | Meaning |
| ------------- | ------------- |
| create_time | File creation time  |
| modify_time | Last file modification time  |
| path | The path of executable file  |
| pid | Process id  |

- events are as below:
  
 access/modify/attrib/close_write/close/open/move/create/delete/unmount


#### 3.2 Monitoring methods 
  - [inotify](https://medium.com/100-days-of-linux/an-introduction-to-file-system-monitoring-tools-afd99164ce66) : a Linux kernel subsystem that reports file system changes to applications.
  - [Watchman](https://www.tecmint.com/watchman-monitor-file-changes-in-linux/) : an open source and cross-platform file watching service that watches files and records or performs actions when they change
  - [auditd] : Linux Audit system


## Docker Detection



## Reference
- [Linux HIDS agent Summary and User Status HOOK [1]](https://paper.seebug.org/1104/)  @Seebug
- 
