import csv
import matplotlib.pyplot as plt

years = []
spots = []

with open("../data/ISSN_M_tot.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        years.append(float(row["year"])) 
        spots.append(float(row["total"]))
plt.style.use('bmh')
ax = plt.gca()
ax.set_facecolor("#131D55FF")
plt.plot(years, spots, color="#E27A19FF")
plt.title("Number of sunspots x Years")
plt.xlabel("Year")
plt.ylabel("Number of Sunspots")
plt.show()