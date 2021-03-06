
# **서울시 구별 CCTV 현황 분석**


```python
import pandas as pd
import numpy as np
```


```python
import matplotlib
import matplotlib.font_manager as fm
from matplotlib import rc
fm.get_fontconfig_fonts()

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname = font_location, size = 50).get_name()
matplotlib.rc('font', family = font_name)
```


```python
CCTV_Seoul = pd.read_csv('CCTV_in_Seoul.csv', encoding = 'utf-8')
```


```python
CCTV_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관명</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 기존 컬럼 '기관명'을 '구별'로 바꿔준다.
CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0]: '구별'}, inplace = True)
CCTV_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul = pd.read_excel('population_in_Seoul.xls',
                         header = 2,                       # 세 번째 줄부터 읽어오기
                         parse_cols = 'B, D, G, J, N',     # B, D, G, J, N 열만 읽어오기
                         encoding = 'utf-8')
pop_Seoul.head(3)
```

    C:\Users\Administrator\Anaconda3\lib\site-packages\ipykernel_launcher.py:4: FutureWarning: the 'parse_cols' keyword is deprecated, use 'usecols' instead
      after removing the cwd from sys.path.
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>자치구</th>
      <th>계</th>
      <th>계.1</th>
      <th>계.2</th>
      <th>65세이상고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10197604.0</td>
      <td>9926968.0</td>
      <td>270636.0</td>
      <td>1321458.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 위에서 컬럼멍이 이상하므로 수정
pop_Seoul.rename(columns = {pop_Seoul.columns[0]: '구별',
                           pop_Seoul.columns[1]: '인구수',
                           pop_Seoul.columns[2]: '한국인',
                           pop_Seoul.columns[3]: '외국인',
                           pop_Seoul.columns[4]: '고령자'}, inplace = True)

pop_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10197604.0</td>
      <td>9926968.0</td>
      <td>270636.0</td>
      <td>1321458.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
  </tbody>
</table>
</div>



---

## **(1) CCTV 데이터 살펴보기**


```python
# CCTV가 가장 적은 구는 '도봉구', '마포구', '송파구', '중랑구', '중구'이다.
CCTV_Seoul.sort_values(by = '소계', ascending = True).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>485</td>
      <td>238</td>
      <td>159</td>
      <td>42</td>
      <td>386</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>574</td>
      <td>314</td>
      <td>118</td>
      <td>169</td>
      <td>379</td>
    </tr>
    <tr>
      <th>17</th>
      <td>송파구</td>
      <td>618</td>
      <td>529</td>
      <td>21</td>
      <td>68</td>
      <td>463</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>660</td>
      <td>509</td>
      <td>121</td>
      <td>177</td>
      <td>109</td>
    </tr>
    <tr>
      <th>23</th>
      <td>중구</td>
      <td>671</td>
      <td>413</td>
      <td>190</td>
      <td>72</td>
      <td>348</td>
    </tr>
  </tbody>
</table>
</div>




```python
# CCTV가 가장 많은 구는 '강남구', '양천구', '서초구', '은평구', '용산구'이다.
CCTV_Seoul.sort_values(by = '소계', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>2034</td>
      <td>1843</td>
      <td>142</td>
      <td>30</td>
      <td>467</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>1930</td>
      <td>1406</td>
      <td>157</td>
      <td>336</td>
      <td>398</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>1873</td>
      <td>1138</td>
      <td>224</td>
      <td>278</td>
      <td>468</td>
    </tr>
    <tr>
      <th>20</th>
      <td>용산구</td>
      <td>1624</td>
      <td>1368</td>
      <td>218</td>
      <td>112</td>
      <td>398</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 3년간 CCTV 증가율 계산하기
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                          CCTV_Seoul['2014년'] / CCTV_Seoul['2013년도 이전'] * 100)

