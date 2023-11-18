import datetime
import requests, re
from bs4 import BeautifulSoup
import write

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# =========================================== 학교코드 ===========================================
#시도교육청코드
SC_CODE = "ur code"
#행정표준코드
SD_CODE = "ur code"

# ================================ 파일위치 (역슬레쉬 2번씩 넣기) =================================
#txt파일위치
txtfile = "ur file"
#png파일위치
pngfile = "ur file"
#폰트파일위치
fontfile = "ur file"

# ===================================== 색깔코드(HEXCODE) ========================================
#배경색깔
backclr = "ur code"
#글씨색깔
txtclr = "ur code"

# ===============================================================================================

#오늘의 날짜
today = datetime.date.today().strftime('%Y%m%d')
url = str("https://open.neis.go.kr/hub/mealServiceDietInfo?ATPT_OFCDC_SC_CODE=" + SC_CODE + "&SD_SCHUL_CODE=" + SD_CODE + "&MLSV_YMD=" + today)

#크롤링
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
data = soup.get_text().replace("<br/>", "")
td_dataset = []
t = 0

#파일오픈
f = open(txtfile,"w+")

#데이터 기록
for i in data.splitlines():
    if t == 17: td_dataset.append(i)#re.sub("[^가-힣 ]", "", i)
    t += 1

try: mfilter = td_dataset[0].split("1.")
except: pass

#데이터 정리
for i in range(1, len(mfilter)):
    a = mfilter[i].strip(" ")
    a = re.sub(r"\(.*?\)", "", a)
    a = a.strip("()")
    a = re.sub("[^가-힣]", "", a)

    if a == "":
        continue
    #출력
    print(a)
    f.write(f'{a}\n')

#파일 닫기
f.close()

#파일열기
with open(txtfile, "r") as f:
    meal = f.readlines()
#색깔설정
img = PIL.Image.new("RGB", (1080, 1080), (backclr))
#이미지 제작
draw = PIL.ImageDraw.Draw(img)
font = PIL.ImageFont.truetype(fontfile, 100)

for i in range(len(meal)):
    draw.text((100, 150 * i), meal[i], font=font, fill=(txtclr))

#이미지 저장
img.save(pngfile)