#!/usr/bin/env python
# coding: utf-8

# ### 作业一：输出 9*9 乘法口诀表(注意格式)
# 
# 注意：提交作业时要有代码执行输出结果。

# In[5]:


def table():
    #在这里写下您的乘法口诀表代码吧！
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i)+'*'+str(j)+'='+str(i*j)+' ',end='\t')
        print()




if __name__ == '__main__':
    table()

