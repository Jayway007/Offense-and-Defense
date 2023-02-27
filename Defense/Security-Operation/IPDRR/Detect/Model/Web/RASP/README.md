# Definition

# Principle
- java instrumentation
  - OpenRASP: Class--ClassLoader--define Transformer--if hook--javassist
- Servlet Filter
- bottom JVM replace
- virtualization
  - Waratek
 
 
# Design 
1. Reqest
   - parameter
   - json: value 


# Detection Type
- Hook Function

| Type | Detect Principle | Hook function | Bypass |
| ------------- | ------------- | ------------- |  ------------- |
| SQL Injection | 1. request parameter, mybatis: $,[libjection](https://github.com/libinjection/libinjection) to lexical analysis   2. hook SQL excute function | Statement.execute,Preparestatement,mybatis| specific type not monitor: restful, json, XML or origin |
| Cross Site Injection | [libjection](https://github.com/libinjection/libinjection) token handling and detect logic | Tag, Attrite key, value | Tab, Javascript |
| Command Injection  | hook String like: &\|<>`; and lexical analysis | Runtime.getRuntime.exec, ProcessImpl.start | Same as blacklist |
| XML External Entity Injection | 1. hook SystemId: gopher, file, http, ftp, jar 2. compare with !ENTITY |   |  |
| Unsecure Desirialization | hook and get target class, if exists in blacklist: CommonCollections | ObjectInputStream.resolveClass | |
| Expression Injection | hook and get target class, if exists in blacklist:Runtime, Shutdown | OgnlRuntime.callConstructor | |

- Context
- Business Whitelist

## Scenes
- vulnerability repair : hotfix
- Detect webshell : memshell : character ： classloader

# Block
- define rules
  - log4j : hook lookup function and extract the domain and version, generate the alarm and block the requests

# Operation key goal
 - coverage
 - efficiency
 - false positive
 - availability

# Open-source RASP
- [JRASP](https://www.jrasp.com/)
