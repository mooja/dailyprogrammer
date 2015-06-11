#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 136 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/
#
# June.11.2015


def main():
    nstudents, ngrades = raw_input().split()
    nstudents, ngrades = int(nstudents), int(ngrades)

    students = {}
    ngrades = 0
    total_grades_sum = 0

    for _ in range(nstudents):
        items = raw_input().strip().split()
        name = items[0]
        grades = map(int, items[1:])
        students[name] = grades
        ngrades += len(grades)
        total_grades_sum += sum(grades)

    total_avg = total_grades_sum / float(ngrades)
    print total_avg

    for student, grades in ((s, students[s]) for s in sorted(students.iterkeys())):
        student_avg = sum(grades) / float(len(grades))
        print student, '{:.2f}'.format(student_avg)


if __name__ == '__main__':
    main()
