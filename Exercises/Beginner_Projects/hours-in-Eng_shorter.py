# -*- coding: utf-8 -*-

def main():
    from sys import stdin, stdout

    standardinput = list(map(int, stdin.readline().split()))
    hourslist = ['one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight',
                    'nine',
                    'ten',
                    'eleven',
                    'twelve']
    hours = int(standardinput[0])
    minutes = int(standardinput[1])

    if hours in range(0,25,1) and minutes in range(0,46,15):
        if hours == 11 and minutes == 45:
            stdout.write('a quarter to twelve a.m.')
            exit()
        if hours == 23 and minutes == 45:
            stdout.write('a quarter to twelve p.m.')
            exit()
        if minutes in range(15,31):
            if minutes == 15:
                stdout.write('a quarter past ')
            elif minutes == 30:
                stdout.write('half past ')
        elif minutes == 45:
            stdout.write('a quarter to ')
            hours = hours + 1
        if hours in range(1,12,1):
           stdout.write(hourslist[hours-1])
           if minutes != 0:
               stdout.write(' a.m.')
           elif minutes == 0:
            stdout.write(" o' clock")
            stdout.write(' a.m.')
        elif hours in range(12,24,1) or hours == 0:
            stdout.write(hourslist[(hours-13)])
            if hours == 24 or 0:
                stdout.write('twelve')
            if minutes != 0:
                stdout.write(' p.m.')
            elif minutes == 0:
                stdout.write(" o'clock")
                stdout.write(' p.m.')
    else:
        stdout.write("Érvénytelen formátum, a helyes formátum ÓÓ PP! Invalid format, the correct format is HH MM. ")
        exit()
main()

