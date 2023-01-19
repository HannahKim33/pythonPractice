import pandas as pd

# df_exam=pd.read_excel('../Data/excel_exam.xlsx')    #./ : 현재 폴더   ../ : 상위 폴더
# print(df_exam)
#
# print(sum(df_exam['english'])/len(df_exam))
# print(sum(df_exam['science'])/len(df_exam))
#
# x=[1,2,3,4,5]
# print(x)
# print(len(x))
#
# df=pd.DataFrame({
#     "a":[1,2,3],
#     "b":[4,5,6]
# })
# print(df)
# print(len(df))  #행의 수

#읽어들일 엑셀파일에 header가 없을 경우 header=None을 써줘야 함. 안 그러면 맨 윗줄 레코드를 칼럼으로 인식한다.
# df_exam_novar=pd.read_excel("../Data/excel_exam_novar.xlsx", header=None)
# print(df_exam_novar)
# print(len(df_exam_novar))

#여러 시트 중 특정 시트를 읽어옴. sheet_name을 설정하지 않으면 첫 번째 시트를 읽어옴.
df_exam=pd.read_excel("../Data/excel_exam.xlsx", sheet_name='sist')
print(df_exam)

