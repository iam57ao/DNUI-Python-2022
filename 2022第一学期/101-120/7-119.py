classA, classB = set(input()), set(input().split())
acmStu = set(input().split())
engStu = set(input().split())
leave = input()
print(f"""Total: {len(classA | classB)}
Not in race: {sorted((classA | classB) - (acmStu | engStu))}, num: {len((classA | classB) - (acmStu | engStu))}
All racers: {sorted(acmStu | engStu)}, num: {len(acmStu | engStu)}
ACM + English: {sorted(acmStu & engStu)}, num: {len(acmStu & engStu)}
Only ACM: {sorted(acmStu - engStu)}
Only English: {sorted(engStu - acmStu)}
ACM Or English: {sorted((acmStu | engStu) - (acmStu & engStu))}""")
if leave in classA:
    classA.remove(leave)
    print(sorted(classA))
elif leave in classB:
    classB.remove(leave)
    print(sorted(classB))
