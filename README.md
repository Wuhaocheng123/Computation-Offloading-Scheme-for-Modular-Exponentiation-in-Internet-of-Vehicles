# Calculation-Offloading-Scheme-for-Modular-Exponentiation-in-Internet-of-Vehicles
车联网环境下的计算卸载方案，共包含4方实体：RSU、Smart Car、Service Organization、MEC Server
![image](https://github.com/YinDFY/Calculation-Offloading-Scheme-for-Modular-Exponentiation-in-Internet-of-Vehicles/assets/127073326/db66bd27-ea4a-48a9-b008-13be9033b8d8)
![image](https://github.com/YinDFY/Calculation-Offloading-Scheme-for-Modular-Exponentiation-in-Internet-of-Vehicles/assets/127073326/a2d3f140-bcbf-4ecf-ad0b-06db90307d0b)
项目中的complete文件在一个py文件中模拟整个过程。

Smart car 中首先调用connectSA向SA发起初始化请求

SA 调用init生成初始化的参数

Smart car 调用localcompute 完成本地运算，再传输至MEC

MEC compute完成计算

RSU verification 完成验证过程，之后传输至Smart car聚合结果

Smar car 聚合最终结果generate_realanswer

使用python、mysql、socket等进行编程
