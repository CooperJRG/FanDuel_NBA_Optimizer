import pandas
from itertools import combinations as comb
import itertools

path = input("File Path: ")
depth = input("How much are you willing to pay per point? ")
amount = input("How many lineups do you want? ")
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)
df = pandas.read_csv(path, error_bad_lines=False)
df = df[df["FPPG"] >= 17]
df = df[df["Injury Indicator"] != "O"]
df = df[df["Injury Indicator"] != "GTD"]
df = df.reset_index()
df = df[["Nickname", "FPPG", "Salary", "Roster Position"]]
p_c = df[df["Roster Position"] == "C"]
p_c = p_c.reset_index()
p_sg = df[df["Roster Position"] == "SG"]
p_sg = p_sg.reset_index()
p_pg = df[df["Roster Position"] == "PG"]
p_pg = p_pg.reset_index()
p_pf = df[df["Roster Position"] == "PF"]
p_pf = p_pf.reset_index()
p_sf = df[df["Roster Position"] == "SF"]
p_sf = p_sf.reset_index()
print("Successfully gathered data")


def combine(a):
    x = len(a)
    x_range = list(range(x))
    return list(comb(x_range, 2))


sf_comb = combine(p_sf)
pf_comb = combine(p_pf)
sg_comb = combine(p_sg)
pg_comb = combine(p_pg)

def points(a, b, c):
    value_b = float(a.loc[b]["FPPG"])
    value_c = float(a.loc[c]["FPPG"])
    value = value_b + value_c
    return value


def salary(a, b, c):
    value_b = float(a.loc[b]["Salary"])
    value_c = float(a.loc[c]["Salary"])
    value = value_b + value_c
    return value


def split(word):
    return [char for char in word]


sf_point = []
sg_point = []
pf_point = []
pg_point = []
c_point = []
for i in list(range(len(sf_comb))):
    word = sf_comb[i]
    x = (split(word))
    sf_point.append(points(p_sf, x[0], x[1]))

for i in list(range(len(sg_comb))):
    word = sg_comb[i]
    x = (split(word))
    sg_point.append(points(p_sg, x[0], x[1]))

for i in list(range(len(pf_comb))):
    word = pf_comb[i]
    x = (split(word))
    pf_point.append(points(p_pf, x[0], x[1]))

for i in list(range(len(pg_comb))):
    word = pg_comb[i]
    x = (split(word))
    pg_point.append(points(p_pg, x[0], x[1]))

for i in list(range(len(p_c))):
    x = float(p_c.loc[i]["FPPG"])
    c_point.append(x)

sf_salary = []
sg_salary = []
pf_salary = []
pg_salary = []
c_salary = []
for i in list(range(len(sf_comb))):
    word = sf_comb[i]
    x = (split(word))
    sf_salary.append(salary(p_sf, x[0], x[1]))

for i in list(range(len(sg_comb))):
    word = sg_comb[i]
    x = (split(word))
    sg_salary.append(salary(p_sg, x[0], x[1]))

for i in list(range(len(pf_comb))):
    word = pf_comb[i]
    x = (split(word))
    pf_salary.append(salary(p_pf, x[0], x[1]))

for i in list(range(len(pg_comb))):
    word = pg_comb[i]
    x = (split(word))
    pg_salary.append(salary(p_pg, x[0], x[1]))

for i in list(range(len(p_c))):
    x = float(p_c.loc[i]["Salary"])
    c_salary.append(x)
print("Successfully split data into relevant variables")
sf = list(range(len(sf_comb)))
sg = list(range(len(sg_comb)))
pf = list(range(len(pf_comb)))
pg = list(range(len(pg_comb)))
c = list(range(len(p_c)))
sf_ratio = []
pf_ratio = []
sg_ratio = []
pg_ratio = []
c_ratio = []
for i in sf:
    sf_ratio.append(sf_salary[i] / sf_point[i])
for i in sg:
    sg_ratio.append(sg_salary[i] / sg_point[i])
for i in pf:
    pf_ratio.append(pf_salary[i] / pf_point[i])
for i in pg:
    pg_ratio.append(pg_salary[i] / pg_point[i])
for i in c:
    c_ratio.append(c_salary[i] / c_point[i])

sf_glue = []
sg_glue = []
pf_glue = []
pg_glue = []
c_glue = []


def glue(a, b, c, d):
    z = zip(a, b, c, d)
    sort = sorted(z)
    tuples = zip(*sort)
    a, b, c, d = [list(tuple) for tuple in tuples]
    return a, b, c, d


pf_glue, pf_order, pf_sal, pf_point = (glue(pf_ratio, pf_comb, pf_salary, pf_point))
c_glue, c_order, c_sal, c_point = (glue(c_ratio, c, c_salary, c_point))
sf_glue, sf_order, sf_sal, sf_point = (glue(sf_ratio, sf_comb, sf_salary, sf_point))
sg_glue, sg_order, sg_sal, sg_point = (glue(sg_ratio, sg_comb, sg_salary, sg_point))
pg_glue, pg_order, pg_sal, pg_point = (glue(pg_ratio, pg_comb, pg_salary, pg_point))
pf_count = 0
sf_count = 0
sg_count = 0
pg_count = 0
c_count = 0

depth = float(depth)

for i in pf_glue:
    if i > depth:
        pf_count = pf_count + 1
