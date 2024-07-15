# def solution(str1, str2):
#     answer = 0
#     li1 = []
#     for i in range((len(str1))-1):
#         if str1[i].isalpha() and str1[i+1].isalpha():
#             li1.append((str1[i:i+2]).lower())
#     li1.sort()
#     print(li1)
#     li2 = []
#     for i in range(len(str2)-1):
#         if str2[i].isalpha() and str2[i+1].isalpha():
#             li2.append((str2[i:i+2]).lower())
#     li2.sort()
#     print(li2)
#     longer = 0
#     longer = max(len(li1), len(li2))
    
#     same_cnt = 0
#     all_cnt = 0 # len(li1) + len(li2) - same_cnt
    
#     if longer == 0:
#         answer = 65536
#     else:
#         if len(li1) == len(li2):
#             for i in range(len(li1)):
#                 if li1[i] == li2[i]:
#                     same_cnt += 1
#         elif len(li1) > len(li2):
#             for i in range(len(li2)):
#                 if li2[i] == li1[i]:
#                     same_cnt += 1
#         elif len(li1) < len(li2):
#             for i in range(len(li1)):
#                 if li1[i] == li2[i]:
#                     same_cnt += 1            
        
#         print(same_cnt)
#         all_cnt = len(li1) + len(li2) - same_cnt
#         print(all_cnt)
#         answer = int((same_cnt / all_cnt) * 65536)
#     return answer


def solution(str1, str2):
    # 두 글자씩 묶은 결과를 담을 리스트
    ngram1 = []
    ngram2 = []
    
    # str1에서 두 글자씩 묶기
    for i in range(len(str1) - 1):
        s = str1[i:i+2].lower()
        if s.isalpha():
            ngram1.append(s)
    
    # str2에서 두 글자씩 묶기
    for i in range(len(str2) - 1):
        s = str2[i:i+2].lower()
        if s.isalpha():
            ngram2.append(s)
    
    # 교집합 개수 구하기
    intersection = 0
    for ng1 in ngram1:
        if ng1 in ngram2:
            intersection += 1
            ngram2.remove(ng1)
    
    # 합집합 개수 구하기
    union = len(ngram1) + len(ngram2)
    
    # 유사도 계산
    if union == 0:
        answer = 65536
    else:
        answer = int(intersection / union * 65536)
    
    return answer
