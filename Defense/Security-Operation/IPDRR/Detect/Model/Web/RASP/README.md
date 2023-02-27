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
- Hook function
| Typpe  | Detect Principle | Hook function |
| ------------- | ------------- | ------------- |
| SQL Injection | 1. request parameter, mybatis: $,libjection to lexical analysis  2. hook SQL excute function | Statement.execute,Preparestatement,mybatis $ |
| Content Cell  | Content Cell  |
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