for i in list(range(pf_count)):
    pf_glue.pop()
    pf_order.pop()
    pf_sal.pop()
    pf_point.pop()
for i in sf_glue:
    if i > depth:
        sf_count = sf_count + 1
for i in list(range(sf_count)):
    sf_glue.pop()
    sf_order.pop()
    sf_sal.pop()
    sf_point.pop()
for i in pg_glue:
    if i > depth:
        pg_count = pg_count + 1
for i in list(range(pg_count)):
    pg_glue.pop()
    pg_order.pop()
    pg_sal.pop()
    pg_point.pop()
for i in pg_glue:
    if i > depth:
        pg_count = pg_count + 1
for i in list(range(sg_count)):
    sg_glue.pop()
    sg_order.pop()
    sg_sal.pop()
    sg_point.pop()
for i in c_glue:
    if i > depth:
        c_count = c_count + 1
for i in list(range(c_count)):
    c_glue.pop()
    c_order.pop()
    c_sal.pop()
    c_point.pop()
final = []

print("Successfully narrowed potential line-ups")


def array(a, b, c):
    return pandas.DataFrame({'Salary': a, 'FPPG': b, 'Index': c})


sg_list = array(sg_sal, sg_point, sg_order)
sg_list.columns = ['Salary', 'FPPG', 'SG_Index']
sf_list = array(sf_sal, sf_point, sf_order)
sf_list.columns = ['Salary', 'FPPG', 'SF_Index']
pg_list = array(pg_sal, pg_point, pg_order)
pg_list.columns = ['Salary', 'FPPG', 'PG_Index']
pf_list = array(pf_sal, pf_point, pf_order)
pf_list.columns = ['Salary', 'FPPG', 'PF_Index']
c_list = array(c_sal, c_point, c_order)
c_list.columns = ['Salary', 'FPPG', 'C_Index']

final_sal = sg_list['Salary'], pg_list['Salary'], pf_list['Salary'], sf_list['Salary'], c_list['Salary']
final_order = sg_list['SG_Index'], pg_list['PG_Index'], pf_list['PF_Index'], sf_list['SF_Index'], c_list['C_Index']
final_point = sg_list['FPPG'], pg_list['FPPG'], pf_list['FPPG'], sf_list['FPPG'], c_list['FPPG']
total_sal = pandas.DataFrame(itertools.product(*final_sal))
total_point = pandas.DataFrame(itertools.product(*final_point))
total_order = pandas.DataFrame(itertools.product(*final_order))

total_sal["sum"] = total_sal.sum(axis=1)
total_point['points'] = total_point.sum(axis=1)
total_order.columns = ['SG_Index', 'PG_Index', 'PF_Index', 'SF_Index', 'C_Index']
total = pandas.concat([total_sal["sum"], total_point['points'], total_order], axis=1)
print("Successfully generated ", len(total.index), " line-ups")
total = total[total['sum'] <= 60000]
total = total[total['sum'] >= 58000]
total = total[total['points'] >= 300]
total = total.sort_values(by=["points"], ascending=False)
total = total.reset_index()
print("Successfully narrowed down to best possible lineups")
Predicted_Points = []
Salary_F = []
Point_Guard1 = []
Point_Guard2 = []
Shooting_Guard1 = []
Shooting_Guard2 = []
Small_Forward1 = []
Small_Forward2 = []
Power_Forward1 = []
Power_Forward2 = []
Center0 = []

for i in list(range(len(total.index))):
    SG_T = list(total.at[i, "SG_Index"])
    SG_F1 = SG_T[0]
    SG_F2 = SG_T[1]
    SF_T = list(total.at[i, "SF_Index"])
    SF_F1 = SF_T[0]
    SF_F2 = SF_T[1]
    PG_T = list(total.at[i, "PG_Index"])
    PG_F1 = PG_T[0]
    PG_F2 = PG_T[1]
    PF_T = list(total.at[i, "PF_Index"])
    PF_F1 = PF_T[0]
    PF_F2 = PF_T[1]
    C_T = total.at[i, "C_Index"]
    Predicted_Points.append(total.at[i, "points"])
    Salary_F.append(total.at[i, "sum"])
    Point_Guard1.append(p_pg.at[PG_F1, "Nickname"])
    Point_Guard2.append(p_pg.at[PG_F2, "Nickname"])
    Shooting_Guard1.append(p_sg.at[SG_F1, "Nickname"])
    Shooting_Guard2.append(p_sg.at[SG_F2, "Nickname"])
    Small_Forward1.append(p_sf.at[SF_F1, "Nickname"])
    Small_Forward2.append(p_sf.at[SF_F2, "Nickname"])
    Power_Forward1.append(p_pf.at[PF_F1, "Nickname"])
    Power_Forward2.append(p_pf.at[PF_F2, "Nickname"])
    Center0.append(p_c.at[C_T, "Nickname"])
Lineups = pandas.DataFrame({'Total Salary': Salary_F, 'Points': Predicted_Points, '1st Point Guard': Point_Guard1,
                            '2nd Point Guard': Point_Guard2, 'st Shooting Guard': Shooting_Guard1,
                            '2nd Shooting Guard': Shooting_Guard2, '1st Small Forward': Small_Forward1,
                            '2nd Small Forward': Small_Forward2, '1st Power Forward': Power_Forward1,
                            '2nd Power Forward': Power_Forward2, 'Center': Center0})

print(Lineups.head(int(amount)))