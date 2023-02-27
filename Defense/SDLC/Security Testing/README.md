## DAST
## SAST
## IAST
### 1.Flow-based
- browser/client proxy
- traffic mirroring
  - Nginx: proxy pass
  - WAF


### 2.Stack-based
- active
  - hook dangerous function and send check payload

- passive
  - detect based on string match and sink trace, no need send request, no dirty data
