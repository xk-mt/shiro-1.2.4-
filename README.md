# shiro-1.2.4-漏洞工具
解rememberMe值并导出对应的class文件

# 使用方式

## xk-mt-rememberMe解码.py

运行讲解：运行后先输入密钥或者回车默认密钥为‘kPH+bIxk5D2deZiIxcaaaA==’，在输入请求包里面的rememberMe值，解析后会提示输入导出文件名会自动加class,如果不导出则直接回车。

运行启动：```python xk-mt-rememberMe解码.py```

![image](https://github.com/xk-mt/CVE-2016-4437/assets/77874955/3c582326-f861-45ae-98c6-7ad487e309d5)

## xk-mt-单个域名单个密钥检测.py

运行讲解：运行时需要输入对应的key和url，key有默认值‘kPH+bIxk5D2deZiIxcaaaA==’，密钥必须是16字节的base64编码，验证不会执行系统命令，其中请求头的techo值如果回显到响应头则代表存在漏洞。

运行启动：

&nbsp;&nbsp;&nbsp;&nbsp;```python xk-mt-单个域名单个密钥检测.py -key kPH+bIxk5D2deZiIxcaaaA== -u http://127.0.0.1:8081/login```

&nbsp;&nbsp;&nbsp;&nbsp;```python xk-mt-单个域名单个密钥检测.py -url http://127.0.0.1:8081/login```

&nbsp;&nbsp;&nbsp;&nbsp;```python xk-mt-单个域名单个密钥检测.py -u http://127.0.0.1:8081/login```

![image](https://github.com/xk-mt/CVE-2016-4437/assets/77874955/3faa7976-73b5-4269-928d-bdabe12f5a40)

![image](https://github.com/xk-mt/CVE-2016-4437/assets/77874955/911d67a9-a376-4a33-b05d-8db358d220a3)

![image](https://github.com/xk-mt/CVE-2016-4437/assets/77874955/27775345-1bea-4a9d-a7db-22cd64ee5e02)


# 免责声明：
使用风险： 本工具仅供学习和技术研究目的使用。使用者应理解并接受使用该工具可能带来的风险和后果。

法律合规： 使用者必须确保在使用本工具的过程中遵守所有适用的法律法规。禁止使用本工具进行任何非法活动、攻击或侵犯隐私的行为。

免责声明： 本工具是按照"现状"提供的，没有任何形式的明示或暗示保证。使用者对使用本工具的结果负全部责任。

潜在风险： 本工具可能会导致系统故障、数据丢失或其他意外后果。使用者应该在合适的环境中进行测试，以减小潜在风险。

技术支持： 作者或维护者不提供对该工具的任何形式的技术支持。使用者应当依赖社区或其他渠道获取支持。

合理用途： 使用者应仅将本工具用于合法和良好用途，包括但不限于安全测试、研究和教育。

变更和更新： 作者或维护者保留随时更改或更新本工具的权利。使用者应定期查看相关文档和公告以获取最新信息。


# 通过使用本工具，使用者表明已经阅读并理解本免责声明，并同意遵守所有规定和条件。

