# at-coder

https://ron-tech.hatenablog.com/entry/2021/01/23/193107


oj login -u <userID> -p <PW> "https://atcoder.jp/"

oj login --check "https://atcoder.jp/"

### コンテストディレクトリを作るとき
acc new <コンテストID>

### 問題を追加するとき
acc add

### テストするとき
oj t -c "python answer.py" -d <testsディレクトリ>

### 提出するとき
acc submit answer.py
