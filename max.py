student_marks = [9.1,8.3,4.1]
max_marks = max(student_marks)
print(max_marks)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
ten_points = student_grades.count(10.0)
print(ten_points)

lst_pyth = "PYTHON"
print(lst_pyth.lower())

day_temperatures = dict([
    ("morning",28),
    ("noon",32),
    ("eveninig",25)
])
print(day_temperatures["morning"])

color_codes = (("red",182),("green",213),("blue",123))



day_temperatures={
    "morning":(23.5,23.6),
    "noon":(24.5,34),
    "evening":(22.1,13)
}
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
print(seconds)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]

del seconds[1:]
print(seconds)

lst=[10,20,300,13,12]
def calculate_length(lst_inp):
    print(len(lst))

calculate_length(lst)