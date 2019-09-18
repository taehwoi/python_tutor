from konlpy.tag import Kkma

k = Kkma()
s = "치킨과 맥주를 한강에서 먹고 싶은 날씨"
print(k.nouns(s)) # 명사들
print(k.pos(s)) # 형태소 분석
