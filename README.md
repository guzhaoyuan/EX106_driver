#EX106驱动程序
---
使用python的serial进行串口通信
##Usage
---
	python EX106util.py

##Structure
---
- EX106util.py #主程序入口
- EX106.py #底层驱动，串口通讯
- pid.py #pid算法实现
- readIMU.py #读取IMU数据并且使用
- testEX106.py #测试文件

##Dependency
---

- pySerial
- time