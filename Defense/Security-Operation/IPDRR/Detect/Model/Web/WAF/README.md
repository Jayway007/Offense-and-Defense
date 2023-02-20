## Principle of WAF
- characters
- AST


## Value of WAF
 First defense line of the system and network.


## Rule maintenance
- Whitelists : manual & automation analysis
- payloads detection optimization : bypass
- Nday / 0day hotfix


## Platform
- WAF Summary dashboard
- Log search
- Monitor guesture


## Scenes
- potential vulnerability or success attack : response
- monitor guesture : top attacks number / type / source /
- attacks block
- identify targeted attack and group
- IAST baseed flow


## Rules：
- attack success : response characters / multiple requests but response differ
- auto block and unblock : score
- targeted or persistent attack
- false positive : cookie/referer/deviceID/srcIP/single-type/
- threat ioc : domain / IP
- specific attack technique : brute-force
- abnormal : probe availability or high CPU

 

## Response
- Target Analysis : target\type\time\weapon\ioc
- SOAR: Score and auto-block 
- Identify false positive & add to whitelists: characters

## Shortcoming
- Detection principle ：lack of summary / joint / algorithm
- Attack types : OOB / XSS
- Downgrade
- precise info : real_srcip


## Practice
- [WAF建设运营及AI应用实践](https://security.tencent.com/index.php/blog/msg/145) @Tencent
