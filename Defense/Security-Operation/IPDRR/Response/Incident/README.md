## Drill

## Playbook
### Step by step
- Investigatation
  - cmd used to analyze : zgrep
- Block
  - Network : unbind / ACL / iptables
  - Application : WAF / RASP / business
  - Host : islation / kill process / configure
- Forensic
- Recover

## Process
- record the timeline and evidence
- send to related personnel
- review and optimization

## Forensic

  - Automatic Query, merge and analyze:
    - IOC of IP : CTI / bind domain / NIPS / HIPS net or process or cmdlne / WAF / RASP / log 
    - IOC of domain : CTI / bind IP / NIPS / DNS / cmdline / log
    - External IP : bind IP and domain / owner / fingerprint / web vulnerability / 
    - Host IP : basic / business / owner / bind IP / public access / ACLs / HIPS / RASP / login audit
  - Docker scene

## Reference
- [从“复盘”到“复仇”，谈如何正确的复盘](https://www.secrss.com/articles/29912) @君哥
- Mitre-事前之中事后
