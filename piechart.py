import matplotlib.pyplot as plt

labels = "Sleep", "School", "Coding Practice", "Gaming","Other"
sizes = [8,6,3,2,5]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
