lst_who = ['小马', '小羊', '小鹿']
lst_where = ['草地上', '电影院', '家里']
st_what = ['看电影', '听故事', '吃晚饭']
a, b, c = map(int, input().split(","))
print(f"{lst_who[a]}在{lst_where[b] + st_what[c]}")
