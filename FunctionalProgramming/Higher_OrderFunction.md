## 高阶函数
1. ### 函数本身能够赋值给对象
    猜测原因是因为python中的变量本质是应用的缘故
2. ### 函数本身就是一个对象
    `abs = 10`这段代码是成立的
3. ### 函数可以作为参数使用
    ```
   def add_abs(x, y, fabs):
    return fabs(x) + fabs(y)
   ```
   外层的add_abs函数就是所谓的高阶函数