# test_framework
easy way to generate test cases for python

according to George:
```
這樣就造成令一個問題, 我們功能都開發好, 也手動debug 過了, 程式大體上穩定, 這時候我們回頭寫 test case 感覺就很蠢… 面對一個正常穩定的程式碼在寫他的 test case, 我們必須要反覆的 try and error 取得程式輸出… 但是, 我們在debug 的過程當中其實已經有作過測試了… 所以反覆作這些問題其實會很煩…

所以簡單來說這次要做的就是要 自動 產生 穩定code的 test case 的 framework!!!
```


## usage

put module.json files in ./schemas

```python
python test_generator.py
cd test_cases/
python test_add.py
>>> 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## json file format



