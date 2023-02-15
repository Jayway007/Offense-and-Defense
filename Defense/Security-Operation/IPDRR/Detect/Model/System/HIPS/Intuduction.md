## Summary
 - [Introduction](#introduction)
 - [Functions](#functions)
 - [Agent information Collection](#information)
   - Process
   - Network
   - File

## Introduction
   Host intrusion detection usually divided into two parts: agent and server.
   
   **Agent** is responsible for collecting information, sorting out relevant information and sending it to the server.
   
   **Server** is usually used as an information center to deploy rules, collect data obtained from various security components, analyze the data, and determine whether host behavior is abnormal based on rules, and alarms and prompts the abnormal behaviors of the host.
   

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
  -  hijack libc library
  -  
- _Kernel-level(Ring0/Ring1)_ :  complex and may cause compatibility problems, kernel may panic but cannot be bypassed in principle
  
