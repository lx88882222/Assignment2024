# 第一讲作业

## 点灯

- 配置好CUBE IDE环境，完成STM32板载灯闪烁操作，并录制展示视频。
  - 闪烁方式：1秒亮灭各一次，即每500ms切换灯的亮灭状态
- 将录制好的展示视频以清华云盘链接的形式上传到网络学堂。
- 在Assignment-Embedded中创建`"{}_{}".format(name,sector)`格式的文件夹，其中创建blink.txt，里面写入清华云盘链接。
- 例：上传到Assignment-Embedded/李翔宇_硬件部/blink.txt
- 参考教程：https://obsidian-algebra-843.notion.site/STM32-ed7a3d1e61504aeca49f4b456c7a1012



## 串口双向通信

- 创建serialTest工程，使用串口实现A+B problem，即串口输入空格分隔的整数a，b，在同一个串口输出a+b的结果。
- 推荐使用在线串口调试助手https://itldg.github.io/web-serial-debug/（翻墙困难则用https://www.itldg.com/web_serial_debug/）
- 例：上传到Assignment-Embedded/李翔宇_硬件部/serailTest
- **重要！！！** 请确认serialTest文件夹下有.gitignore文件，并写入了正确的内容。如果没有，请自行创建，并写入以下内容

```
# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf
#disable build folder and its subfolders
build/
```



# 第二讲作业

- 观看[第二讲：PCB设计基础-基于立创EDA](https://cloud.tsinghua.edu.cn/d/79c394f05d4b425bb34c/files/?p=%2F%E8%AF%BE%E7%A8%8B%E5%86%85%E5%AE%B9%2F%E7%A1%AC%E4%BB%B6_PCB%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B_%E5%9F%BA%E4%BA%8E%E7%AB%8B%E5%88%9BEDA.mp4)

- 学习[立创EDA](https://pro.lceda.cn/)的基本操作，找到自己手里的stm32板子的资料（包括原理图和规格尺寸），绘制一块最基础的“扩展板”。

  - 要求：使用排母和排针，引出任意两个GPIO口，一排至少5个3V3，一排至少5个5V，一排至少5个GND，并创建铺铜区域，使得整块PCB的其他区域接地。资料可使用[这个](https://pan.baidu.com/s/1HH72h2E8srl6pn0-pe6Cyg?pwd=1234)

- 另存为工程为epro文件，不要设置密码。
![image-20240828123910571](https://github.com/user-attachments/assets/d0757425-3a98-4f35-be74-a9f7dd5f8889)

- 例：上传到Assignment-Embedded/李翔宇_硬件部/stm32_basic_extender.epro