CCTV_Seoul.sort_values(by = '최근증가율', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>최근증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
      <td>1549.281734</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
      <td>1033.732861</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>1265</td>
      <td>542</td>
      <td>57</td>
      <td>451</td>
      <td>516</td>
      <td>977.516605</td>
    </tr>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>1002</td>
      <td>464</td>
      <td>314</td>
      <td>211</td>
      <td>630</td>
      <td>908.672414</td>
    </tr>
    <tr>
      <th>10</th>
      <td>동대문구</td>
      <td>1294</td>
      <td>1070</td>
      <td>23</td>
      <td>198</td>
      <td>579</td>
      <td>779.149533</td>
    </tr>
  </tbody>
</table>
</div>



## **(2) 인구 데이터 살펴보기**


```python
pop_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10197604.0</td>
      <td>9926968.0</td>
      <td>270636.0</td>
      <td>1321458.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul.drop([0], inplace = True)
pop_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# '구별' 컬럼의 unique 조사하기
# unique는 반복된 데이터는 하나로 나타내서 한 번 이상 나타난 데이터를 확인하는 것
pop_Seoul['구별'].unique()

# Nan값 찾고 제거하기
pop_Seoul[pop_Seoul['구별'].isnull()]
pop_Seoul.drop([26], inplace = True)
```


```python
# 각 구별로 '외국인비율'과 '고령자비율' 계산하기
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100

pop_Seoul.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
      <td>5.669451</td>
      <td>15.615404</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
      <td>6.700690</td>
      <td>15.583909</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
      <td>6.038828</td>
      <td>14.836427</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 외국인비율이 높은 구 추출하기
pop_Seoul.sort_values(by = '외국인비율', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>402985.0</td>
      <td>368072.0</td>
      <td>34913.0</td>
      <td>52413.0</td>
      <td>8.663598</td>
      <td>13.006191</td>
    </tr>
    <tr>
      <th>18</th>
      <td>금천구</td>
      <td>255082.0</td>
      <td>236353.0</td>
      <td>18729.0</td>
      <td>32970.0</td>
      <td>7.342345</td>
      <td>12.925255</td>
    </tr>
    <tr>
      <th>17</th>
      <td>구로구</td>
      <td>447874.0</td>
      <td>416487.0</td>
      <td>31387.0</td>
      <td>56833.0</td>
      <td>7.007998</td>
      <td>12.689506</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
      <td>6.700690</td>
      <td>15.583909</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
      <td>6.038828</td>
      <td>14.836427</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 고령자비율이 높은 구 추출하기
pop_Seoul.sort_values(by = '고령자비율', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>강북구</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
      <td>1.061806</td>
      <td>16.600342</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
      <td>5.669451</td>
      <td>15.615404</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
      <td>6.700690</td>
      <td>15.583909</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
      <td>6.038828</td>
      <td>14.836427</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>327163.0</td>
      <td>314982.0</td>
      <td>12181.0</td>
      <td>48161.0</td>
      <td>3.723221</td>
      <td>14.720797</td>
    </tr>
  </tbody>
</table>
</div>



---
## **(연습) 데이터프레임 병합하기**


```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index = [4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index = [8, 9, 10, 11])


```


```python
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                    index = [2, 3, 6, 7])
```

* **pd.concat**
    * **pd.concat(['objs', 'axis=0', "join='outer'", 'join_axes=None', 'ignore_index=False', 'keys=None', 'levels=None', 'names=None', 'verify_integrity=False', 'sort=None', 'copy=True'])**


```python
# concat 명령어로 데이터를 열 방향으로 단순하 합치기
result = pd.concat([df1, df2, df3])
result
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# concat 명령에 keys 옵션으로 구분하기
# key 지정된 구분은 다중 index가 되어서 level을 형성한다.
result = pd.concat([df1, df2, df3], keys = ['x', 'y', 'z'])
```


```python
# df1과 df2 합치기
df1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B6</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B7</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
# concat 명령은 index를 기준으로 합치기 때문에 값을 가질 수 없는 부분은 NaN이 저정된다.
result = pd.concat([df1, df4], axis = 1)
result
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B6</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B7</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 공통된 index로 합치고 공통되지 않은 index의 데이터는 버리도록 하는 옵션이 join = 'inner'이다.
result = pd.concat([df1, df4], axis = 1, join = 'inner')
result
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# join_axes = [df1.index] 옵션으로 df1의 인덱스에 맞추도록 할 수도 있다.
result = pd.concat([df1, df4], axis = 1, join_axes = [df1.index])
result
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ignore_index = True 옵션을 잡으면 두 데이터의 index를 무시하고 합친 후 새로 index를 부여한다.
result = pd.concat([df1, df4], ignore_index = True)
result
```

    C:\Users\Administrator\Anaconda3\lib\site-packages\ipykernel_launcher.py:2: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
    of pandas will change to not sort by default.
    
    To accept the future behavior, pass 'sort=False'.
    
    To retain the current behavior and silence the warning, pass 'sort=True'.
    
      
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>B2</td>
      <td>NaN</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>B3</td>
      <td>NaN</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>B6</td>
      <td>NaN</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>B7</td>
      <td>NaN</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>



* **pd.merge**
    * **pd.merge(['left', 'right', "how='inner'", 'on=None', 'left_on=None', 'right_on=None', 'left_index=False', 'right_index=False', 'sort=False', "suffixes=('_x', '_y')", 'copy=True', 'indicator=False', 'validate=None'])**


```python
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                    'key': ['K0', 'K4', 'K2', 'K3']})

