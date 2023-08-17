from josaa.models import programm
import csv


def run():
    with open('data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        programm.objects.all().delete()
        for row in reader:
            p = programm(
                        institute=row[1],
                        program=row[2],
                        seat_type=row[3],
                        gender=row[4],
                        open=row[5],
                        close=row[6],
                        year=row[7],
                        roundd=row[8]
                        )
            p.save()