right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3'],
                     'key': ['K0', 'K1', 'K2', 'K3']})
```


```python
left
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>K4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
      <th>key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C0</td>
      <td>D0</td>
      <td>K0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C1</td>
      <td>D1</td>
      <td>K1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C2</td>
      <td>D2</td>
      <td>K2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C3</td>
      <td>D3</td>
      <td>K3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# left, right에 공통으로 있는 컬럼인 key를 기준으로 on 옵션으로 합친다.
pd.merge(left, right, on = 'key')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# how 옵션으로 두 데이터를 하나씩 기준으로 합칠 수도 있다.
pd.merge(left, right, how = 'left', on = 'key')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>K4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, how = 'right', on = 'key')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>K1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# outer 옵션을 사용하면 마치 합집합처럼 merge가 되며 공통된 요소가 아닌 곳은 NaN 처리가 된다.
pd.merge(left, right, how = 'outer', on = 'key')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>K4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>K1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# inner 옵션을 사용하면 마치 교집합처럼 merge가 된다. outer와 다르게 Null값이 없다.
pd.merge(left, right, how = 'inner', on = 'key')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A3</td>
      <td>B3</td>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



---


```python
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on = '구별')
data_result.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
      <td>558.121372</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
      <td>0.929765</td>
      <td>12.051638</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
      <td>374.520325</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
      <td>1.061806</td>
      <td>16.600342</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 의미 없는 컬럼 지우기
# drop 행 방향으로 삭제 / del 열 방향으로 삭제
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>558.121372</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
      <td>0.929765</td>
      <td>12.051638</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>374.520325</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
      <td>1.061806</td>
      <td>16.600342</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 나중에 그래프를 그릴 것을 생각하면 index는 구 이름으로 바꾸는 것이 유리하다.
# set_index 명령어로 index를 바꿔준다.
data_result.set_index('구별', inplace = True)
data_result.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>773</td>
      <td>558.121372</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
      <td>0.929765</td>
      <td>12.051638</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>748</td>
      <td>374.520325</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
      <td>1.061806</td>
      <td>16.600342</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>884</td>
      <td>331.494845</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
      <td>1.080540</td>
      <td>12.015794</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1496</td>
      <td>1033.732861</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
      <td>3.484582</td>
      <td>12.955291</td>
    </tr>
  </tbody>
</table>
</div>



---
## **numpy의 corrcef 명령어로 상관계수 조사하기**
* **고령자비율, 외국인비율, 인구수 중에서 무슨 데이터와 CCTV를 비교할지 정해보도록 하겠습니다. 그렇게 하는 가장 단순한 작업이 상관계수를 조사하는 것입니다. 상관계수의 절대값이 클수록 두 데이터는 관계가 있다고 볼 수 있습니다.**
* **상관분석을 인터넷에서 검색해보면, 상관계수의 절대값이 0.1 이하면 거의 무시, 0.3 이하면 약한 상관관계, 0.7 이하면 뚜렷한 상관관계라고 나옵니다.**
* **상관관계는 numpy에 있는 corrcoef 명령어를 사용합니다. 이 명령의 결과는 행렬로 나타납니다. 주 대각선을 기준으로 대칭인 행렬이고 대각선 빼고 다른 값을 읽으면 됩니다.**

* **np.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>)**


```python
# 고령자비율 상관관계
# 고령자비율은 -0.28 수준이므로 '약한 음의 상관관계'를 보인다.
np.corrcoef(data_result['고령자비율'], data_result['소계'])
```




    array([[ 1.        , -0.28078554],
           [-0.28078554,  1.        ]])




```python
# 외국인비율 상관관계
# 외국인비율은 -0.13 수준이므로 '거의 무시 상관관계'를 보인다.
np.corrcoef(data_result['외국인비율'], data_result['소계'])
```




    array([[ 1.        , -0.13607433],
           [-0.13607433,  1.        ]])




```python
# 인구수 상관관계
# 인구수는 0.3 수준이므로 '약한 상관관계'를 보인다.
np.corrcoef(data_result['외국인비율'], data_result['소계'])
```




    array([[ 1.        , -0.13607433],
           [-0.13607433,  1.        ]])




```python
# CCTV와 인구수의 관계를 파악하기
data_result.sort_values(by = '소계', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2034</td>
      <td>504.704829</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
      <td>0.839413</td>
      <td>11.036964</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>1930</td>
      <td>745.166430</td>
      <td>450310.0</td>
      <td>445994.0</td>
      <td>4316.0</td>
      <td>51733.0</td>
      <td>0.958451</td>
      <td>11.488308</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>1873</td>
      <td>765.683656</td>
      <td>494388.0</td>
      <td>489943.0</td>
      <td>4445.0</td>
      <td>72334.0</td>
      <td>0.899091</td>
      <td>14.631019</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>1624</td>
      <td>525.935673</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
      <td>6.038828</td>
      <td>14.836427</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.sort_values(by = '인구수', ascending = False).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>송파구</th>
      <td>618</td>
      <td>534.969754</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
      <td>1.033584</td>
      <td>10.862599</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>884</td>
      <td>331.494845</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
      <td>1.080540</td>
      <td>12.015794</td>
    </tr>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>1265</td>
      <td>977.516605</td>
      <td>569384.0</td>
      <td>565565.0</td>
      <td>3819.0</td>
      <td>71941.0</td>
      <td>0.670725</td>
      <td>12.634883</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1496</td>
      <td>1033.732861</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
      <td>3.484582</td>
      <td>12.955291</td>
    </tr>
  </tbody>
</table>
</div>



---
## **(연습) 파이썬의 대표 시각화 도구 Matplotlib**
* **Matplotlib에서 그래프를 그리는 모듈은 matplotlib.pyplot이고 plt로 줄여서 씁니다.**
* **%matplotlib inline 명령은 그래프 결과를 출력 세션에 나타나게 하는 설정입니다.**


```python
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
plt.figure
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
plt.show()
```


![output_54_0](https://user-images.githubusercontent.com/42408554/55370324-137b8300-5535-11e9-9db3-9efaad0b5bef.png)



```python
t = np.arange(0, 12, 0.01)
y = np.sin(t)
```


```python
plt.figure(figsize = (10, 6))
plt.plot(t, y)
plt.show()
```


![output_56_0](https://user-images.githubusercontent.com/42408554/55370331-1a09fa80-5535-11e9-871f-a8bcdb0d2ccd.png)



```python
# 격자와 x축, y축 이름 지정하기
plt.figure(figsize = (10, 6))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()
```
![image](https://user-images.githubusercontent.com/42408554/55370337-21310880-5535-11e9-8e5e-4c44f6238622.png)


```python
# grid 그리고 제목 지정하기
plt.figure(figsize = (10, 6))
plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid(linestyle = '-')
plt.xlabel('time', color = 'white')
plt.ylabel('Amplitude', color = 'white')
plt.title('Example of sinewave', color = 'white')
plt.show()
```


![output_58_0](https://user-images.githubusercontent.com/42408554/55370348-27bf8000-5535-11e9-91ae-a43f38bf2e78.png)




```python
# 라벨 지정하기
plt.figure(figsize = (10, 6))
plt.plot(t, np.sin(t), label = 'sin')
plt.plot(t, np.cos(t), label = 'cos')
plt.grid()
plt.legend()
plt.xlabel('time', color = 'white')
plt.ylabel('Amplitude', color = 'white')
plt.title('Example of sinewave')
plt.show
```




    <function matplotlib.pyplot.show(*args, **kw)>



![output_59_1](https://user-images.githubusercontent.com/42408554/55370355-2ee68e00-5535-11e9-9d2e-267596e2a3b8.png)



```python
# lw 옵션으로 선의 굵기 지정
plt.figure(figsize = (10, 6))
plt.plot(t, np.sin(t), lw = 3, label = 'sin')
plt.plot(t, np.cos(t), color = 'r', label = 'cos')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()
```


![output_60_0](https://user-images.githubusercontent.com/42408554/55370357-35750580-5535-11e9-9fd7-e3761e736aad.png)



```python
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize = (10, 6))
plt.plot(t, y, color = 'green')
plt.show()
```


![output_61_0](https://user-images.githubusercontent.com/42408554/55370365-3ad25000-5535-11e9-977c-806d516733ce.png)



```python
plt.figure(figsize = (10, 6))
plt.plot(t, y, color = 'green', linestyle = '--', lw = 2)
plt.show()
```


![output_62_0](https://user-images.githubusercontent.com/42408554/55370375-3f970400-5535-11e9-8ff6-a853a424405c.png)




```python
plt.figure(figsize = (10, 6))
plt.plot(t, y, color = 'green', linestyle = '--', marker = 'o')
```




    [<matplotlib.lines.Line2D at 0x2456c2fbe48>]




![output_63_1](https://user-images.githubusercontent.com/42408554/55370377-445bb800-5535-11e9-8841-a81992d732de.png)




```python
plt.figure(figsize = (10, 6))
plt.plot(t, y, color = 'green', linestyle = '--', marker = 'o',
        markerfacecolor = 'blue', markersize = 12)
plt.xlim([-0.5, 6.5])
plt.ylim([0.5, 9.5])
plt.show()
```


![output_64_0](https://user-images.githubusercontent.com/42408554/55370380-49b90280-5535-11e9-8244-17ac64da5800.png)



* **plt.scatter(['x', 'y', 's=None', 'c=None', 'marker=None', 'cmap=None', 'norm=None', 'vmin=None', 'vmax=None', 'alpha=None', 'linewidths=None', 'verts=None','edgecolors=None','*', 'data=None','**kwargs'])**


```python
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 9, 8, 3, 2, 4, 3, 4])
plt.scatter(t, y)
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370388-5178a700-5535-11e9-91c3-15ba62dbccff.png)




```python
plt.figure(figsize = (10, 6))
plt.scatter(t, y, marker = '>')
```




    <matplotlib.collections.PathCollection at 0x2456d9f3ef0>




![image](https://user-images.githubusercontent.com/42408554/55370399-576e8800-5535-11e9-81b2-6f7b899d93d2.png)



```python
color_map = t

plt.figure(figsize = (10, 6))
plt.scatter(t, y, s = 50, c = color_map, marker = '>')
plt.colorbar()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370412-5fc6c300-5535-11e9-8cd7-f8f077aa156a.png)




```python
s1 = np.random.normal(loc = 0, scale = 1, size = 1000)
s2 = np.random.normal(loc = 5, scale = 0.5, size = 1000)
s3 = np.random.normal(loc = 10, scale = 2, size = 1000)
```


```python
plt.figure(figsize = (10, 6))
plt.plot(s1, label = 's1')
plt.plot(s2, label = 's2')
plt.plot(s3, label = 's3')
plt.legend()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370423-65bca400-5535-11e9-81a7-ad0506481edb.png)




```python
plt.figure(figsize = (10, 6))
plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370434-6b19ee80-5535-11e9-8e06-db4117aa4843.png)



---
## **CCTV 현황 그래프로 분석하기**

* **bar 그래프로 시각화**


```python
data_result.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>773</td>
      <td>558.121372</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
      <td>0.929765</td>
      <td>12.051638</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>748</td>
      <td>374.520325</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
      <td>1.061806</td>
      <td>16.600342</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 강남구, 양천구, 서초구, 은평구에 많은 CCTV가 설치되어 있다.
data_result['소계'].sort_values().plot(kind = 'barh', grid = True, figsize = (10, 10))
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370446-71a86600-5535-11e9-898d-427a3545e7ee.png)




```python
# 인구 대비 CCTV 비율을 계산해서 정렬하고 시각화하기
# 인구 대비로 보면 용산구와 종로구가 상당히 높은 반면, 송파구는 인구 대비로 보아도 CCTV 비율이 낮다.
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind = 'barh', grid = True, figsize = (10, 10))
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370454-7705b080-5535-11e9-92cf-a2f328dfafef.png)



* **scatter 그래프로 시각화**


```python
plt.figure(figsize = (6, 6))
plt.scatter(data_result['인구수'], data_result['소계'], s = 50)
plt.xlabel('인구수', color = 'white')
plt.ylabel('CCTV', color = 'white')
plt.grid()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370457-7c62fb00-5535-11e9-8f61-ef809b4da0da.png)



```python
# numpy의 polyfit 명령으로 직선을 만들 수 있습니다.
# 직선을 그리기 위해 x축과 y축 데이터를 얻어야 하는데, x축 데이터는 numpy의 linspace로 만들고,
# y축은 poly1d로 만들 수 있습니다.
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1
```




    array([1.30916415e-03, 6.45066497e+02])




```python
f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 10000)
```

![image](https://user-images.githubusercontent.com/42408554/55370496-9ef51400-5535-11e9-81be-b94142b71543.png)



```python
plt.figure(figsize = (10, 10))
plt.scatter(data_result['인구수'], data_result['소계'], s = 50)
plt.plot(fx, f1(fx), ls = 'dashed', lw = 3, color = 'green')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370504-a3b9c800-5535-11e9-9a3d-09c3994a20f0.png)



* **위의 그래프에서 직선이 인구수가 300,000명 일 때, CCTV는 1,100대 정도여야 한다는 개념을 이야기하는 것이라면 직선 상단(CCTV가 기준치보다 많은 곳), 직선 하단(CCTV가 기준치보다 적은 곳)을 의미한다.**
* **따라서 오차를 계산할 수 있는 코드를 만들고 오차가 큰 순으로 데이터를 정렬한다.**


```python
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

df_sort = data_result.sort_values(by = '오차', ascending = False)
df_sort.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
      <th>CCTV비율</th>
      <th>오차</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>1549.281734</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
      <td>0.867660</td>
      <td>11.072217</td>
      <td>0.487292</td>
      <td>1388.055355</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>618</td>
      <td>534.969754</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
      <td>1.033584</td>
      <td>10.862599</td>
      <td>0.092587</td>
      <td>900.911312</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2034</td>
      <td>504.704829</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
      <td>0.839413</td>
      <td>11.036964</td>
      <td>0.423769</td>
      <td>760.563512</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (14, 10))
plt.scatter(data_result['인구수'], data_result['소계'],
           c = data_result['오차'], s =50)
plt.plot(fx, f1(fx), ls = 'dashed', lw = 3, color = 'green')

for n in range(10):
    plt.text(df_sort['인구수'][n] * 1.02, df_sort['소계'][n] * 0.98,
            df_sort.index[n], fontsize = 15)

plt.xlabel('인구수')
plt.ylabel('인구당비율')

plt.colorbar()
plt.grid()
plt.show()
```


![image](https://user-images.githubusercontent.com/42408554/55370511-a9afa900-5535-11e9-9e9e-d8c5f6cf88ac.png)


